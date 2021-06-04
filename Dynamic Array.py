import ctypes
import sys
from pympler import asizeof

class DynamicArray:

    def getsize(self):
        try:
            return sys.getsizeof(self._A)
        except:
            return 0

    def ToString(self):
        try:
            for i in self._A:
                print(i," ")
        except:
            pass

    def getLength(self):
        return len(self._A)
    
    def __init__(self):
        """Boş array oluştur"""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def make_array(self, c):
        """c kapasiteli array döndür"""
        return (c * ctypes.py_object)()

    def append(self, obj):
        """array sonuna nesne ekle"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
        return self._A[k]

    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)

        for j in range(self.n, k, -1):
            self._A[j] = self._A[j-1]
        
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        for k in range(self._n):
            if self.A[k] == value:
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None
                self._n -= 1
            return
        raise ValueError("value not found")

def get_size(obj, seen=None):
        size = sys.getsizeof(obj)
        if seen is None:
            seen = set()
        obj_id = id(obj)
        if obj_id in seen:
            return 0
        # Important mark as seen *before* entering recursion to gracefully handle
        # self-referential objects
        seen.add(obj_id)
        if isinstance(obj, dict):
            size += sum([get_size(v, seen) for v in obj.values()])
            size += sum([get_size(k, seen) for k in obj.keys()])
        elif hasattr(obj, '__dict__'):
            size += get_size(obj.__dict__, seen)
        elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
            size += sum([get_size(i, seen) for i in obj])
        return size



c = DynamicArray()

s_1 = sys.getsizeof(c)
s_2 = asizeof.asizeof(c)

print("s_1 : {0}, s_2 : {1}".format(s_1, s_2))

get_size(c)

c.getLength(), c.getsize()

n = 10
for i in range(n):
    c.append(12)
    c.append("asdfqwe")

s_1 = sys.getsizeof(c)
s_2 = asizeof.asizeof(c)

print("n s_1 : {0}, s_2 : {1}".format(s_1, s_2))

for i in range(10):
    c.append(i)
    c.ToString()
print("len : {0}".format(c.getLength()))
print("size : {0}".format(c.getsize()))

