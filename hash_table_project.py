# hash table implementation - if Python didn't have dictionaries...

class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for i in range(self.size)]

    def create_buckets(self):
        pass

    def set_val(self, key, value):
        hashed_key = hash(key) % self.size  # returns a value between 0 and self.size
        bucket = self.hash_table[hashed_key]  # so this doesn't cause an IndexError
        already_in_bucket = False  # remains False in case of no collisions
        for index, item in enumerate(bucket):  # checking for collisions...
            if item[0] == key:
                already_in_bucket = True
                bucket[index] = (key, value)  # updates the bucket at the correct index
                break
        if not already_in_bucket:
            bucket.append((key, value))

    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        for item in bucket:
            item_key, item_value = item[0], item[1]
            if item_key == key:
                return item_value
        return "nope"

    def __str__(self):
        return " ".join(str(bucket) for bucket in self.hash_table)


hash_table = HashTable(4)
print(hash_table)
hash_table.set_val("what", "the")
print(hash_table)
hash_table.set_val("what", "eggs")
print(hash_table)
hash_table.set_val("spam", "spem")
print(hash_table)
print(hash_table.get_val("what"))
print(hash_table.get_val("spam"))