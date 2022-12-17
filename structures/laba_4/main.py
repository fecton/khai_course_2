import time
from random import randint

class Array:
    def __init__(self, arr: list):
        self._array = arr.copy()

    @property
    def array(self):
        return self._array

    @array.setter
    def array(self, value):
        self._array = value.copy()

    def __len__(self):
        return len(self._array)

    def __getitem__(self, index):
        return self._array[index]

    def show(self) -> None:
        for i in self.array:
            print('%d ' % i, end='')
        print()

    def generate(self, length: int) -> None:
        MIN, MAX = 0, 1000
        new = []
        for i in range(length):
            new.append(randint(MIN,MAX))
        self.array = new

    def binary_search(self, x: int) -> int:
        # array must be sorted!
        op_count = 0
        
        arr = sorted(self.array)
        low = 0
        high = len(arr) - 1
        mid = 0
        while low <= high:
            op_count += 1
            mid = (high + low) // 2
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                print(op_count)
                return 1
        print(op_count)
        return 0 

    def m_block_search(self, x: int, block_size: int = 1) -> int:
        # array must be sorted!
        op_count = 0
        
        arr = sorted(self.array)
        i = len(arr) - 1 
        j = 0
        s = 0
        b = []
        while 1:
            op_count += 1
            
            b.append(block_size)
            s += b[j]
            if(s >= i): break
        j = 0
        k = b[j] - 1
        j += 1
        while(arr[k] < x and k <= i):
            op_count += 1
            # print(j, b[j])
            k += b[j]
            j += 1
        if(k > j):
            print(op_count)
            return -1
        z = k - b[j - 1]
        while(z <= k):
            op_count += 1
            z += 1
            if(arr[z] == x):
                print(op_count)
                return 1
        print(op_count)
        return -1

    def built_in_search(self, x: int) -> int:
        print('[INFO] OPERATION COUNT CAN\'NT BE DEFINED!')
        try:
            a = self.array.index(x)
            a = 1
        except ValueError:
            a = 0
        return a

def runtime_decorator(func, blocksize: int = 1):
    arg = int(input('[VALUE] >> '))

    start_time = time.time()

    if func is Array.m_block_search:
        result = func(arg, blocksize)
    else:
        result = func(arg)

    if result in [0, -1]:
        print("Not found")
    else:
        print("Found")

    end_time = time.time()

    print('Runtime: ', round(end_time - start_time, 5))
    

def menu() -> None:
    a = """Menu:
    - 0. Show this menu
    - 1. Enter an array
    - 2. Generate an array
    - 3. # Binary search
    - 4. # M-block search
    - 5. # Build-in search
    - 6. Show
    - 7. Show random element and its position (faster)
    - 8. Exit"""
    print(a)

op = 0
arr = Array([])
while 1:
    match op:
        case 0:
            menu()
        case 1:
            t = map(int, input("[ARR] >> ").split(" "))
            arr = list(t)
            print('[OK]')
        case 2:
            l = int(input('[LEN] >> '))
            arr.generate(l)
            print('[OK]')
        case 3:
            runtime_decorator(arr.binary_search)
        case 4:
            m = input('[Block size] >> ')
            runtime_decorator(arr.m_block_search, m)
        case 5:
            runtime_decorator(arr.built_in_search)
        case 6:
            arr.show()
            print('[OK]')
        case 7:
            r = randint(0, len(arr)-1)
            print(r)
            print(f'Element: {arr[r]}\nIndex: {r}')
        case 8:
            print("[OK] Exiting...")
            exit()
        # Else
        case _:
            print("[ERR] An invalid operation!")
    op = int(input('>> ')) 

