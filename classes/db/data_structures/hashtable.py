from .arr import arr
from .sll import sll

class hashtable:
    def __init__(self, size: int = 23):
        self.size = size
        self.arr = arr(size)
        self.exp_factor = 0.73
        self.shrink_factor = 0.3141
        self.occupied = 0

    def insert(self, key, value):
        if self.occupied/self.size >= self.exp_factor:
            self._expand()

        new_key_value = key_value(key, value)

        idx: int = self._hash(key)
        existing_idx = self._quadratic_probing(idx, key)

        if existing_idx is not None:
            # key already exists
            return False
        
        insert_idx = self._quadratic_probing(idx)
        
        if insert_idx is None:

            # no suitable index was found
            self._expand()
            self.insert(key, value)
        else:            
            self.arr.insert(insert_idx, new_key_value)
            self.occupied += 1

        return True

    def get(self, key):
        idx = self._hash(key)
        idx = self._quadratic_probing(idx, key)

        if idx is None:
            return None

        pair: key_value = self.arr.get(idx)
        if pair: return pair.value
    
    def delete(self, key):
        idx = self._hash(key)
        idx = self._quadratic_probing(idx, key)

        if idx is None:
            return False

        self.arr.insert(idx, "x")
        self.occupied -= 1
        return True
    
    def get_all(self)->sll:
        all = sll()
        
        for i in range(self.arr.size):
            pair:key_value = self.arr.get(i)
            
            if pair and pair != 'x':
                all.add_first(pair.value)
        
        return all

    def _hash(self, key):
        key = str(key)
        hash = 127
        
        for c in key:
            hash += ord(c)
        
        return hash % self.size

    def _quadratic_probing(self, idx, key = None, array = None):
        if array is None:
            array = self.arr

        # return found item index if key is provided
        if key:
            for i in range(self.size):
                probe_idx = (idx + i**2) % array.size
                pair: key_value = array.get(probe_idx)

                if pair and pair != "x":
                    if pair.key == key:
                        return probe_idx
                    
                elif not pair: return None
        
        # return insertion index if key isn't provided
        else:
            for i in range(self.size):
                probe_idx = (idx + i**2) % array.size
                pair: key_value = array.get(probe_idx)

                if not pair or pair == "x":
                    return probe_idx

        return None

    def _expand(self):
        
        self.size = int(self.size * 2.763)
        self.occupied = 0

        old_arr = self.arr
        new_arr = arr(self.size)

        for i in range(old_arr.size):
            old_pair: key_value = old_arr.get(i)
            
            if old_pair and old_pair != 'x':
                new_pair = key_value(old_pair.key, old_pair.value)
                idx = self._hash(old_pair.key)
                
                if new_arr.get(idx):
                    idx = self._quadratic_probing(idx, array = new_arr)

                new_arr.insert(idx, new_pair)
                self.occupied += 1

        self.arr = new_arr
        del old_arr
    
    def _shrink(self):

        self.size = int(self.size / 2.763)
        self.occupied = 0

        old_arr = self.arr
        new_arr = arr(self.size)

        for i in range(old_arr.size):
            old_pair: key_value = old_arr.get(i)
            
            if old_pair and old_pair != 'x':
                new_pair = key_value(old_pair.key, old_pair.value)
                idx = self._hash(old_pair.key)
                
                if new_arr.get(idx):
                    idx = self._quadratic_probing(idx, array = new_arr)

                new_arr.insert(idx, new_pair)
                self.occupied += 1
                
        self.arr = new_arr
        del old_arr
    
    def __repr__(self):
        return f"{self.arr}"

class key_value:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"{self.key} : {self.value}"