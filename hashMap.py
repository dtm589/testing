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
    
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)
        
    def get(self, key):
        index = self.key_to_index(key)
        if self.hashmap[index]:
            return self.hashmap[index][1]
        else:
            raise Exception("sorry, key not found")
        
    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap = [None]
        load = self.current_load()
        if load >= .05:
            new_hashmap = [None]*len(self.hashmap)*10
            temp_hashmap = self.hashmap
            self.hashmap = new_hashmap
            for bucket in temp_hashmap:
                if bucket != None:
                    self.insert(bucket[0], bucket[1])
                    
    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        buckets = 0
        for bucket in self.hashmap:
            if bucket != None:
                buckets += 1
        return buckets / len(self.hashmap)