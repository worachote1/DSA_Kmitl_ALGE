/**
 *
 * Challenge 2: Generic Repository Pattern
 * Create a generic repository interface for CRUD operations.
 *
 *
 *
 * 💡 Key Learning Points for Challenge 2:
 * Generic Constraints: T extends { id: TId } ensures T has an id property
 * Interface Implementation: All methods must match the interface exactly
 * ID Handling: Different strategies for number vs string IDs
 * Promise Wrapping: Converting sync operations to async
 */

interface Repository<T, TId> {
  // TODO: Define methods for CRUD operations
  // - findById(id: TId): Promise<T | null>
  // - findAll(): Promise<T[]>
  // - create(item: Omit<T, 'id'>): Promise<T>
  // - update(id: TId, updates: Partial<T>): Promise<T | null>
  // - delete(id: TId): Promise<boolean>
}

// Should work with different entity types
interface User {
  id: number;
  name: string;
  email: string;
}

interface Product {
  id: string;
  title: string;
  price: number;
}

// Implementation challenge
class InMemoryRepository<T extends { id: TId }, TId>
  implements Repository<T, TId>
{
  // TODO: Implement this

  private repository: T[] = [];

  public async findById(id: TId): Promise<T | null> {
    const item = this.repository.find((repo) => repo.id === id);
    return item ?? null; // if undefined, return null
  }

  public async findAll(): Promise<T[]> {
    return this.repository;
  }

  public async create(item: Omit<T, "id">): Promise<T> {
    let newId: TId;

    const lastItem = this.repository.at(-1);

    if (!lastItem) {
      // Default id if empty array
      // number -> 1, string -> generate UUID
      newId = (typeof (0 as TId) === "number" ? 1 : crypto.randomUUID()) as TId;
    } else {
      const lastId = lastItem.id;

      if (typeof lastId === "number") {
        // Increment last number id
        newId = ((lastId as number) + 1) as TId;
      } else {
         // TId is string type (or other)
        // Generate new string id (UUID)
        newId = crypto.randomUUID() as TId;
      }
    }

    const newItem = { ...item, id: newId } as T;
    this.repository.push(newItem)
    return newItem;
  }

  public async update(id: TId, updates: Partial<T>): Promise<T | null> {
    const targetItemIdx = this.repository.findIndex((item) => item.id === id);

    if (targetItemIdx === -1) {
      return null;
    }

    this.repository[targetItemIdx] = {
      ...this.repository[targetItemIdx],
      ...updates,
    };

    return this.repository[targetItemIdx];
  }

  public async delete(id: TId): Promise<boolean> {
    const targetItemIdx = this.repository.findIndex((item) => item.id === id);

    if (targetItemIdx === -1) {
      return false; // not found
    }

    this.repository.splice(targetItemIdx, 1); // remove the item
    return true; // deleted successfully
  }
}
