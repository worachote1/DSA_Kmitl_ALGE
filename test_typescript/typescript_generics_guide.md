# TypeScript Generics Mastery Guide

## 🎯 Level 1: Generic Basics

### What are Generics?
Generics allow you to create reusable components that work with multiple types while maintaining type safety.

```typescript
// Without generics - limited and repetitive
function getFirstString(items: string[]): string | undefined {
  return items[0];
}

function getFirstNumber(items: number[]): number | undefined {
  return items[0];
}

// With generics - flexible and reusable
function getFirst<T>(items: T[]): T | undefined {
  return items[0];
}

// Usage
const firstString = getFirst(['a', 'b', 'c']); // string | undefined
const firstNumber = getFirst([1, 2, 3]);       // number | undefined
const firstUser = getFirst(users);             // User | undefined
```

### Generic Constraints
Limit what types can be used with your generic.

```typescript
// Constraint: T must have an 'id' property
interface Identifiable {
  id: string | number;
}

function updateById<T extends Identifiable>(items: T[], id: string | number, updates: Partial<T>): T[] {
  return items.map(item => 
    item.id === id ? { ...item, ...updates } : item
  );
}

// Usage
interface User extends Identifiable {
  id: number;
  name: string;
  email: string;
}

const users: User[] = [
  { id: 1, name: "John", email: "john@example.com" }
];

// ✅ Works - User has id property
const updatedUsers = updateById(users, 1, { name: "Jane" });

// ❌ Error - string doesn't have id property
// const result = updateById(["a", "b"], 1, {});
```

---

## 🎯 Level 2: Advanced Generic Patterns

### Multiple Type Parameters
```typescript
// Generic with multiple type parameters
interface ApiResponse<TData, TError = string> {
  data?: TData;
  error?: TError;
  status: number;
}

// Custom error type
interface ValidationError {
  field: string;
  message: string;
}

// Usage examples
const userResponse: ApiResponse<User> = {
  data: { id: 1, name: "John", email: "john@example.com" },
  status: 200
};

const validationResponse: ApiResponse<User, ValidationError[]> = {
  error: [{ field: "email", message: "Invalid email format" }],
  status: 400
};
```

### Generic Utility Functions
```typescript
// Pick specific properties from an object
function pick<T, K extends keyof T>(obj: T, keys: K[]): Pick<T, K> {
  const result = {} as Pick<T, K>;
  keys.forEach(key => {
    result[key] = obj[key];
  });
  return result;
}

// Usage
interface User {
  id: number;
  name: string;
  email: string;
  password: string;
}

const user: User = {
  id: 1,
  name: "John",
  email: "john@example.com",
  password: "secret123"
};

// Only pick safe properties for API response
const publicUser = pick(user, ['id', 'name', 'email']); 
// Type: { id: number; name: string; email: string; }
```

---

## 🎯 Level 3: React Component Generics

### Generic Table Component
```typescript
interface TableColumn<T> {
  key: keyof T;
  header: string;
  render?: (value: T[keyof T], item: T) => React.ReactNode;
  sortable?: boolean;
}

interface TableProps<T> {
  data: T[];
  columns: TableColumn<T>[];
  onRowClick?: (item: T) => void;
  keyExtractor: (item: T) => string | number;
}

function Table<T>({ 
  data, 
  columns, 
  onRowClick, 
  keyExtractor 
}: TableProps<T>): JSX.Element {
  return (
    <table>
      <thead>
        <tr>
          {columns.map(column => (
            <th key={String(column.key)}>{column.header}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map(item => (
          <tr 
            key={keyExtractor(item)} 
            onClick={() => onRowClick?.(item)}
            style={{ cursor: onRowClick ? 'pointer' : 'default' }}
          >
            {columns.map(column => (
              <td key={String(column.key)}>
                {column.render 
                  ? column.render(item[column.key], item)
                  : String(item[column.key])
                }
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

// Usage Example
interface Product {
  id: string;
  name: string;
  price: number;
  category: string;
}

const products: Product[] = [
  { id: "1", name: "Laptop", price: 999, category: "Electronics" },
  { id: "2", name: "Book", price: 29, category: "Education" }
];

const productColumns: TableColumn<Product>[] = [
  { key: 'name', header: 'Product Name' },
  { 
    key: 'price', 
    header: 'Price',
    render: (price) => `$${price}` 
  },
  { key: 'category', header: 'Category' }
];

// Component usage
<Table<Product>
  data={products}
  columns={productColumns}
  keyExtractor={(product) => product.id}
  onRowClick={(product) => console.log('Clicked:', product)}
/>
```

### Generic Form Hook
```typescript
interface FormState<T> {
  values: T;
  errors: Partial<Record<keyof T, string>>;
  touched: Partial<Record<keyof T, boolean>>;
}

interface FormActions<T> {
  setValue: <K extends keyof T>(field: K, value: T[K]) => void;
  setError: (field: keyof T, error: string) => void;
  setTouched: (field: keyof T, touched: boolean) => void;
  reset: () => void;
  validate: () => boolean;
}

function useForm<T extends Record<string, any>>(
  initialValues: T,
  validationRules?: Partial<Record<keyof T, (value: any) => string | undefined>>
): FormState<T> & FormActions<T> {
  const [state, setState] = React.useState<FormState<T>>({
    values: initialValues,
    errors: {},
    touched: {}
  });

  const setValue = <K extends keyof T>(field: K, value: T[K]) => {
    setState(prev => ({
      ...prev,
      values: { ...prev.values, [field]: value },
      errors: { ...prev.errors, [field]: undefined } // Clear error on change
    }));
  };

  const setError = (field: keyof T, error: string) => {
    setState(prev => ({
      ...prev,
      errors: { ...prev.errors, [field]: error }
    }));
  };

  const setTouched = (field: keyof T, touched: boolean) => {
    setState(prev => ({
      ...prev,
      touched: { ...prev.touched, [field]: touched }
    }));
  };

  const reset = () => {
    setState({
      values: initialValues,
      errors: {},
      touched: {}
    });
  };

  const validate = (): boolean => {
    if (!validationRules) return true;
    
    let isValid = true;
    const newErrors: Partial<Record<keyof T, string>> = {};

    Object.keys(validationRules).forEach(field => {
      const rule = validationRules[field as keyof T];
      if (rule) {
        const error = rule(state.values[field as keyof T]);
        if (error) {
          newErrors[field as keyof T] = error;
          isValid = false;
        }
      }
    });

    setState(prev => ({ ...prev, errors: newErrors }));
    return isValid;
  };

  return {
    ...state,
    setValue,
    setError,
    setTouched,
    reset,
    validate
  };
}

// Usage Example
interface LoginForm {
  email: string;
  password: string;
}

const LoginComponent = () => {
  const form = useForm<LoginForm>(
    { email: '', password: '' },
    {
      email: (value) => !value ? 'Email is required' : 
              !/\S+@\S+\.\S+/.test(value) ? 'Invalid email' : undefined,
      password: (value) => !value ? 'Password is required' :
                 value.length < 6 ? 'Password must be at least 6 characters' : undefined
    }
  );

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (form.validate()) {
      console.log('Form submitted:', form.values);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        value={form.values.email}
        onChange={(e) => form.setValue('email', e.target.value)}
        onBlur={() => form.setTouched('email', true)}
      />
      {form.touched.email && form.errors.email && (
        <span style={{ color: 'red' }}>{form.errors.email}</span>
      )}
      
      <input
        type="password"
        value={form.values.password}
        onChange={(e) => form.setValue('password', e.target.value)}
        onBlur={() => form.setTouched('password', true)}
      />
      {form.touched.password && form.errors.password && (
        <span style={{ color: 'red' }}>{form.errors.password}</span>
      )}
      
      <button type="submit">Login</button>
    </form>
  );
};
```

---

## 🎯 Level 4: Advanced Utility Types

### Conditional Types
```typescript
// Extract function return types
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;

// Usage
function getUserById(id: number): Promise<User> {
  return Promise.resolve({ id, name: "John", email: "john@example.com" });
}

type UserPromise = ReturnType<typeof getUserById>; // Promise<User>

// Extract array element type
type ArrayElement<T> = T extends (infer U)[] ? U : never;

type StringArray = string[];
type StringElement = ArrayElement<StringArray>; // string
```

### Mapped Types with Generics
```typescript
// Make all properties optional except specified ones
type PartialExcept<T, K extends keyof T> = Partial<T> & Pick<T, K>;

interface User {
  id: number;
  name: string;
  email: string;
  age: number;
}

// All optional except id
type CreateUser = PartialExcept<User, 'id'>;
// { id: number; name?: string; email?: string; age?: number; }

// Create API response wrapper
type ApiEndpoint<T> = {
  [K in keyof T]: T[K] extends (...args: any[]) => any
    ? (...args: Parameters<T[K]>) => Promise<ApiResponse<ReturnType<T[K]>>>
    : never;
};

interface UserService {
  getUser: (id: number) => User;
  createUser: (user: CreateUser) => User;
  deleteUser: (id: number) => boolean;
}

type UserApiService = ApiEndpoint<UserService>;
// {
//   getUser: (id: number) => Promise<ApiResponse<User>>;
//   createUser: (user: CreateUser) => Promise<ApiResponse<User>>;
//   deleteUser: (id: number) => Promise<ApiResponse<boolean>>;
// }
```

---

## 🧪 Practice Challenges

Try these challenges to test your understanding:

### Challenge 1: Generic Cache
Create a generic cache class that can store any type of data with string keys.

```typescript
// Your implementation here
class Cache<T> {
  // TODO: Implement this
}

// Should work like this:
const userCache = new Cache<User>();
userCache.set('user1', { id: 1, name: 'John', email: 'john@example.com' });
const user = userCache.get('user1'); // User | undefined
```

### Challenge 2: Generic Repository Pattern
Create a generic repository interface for CRUD operations.

```typescript
// Your implementation here
interface Repository<T, TId> {
  // TODO: Define methods
}

// Should work with any entity type
const userRepo: Repository<User, number> = new UserRepository();
const productRepo: Repository<Product, string> = new ProductRepository();
```

### Challenge 3: Generic Event Emitter
Create a type-safe event emitter that ensures event names match their payload types.

```typescript
// Your implementation here
class TypedEventEmitter<TEvents> {
  // TODO: Implement this
}

// Usage
interface AppEvents {
  'user:login': { userId: number; timestamp: Date };
  'user:logout': { userId: number };
  'error': { message: string; code: number };
}

const emitter = new TypedEventEmitter<AppEvents>();
// Should be type-safe
emitter.emit('user:login', { userId: 1, timestamp: new Date() }); // ✅
emitter.emit('user:login', { userId: 1 }); // ❌ Should error - missing timestamp
```

---

## 📝 Best Practices Summary

1. **Use meaningful generic parameter names**: `T`, `TData`, `TKey` instead of just `T`, `U`, `V`
2. **Add constraints when needed**: Use `extends` to limit generic types
3. **Provide defaults for optional generics**: `<T = string>` when appropriate
4. **Keep generics simple**: Don't over-engineer, use when you need reusability
5. **Document complex generics**: Add JSDoc comments for complex generic functions
6. **Test with different types**: Ensure your generics work with various type combinations

Ready for the challenges? Try implementing the solutions and I'll review them with you!