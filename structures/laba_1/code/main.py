from time import time
from random import randint
from tkinter import W
from types import NotImplementedType

class Main:
    def __init__(self) -> None:
        self._array = []

    @staticmethod
    def genArray(_array: list, 
            start: int = 0, end: int = 10, step:int = 1, 
            startNum:int = 0, endNum:int = 100, orderby:int=0) -> list:
        _array = []
        for i in range(start, end, step):
            _array.append(randint(startNum, endNum))
        
        if orderby == -1:
            _array = _array.sort(reverse=True)
        elif orderby == 1:
            _array = _array.sort(reverse=False)
        else:
            pass

        return _array


    @property
    def array(self) -> None:
        for i in range(len(self._array)):
            print(self._array[i], end=" ")
 
    @array.setter
    def setArray(self, arr: list) -> None:
        self._array = arr.copy()
    

    @staticmethod
    def buble_sort(_array: list) -> list:
        array = _array.copy()
        size = len(array)
        flag = size < 15
        compare_count = 0
        exchange_count = 0
        start_time = time()

        for i in range(size-1):
            if flag:
                print(f"[{i}] {array}")
            for j in range(0, size-i-1):
                if array[j] > array[j + 1]:
                    if flag:
                        print(f"\tExchanging {array[j]} <> {array[j+1]} ({j}, {j+1})")
                    array[j], array[j + 1] = array[j + 1], array[j]
                    exchange_count += 1
                compare_count += 1
        print("\t[?] Compares count: %d" % compare_count)
        print("\t[?] Exchange count: %d" % exchange_count)
        print(f"\t[?] Exchanges to compares count: {round(exchange_count / compare_count * 100)}%")
        print("\t--- %.5s seconds ---" % (time()-start_time))

        return array

    @staticmethod
    def selection_sort(_array: list) -> list:
        array = _array.copy()
        size = len(array)
        flag = size < 15
        compare_count = 0
        exchange_count = 0

        start_time = time()
        for ind in range(size):
            if flag:
                print(f"[{ind}] {array}")
            min_index = ind
            for j in range(ind + 1, size):
                if array[j] < array[min_index]:
                    min_index = j
                compare_count += 1
            if flag:
                print(f"\tMin index: {min_index}")
                print(f"\tExchanging {array[ind]} <> {array[min_index]} ({ind} <> {min_index})")
            (array[ind], array[min_index]) = (array[min_index], array[ind])
            exchange_count += 1

        print("\t[?] Compares count: %d" % compare_count)
        print("\t[?] Exchange count: %d" % exchange_count)
        print(f"\t[?] Exchanges to compares count: {round(exchange_count / compare_count * 100)}%")
        print("\t--- %.5s seconds ---" % (time()-start_time))

        return array
    

def Menu():
    print("""
    - 0. Show menu
    - 1. Set  array
    - 2. Show array
    - 3. Gen  array
    - 4. Buble sort
    - 5. Selection sort
    - 6. Exit
    """)
   
    
def main():
    op = 0
    arr = Main()
    arr = [1,2,7,4,0,0,0,3,5,7,2]
    while True:
        match op:
            case 0:
                Menu()
            case 1:
                arr = list(map(int, input("Enter array by space: ").split(" ")))
            case 2:
                print(arr)
            case 3:
                start = int(input("Enter start: "))
                end = int(input("Enter end: "))
                step = int(input("Enter step: "))
                startNum = int(input("Enter start number: "))
                endNum = int(input("Enter end number: "))
                orderBy = int(input("Enter order by (-1 - descending, 1 - ascending): "))
                arr = Main.genArray(arr,start,end,step,startNum,endNum,orderBy)

                print("\nResult: ", arr)
            case 4:
                print("Bubble sort")
                print("\nResult: ", Main.buble_sort(arr))
            case 5:
                print("Selection sort")
                print("\nResult: ", Main.selection_sort(arr))
            case 6:
                print("Exiting...")
                break
            case _:
                print("Invalid operation")
        op = int(input("\nEnter operation: "))


if __name__ == "__main__":
    main()
    print("Program finished")
