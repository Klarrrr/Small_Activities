class HashTable :
    def __init__(self):
        self.collection = dict()

    def hash(self, string):

            if not isinstance(string, str):
                return "Key must be a string"
            return sum(ord(ch) for ch in string)
        
    def add(self, key, value):

            hash_value = self.hash(key)
            
            if hash_value not in self.collection:
                self.collection[hash_value] = {}
            self.collection[hash_value][key] = value
        
    def remove(self, key):
            hvalue = self.hash(key)
            
            if hvalue in self.collection:
                if key in self.collection[hvalue]:
                    del self.collection[hvalue][key]
            else:
                return "No keys match"

    def lookup(self,key):
            hvalue = self.hash(key)
            if hvalue in self.collection:
                if key in self.collection[hvalue]:
                    return self.collection[hvalue][key]
            else:
                return None

ht = HashTable()

  
ht.add("dear", "friend")
ht.add("read", "book")
ht.add("sfjsfji", "book")

print("Lookup 'dear':", ht.lookup("dear")) 
print("Lookup 'read':", ht.lookup("read"))

print("\nHash of 'dear':", ht.hash("dear"))
print("Hash of 'read':", ht.hash("read"))
print("Hash of 'read':", ht.hash("sfjsfji"))

ht.remove("read")
print("Lookup 'read' after removal:", ht.lookup("read")) 
print("Removing 'unknown' returns:", ht.remove("unknown")) 

for hval, inner in ht.collection.items():
    print(f"  {hval}: {inner}")