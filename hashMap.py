class HashMap:
    def key_to_index(self, key):
        unicode = 0
        for character in key:
            unicode += ord(character)
        index = unicode % len(self.hashmap)
        return index
        

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)