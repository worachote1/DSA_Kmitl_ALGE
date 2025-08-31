---

## 📝 Quiz Solutions

### Question 1: Type Inference
```typescript
// ❌ This won't work as intended - conditional types in return position are tricky
function processData<T>(data: T[]): T extends string ? string[] : number[] {
  // TypeScript can't infer this properly in function return types
}

// ✅ Better approaches:

// Option A: Function overloads
function processData(data: string[]): string[];
function processData(data: number[]): number[];
function processData<T>(data: T[]): T[] {
  return data; // Your processing logic here
}

// Option B: Conditional types with proper inference
type ProcessResult<T> = T extends string ? string[] : T extends number ? number[] : T[];

function processData<T>(data: T[]): ProcessResult<T> {
  return data as ProcessResult<T>;
}

// Usage
const strings = processData(['a', 'b']); // string[]
const numbers = processData([1, 2]);     // number[]
```

### Question 2: Conditional Types
```typescript
type IsArray<T> = T extends any[] ? true : false;

type Test1 = IsArray<string[]>; // true  ✅
type Test2 = IsArray<string>;   // false ✅  
type Test3 = IsArray<number[]>; // true  ✅

// More advanced examples:
type IsFunction<T> = T extends (...args: any[]) => any ? true : false;
type IsPromise<T> = T extends Promise<any> ? true : false;

type FuncTest = IsFunction<() => void>;     // true
type PromiseTest = IsPromise<Promise<User>>; // true
type StringTest = IsFunction<string>;       // false
```

### Question 3: Mapped Types
```typescript
// Solution:
type MakeOptional<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>;

// How it works:
// 1. Omit<T, K> - Remove the specified properties from T
// 2. Pick<T, K> - Extract only the specified properties  
// 3. Partial<Pick<T, K>> - Make those picked properties optional
// 4. & - Intersection: combine the types

// Usage example:
interface User {
  id: number;
  name: string;
  email: string;
}

type UserWithOptionalEmail = MakeOptional<User, 'email'>;
// Result: { id: number; name: string; email?: string; }

type UserWithOptionalNameAndEmail = MakeOptional<User, 'name' | 'email'>;
// Result: { id: number; name?: string; email?: string; }

// Alternative implementation (more explicit):
type MakeOptional2<T, K extends keyof T> = {
  [P in keyof T]: P extends K ? T[P] | undefined : T[P];
};

// Real-world example - API update patterns:
interface UpdateUserRequest extends MakeOptional<User, 'id'> {
  // id is required, everything else optional for updates
}

const updateRequest: UpdateUserRequest = {
  id: 1,
  name: "Updated Name" // email is optional
};
```

---

## 🚀 Challenge 2: Generic Repository Pattern

Now let's tackle the Repository Pattern! This is a real-world pattern you'll use constantly:

```typescript
// Challenge 2: Generic Repository Pattern
interface Repository<T, TId> {
  findById(id: TId): Promise<T | null>;
  findAll(): Promise<T[]>;
  create(item: Omit<T, 'id'>): Promise<T>;
  update(id: TId, updates: Partial<T>): Promise<T | null>;
  delete(id: TId): Promise<boolean>;
  findWhere(predicate: (item: T) => boolean): Promise<T[]>;
}

// Entity types for testing
interface User {
  id: number;
  name: string;
  email: string;
  createdAt: Date;
}

interface Product {
  id: string;
  title: string;
  price: number;
  category: string;
}

// Your task: Implement this class
class InMemoryRepository<T extends { id: TId }, TId> implements Repository<T, TId> {
  private data: T[] = [];
  private nextNumericId = 1;

  // TODO: Implement all the interface methods
  // Hints:
  // - Use array methods like find, filter, map
  // - Handle ID generation for create method
  // - Remember to return Promises (use Promise.resolve())
  // - Use proper TypeScript types for all parameters and returns
}

// Should work like this:
const userRepo = new InMemoryRepository<User, number>();
const productRepo = new InMemoryRepository<Product, string>();

// Test your implementation:
const user = await userRepo.create({ 
  name: 'John', 
  email: 'john@example.com', 
  createdAt: new Date() 
});
console.log(user); // Should have auto-generated id

const foundUser = await userRepo.findById(user.id);
const allUsers = await userRepo.findAll();
```

### 💡 **Hints for Implementation:**

1. **For `create()` method**: You'll need to generate IDs based on the TId type
2. **For `findWhere()`**: Use array filter with the predicate function
3. **For `update()`**: Find the item, merge with updates, replace in array
4. **Type safety**: Make sure all methods return the correct Promise types

Give this a try! This pattern is used in almost every real application, so mastering it will be super valuable for your development work. 

Ready to implement it? 🛠️# TypeScript Generics Mastery Guide

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

---

## 🎯 Level 5: Advanced Generic Concepts

### Variance in Generics (Covariance & Contravariance)

```typescript
// Covariance - Generic types that "flow out" (return types)
interface Producer<T> {
  produce(): T;
}

// Contravariance - Generic types that "flow in" (parameter types)  
interface Consumer<T> {
  consume(item: T): void;
}

// Bivariance - Types that both flow in and out
interface Processor<T> {
  process(input: T): T;
}

// Real-world example
class EventHandler<TEvent> {
  private handlers: Array<(event: TEvent) => void> = [];
  
  // Contravariant - TEvent flows into the function
  addHandler(handler: (event: TEvent) => void): void {
    this.handlers.push(handler);
  }
  
  // Contravariant - TEvent flows into the emit function
  emit(event: TEvent): void {
    this.handlers.forEach(handler => handler(event));
  }
}

// Usage with inheritance
interface BaseEvent {
  timestamp: Date;
}

interface UserEvent extends BaseEvent {
  userId: number;
  action: string;
}

const userHandler = new EventHandler<UserEvent>();
const baseHandler = new EventHandler<BaseEvent>();

// This works due to contravariance
userHandler.addHandler((event: BaseEvent) => {
  console.log('Base event:', event.timestamp);
});
```

### Generic Type Inference and Helper Types

```typescript
// Type inference helpers
type InferArray<T> = T extends (infer U)[] ? U : never;
type InferPromise<T> = T extends Promise<infer U> ? U : never;
type InferFunction<T> = T extends (...args: any[]) => infer R ? R : never;

// Advanced inference - Extract nested types
type DeepReadonly<T> = {
  readonly [P in keyof T]: T[P] extends object ? DeepReadonly<T[P]> : T[P];
};

type FlattenArray<T> = T extends ReadonlyArray<infer U> 
  ? FlattenArray<U> 
  : T;

// Usage examples
type NestedArray = string[][][];
type Flattened = FlattenArray<NestedArray>; // string

interface Config {
  api: {
    baseUrl: string;
    timeout: number;
  };
  features: {
    auth: boolean;
  };
}

type ReadonlyConfig = DeepReadonly<Config>;
// All properties become readonly recursively
```

### Generic Factories and Builders

```typescript
// Generic Factory Pattern
interface Factory<T> {
  create(...args: any[]): T;
}

class UserFactory implements Factory<User> {
  create(name: string, email: string): User {
    return {
      id: Math.random(),
      name,
      email
    };
  }
}

// Generic Builder Pattern
class QueryBuilder<T> {
  private conditions: Array<(item: T) => boolean> = [];
  private sortKey?: keyof T;
  private sortDirection: 'asc' | 'desc' = 'asc';
  
  where(predicate: (item: T) => boolean): QueryBuilder<T> {
    this.conditions.push(predicate);
    return this; // Method chaining
  }
  
  orderBy<K extends keyof T>(key: K, direction: 'asc' | 'desc' = 'asc'): QueryBuilder<T> {
    this.sortKey = key;
    this.sortDirection = direction;
    return this;
  }
  
  execute(data: T[]): T[] {
    let result = data;
    
    // Apply filters
    this.conditions.forEach(condition => {
      result = result.filter(condition);
    });
    
    // Apply sorting
    if (this.sortKey) {
      result.sort((a, b) => {
        const aVal = a[this.sortKey!];
        const bVal = b[this.sortKey!];
        
        if (aVal < bVal) return this.sortDirection === 'asc' ? -1 : 1;
        if (aVal > bVal) return this.sortDirection === 'asc' ? 1 : -1;
        return 0;
      });
    }
    
    return result;
  }
}

// Usage
const users: User[] = [
  { id: 1, name: "John", email: "john@example.com" },
  { id: 2, name: "Jane", email: "jane@example.com" },
  { id: 3, name: "Bob", email: "bob@example.com" }
];

const result = new QueryBuilder<User>()
  .where(user => user.name.startsWith('J'))
  .orderBy('name', 'desc')
  .execute(users);
```

### Generic Decorators and Higher-Order Functions

```typescript
// Generic retry decorator
function withRetry<TArgs extends any[], TReturn>(
  fn: (...args: TArgs) => Promise<TReturn>,
  maxRetries: number = 3,
  delay: number = 1000
): (...args: TArgs) => Promise<TReturn> {
  return async (...args: TArgs): Promise<TReturn> => {
    let lastError: Error;
    
    for (let attempt = 1; attempt <= maxRetries; attempt++) {
      try {
        return await fn(...args);
      } catch (error) {
        lastError = error as Error;
        
        if (attempt === maxRetries) {
          throw lastError;
        }
        
        await new Promise(resolve => setTimeout(resolve, delay * attempt));
      }
    }
    
    throw lastError!;
  };
}

// Usage
async function fetchUser(id: number): Promise<User> {
  const response = await fetch(`/api/users/${id}`);
  if (!response.ok) throw new Error('Failed to fetch user');
  return response.json();
}

const fetchUserWithRetry = withRetry(fetchUser, 3, 500);

// Generic memoization
function memoize<TArgs extends any[], TReturn>(
  fn: (...args: TArgs) => TReturn,
  keyGenerator?: (...args: TArgs) => string
): (...args: TArgs) => TReturn {
  const cache = new Map<string, TReturn>();
  
  return (...args: TArgs): TReturn => {
    const key = keyGenerator ? keyGenerator(...args) : JSON.stringify(args);
    
    if (cache.has(key)) {
      return cache.get(key)!;
    }
    
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
}

// Usage
const expensiveCalculation = memoize((a: number, b: number): number => {
  console.log('Computing...'); // Only logs once per unique input
  return a * b * Math.random();
});
```

### Generic State Management

```typescript
// Generic Redux-style state management
type Action<TType extends string, TPayload = void> = TPayload extends void
  ? { type: TType }
  : { type: TType; payload: TPayload };

type ActionCreator<TType extends string, TPayload = void> = TPayload extends void
  ? () => Action<TType>
  : (payload: TPayload) => Action<TType, TPayload>;

// Create typed action creators
function createAction<TType extends string>(type: TType): ActionCreator<TType>;
function createAction<TType extends string, TPayload>(
  type: TType
): ActionCreator<TType, TPayload>;
function createAction<TType extends string, TPayload = void>(
  type: TType
): ActionCreator<TType, TPayload> {
  return ((payload?: TPayload) => 
    payload === undefined ? { type } : { type, payload }
  ) as ActionCreator<TType, TPayload>;
}

// Usage
const increment = createAction('INCREMENT');
const setUser = createAction<'SET_USER', User>('SET_USER');

// Type-safe actions
const incrementAction = increment(); // { type: 'INCREMENT' }
const setUserAction = setUser({ id: 1, name: 'John', email: 'john@example.com' });

// Generic reducer
type Reducer<TState, TAction> = (state: TState, action: TAction) => TState;

function createReducer<TState, TActions extends Action<string, any>>(
  initialState: TState,
  handlers: {
    [K in TActions['type']]?: (
      state: TState, 
      action: Extract<TActions, { type: K }>
    ) => TState;
  }
): Reducer<TState, TActions> {
  return (state = initialState, action) => {
    const handler = handlers[action.type];
    return handler ? handler(state, action as any) : state;
  };
}
```

### Generic API Client Pattern

```typescript
// Generic API client with type safety
interface ApiEndpoint {
  method: 'GET' | 'POST' | 'PUT' | 'DELETE';
  path: string;
}

interface ApiConfig {
  users: {
    list: { method: 'GET'; path: '/users' };
    create: { method: 'POST'; path: '/users' };
    update: { method: 'PUT'; path: '/users/:id' };
    delete: { method: 'DELETE'; path: '/users/:id' };
  };
  products: {
    list: { method: 'GET'; path: '/products' };
    create: { method: 'POST'; path: '/products' };
  };
}

type ApiResponse<T> = {
  data: T;
  status: number;
  message?: string;
};

class TypedApiClient<TConfig extends Record<string, Record<string, ApiEndpoint>>> {
  constructor(private baseUrl: string) {}
  
  async request<
    TResource extends keyof TConfig,
    TEndpoint extends keyof TConfig[TResource],
    TResponse = unknown,
    TPayload = unknown
  >(
    resource: TResource,
    endpoint: TEndpoint,
    options?: {
      params?: Record<string, string | number>;
      body?: TPayload;
    }
  ): Promise<ApiResponse<TResponse>> {
    const config = this.config[resource][endpoint];
    let url = `${this.baseUrl}${config.path}`;
    
    // Replace path parameters
    if (options?.params) {
      Object.entries(options.params).forEach(([key, value]) => {
        url = url.replace(`:${key}`, String(value));
      });
    }
    
    const response = await fetch(url, {
      method: config.method,
      headers: {
        'Content-Type': 'application/json',
      },
      body: options?.body ? JSON.stringify(options.body) : undefined,
    });
    
    const data = await response.json();
    return {
      data,
      status: response.status,
      message: data.message
    };
  }
  
  private config = {} as TConfig;
}

// Usage
const api = new TypedApiClient<ApiConfig>('https://api.example.com');

// Fully type-safe API calls
const users = await api.request('users', 'list'); // GET /users
const newUser = await api.request('users', 'create', { 
  body: { name: 'John', email: 'john@example.com' } 
});
const updatedUser = await api.request('users', 'update', {
  params: { id: 1 },
  body: { name: 'Jane' }
});
```

---

## 🎓 Advanced Concepts Quiz

Before we move to Challenge 2, test your understanding:

### Question 1: Type Inference
```typescript
function processData<T>(data: T[]): T extends string ? string[] : number[] {
  // What should the return type be?
}
```

### Question 2: Conditional Types
```typescript
type IsArray<T> = T extends any[] ? true : false;

type Test1 = IsArray<string[]>; // ?
type Test2 = IsArray<string>;   // ?
type Test3 = IsArray<number[]>; // ?
```

### Question 3: Mapped Types
```typescript
type MakeOptional<T, K extends keyof T> = ?; // How would you implement this?

// Should work like:
interface User {
  id: number;
  name: string;
  email: string;
}

type UserWithOptionalEmail = MakeOptional<User, 'email'>;
// Result: { id: number; name: string; email?: string; }
```

Want to tackle these quiz questions first, or should we explore more patterns like **Template Literal Types**, **Recursive Types**, or **Generic Constraints with keyof**? 

What interests you most? 🤔