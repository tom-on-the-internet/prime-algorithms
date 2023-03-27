class Hashmap:
    length = 0

    def __init__(self) -> None:
        self.back_list = []
        for _ in range(10):
            self.back_list.append([])

    def set(self, key: str, value) -> None:
        hash_key = self.hash(key)
        for i, entry in enumerate(self.back_list[hash_key]):
            curr_key, _ = entry
            if curr_key == key:
                self.back_list[hash_key][i] = (key, value)
                return

        self.back_list[hash_key].append((key, value))
        self.length += 1

    def has(self, key: str) -> bool:
        hash_key = self.hash(key)
        for k, _ in self.back_list[hash_key]:
            if key == k:
                return True

        return False

    def get(self, key: str):
        hash_key = self.hash(key)
        for k, value in self.back_list[hash_key]:
            if key == k:
                return value

        return False

    def delete(self, key: str):
        hash_key = self.hash(key)
        for i, entry in enumerate(self.back_list[hash_key]):
            curr_key, _ = entry
            if curr_key == key:
                self.back_list = self.back_list[:i] + self.back_list[i + 1 :]
                self.length -= 1
            return

    # hash is a bad implementation of a hash function
    def hash(self, key: str) -> int:
        hash_sum = 0
        for char in key:
            hash_sum += ord(char)

        return hash_sum % 10


hm = Hashmap()

print(hm.length)
hm.set("dom", "tur")
print(hm.back_list)
hm.delete("dom")
print(hm.back_list)
print(hm.length)
print(hm.has("dom"))
print(hm.has("tom"))
print(hm.get("dom"))
hm.set("dom", "cur")
print(hm.get("dom"))
print(hm.has("dim"))
hm.set("dim", "cir")
print(hm.has("dim"))
print(hm.length)
print(hm.back_list)
