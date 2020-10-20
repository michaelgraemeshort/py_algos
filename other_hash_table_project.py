# can't remember the objective, here
# something to do with putting the data from data.txt into a custom hash table
# then testing it by accessing two given keys?

class CustomHashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for i in range(self.size)]

    def set_val(self, key, value):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        already_in_bucket = False
        for index, item in enumerate(bucket):
            if item[0] == key:
                already_in_bucket = True
                bucket[index] = (key, value)
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


table = CustomHashTable(10)

with open("data.txt") as f:
    lines = f.readlines()

for line in lines:
    split_line = line.split(":")
    key = split_line[0]
    value = split_line[1][:-1]
    table.set_val(key, value)

# print(table)
print(table.get_val("mashrur@example.com"))
print(table.get_val("evgeny@example.com"))
print(table.get_val("wah"))
