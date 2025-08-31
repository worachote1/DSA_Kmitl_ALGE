/**
 *
 * Challenge 1: Generic Cache
 * Create a generic cache class that can store any type of data with string keys.
 *
 */

interface User {
  id: number;
  name: string;
  email: string;
}

class Cache1<T> {
  // TODO: Create a cache that can:
  // 1. Store values with string keys
  // 2. Get values (return T | undefined if not found)
  // 3. Check if key exists
  // 4. Clear all data
  // 5. Get all keys

  private cacheData: Record<string, T> | {} = {};

  public set(key: string, value: T): void {
    this.cacheData[key] = value;
  }

  public get(key: string): T | undefined {
    return this.cacheData[key];
  }

  public has(key: string): boolean {
    return key in this.cacheData;
  }

  public delete(key: string): boolean {
    if (!(key in this.cacheData)) {
      return false;
    }
    delete this.cacheData[key];
    return true;
  }

  public clear(): void {
    this.cacheData = {};
  }

  public keys(): string[] {
    return Object.keys(this.cacheData);
  }
}

// Should work like this:
const userCache = new Cache1();
userCache.set("user1", { id: 1, name: "John", email: "john@example.com" });
const user = userCache.get("user1"); // User | undefined
