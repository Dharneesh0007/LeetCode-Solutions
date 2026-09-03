class MyHashSet:

    def __init__(self):
        # Collisions koraika oru prime number size select panrom
        self.size = 1009
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        # Index calculate panna simple hash function
        return key % self.size

    def add(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]
        # Element bucket-la illana mattum append panrom (duplicates avoid panna)
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]
        # Element irundha mattum remove panrom
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        bucket = self.buckets[index]
        # Element irukka nu check panni boolean value return panrom
        return key in bucket