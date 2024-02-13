class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [None for i in range(self.Max)]
        
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
        
t = HashTable()
t['January 4'] = 26
t['september 15'] = 47
t['June 17'] = 38

print(t.arr)
print(t['september 15'])
