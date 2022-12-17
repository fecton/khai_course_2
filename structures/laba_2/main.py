# VARIANT: 5
# Сортування підрахунком
# Порозрядне сортування - LSD
# [0, 500] 1,2

from random import randint
from time import time

def genArray(array: list, 
        start: int = 0, end: int = 10, step:int = 1, 
        startNum:int = 0, endNum:int = 500) -> list:
    array = []
    for i in range(start, end, step):
        array.append(randint(startNum, endNum))
    
    return array

def countingSort(arr) -> list:
    """
    Версія сортування вибором для звичайного використання
    """
    print("[INFO] Counting sort starts...")
    op_count = 0
    maxx = max(arr) + 1
    # Визначення розмірності масиву і створення пустої копії
    size = len(arr)
    output = [0] * size

    # Ініціалізувати пустий массив для підрахунків
    count = [0] * 501
    print("[Count] ", count[:maxx])

    # Додавання кількості кожного елементу
    for m in range(0, size):
        op_count += 1
        count[arr[m]] += 1
    print("[Initialized count] ", count[:maxx])

    # Встановлення комулятивної кількості
    for m in range(1, 10):
        op_count += 1
        count[m] += count[m - 1]
    print("[Comulative count] ", count[:maxx])

    # Встановлення елементів в вихідний масив після пошуку індексу до кожного елемента оригінального масива в підрахунках
    m = size - 1
    while m >= 0:
        op_count += 1
        output[count[arr[m]] - 1] = arr[m]
        count[arr[m]] -= 1
        m -= 1
        print("[PROCESSING ARRAY] ", output, count[:maxx])

    # Перезапис існуючого масиву на відсортований
    for m in range(0, size):
        arr[m] = output[m] 
    
    print("[INFO] Counting sort finished! The result: ", arr, end="\n"*2)
    print("[INFO] Operation count: ", op_count)
    return arr

def countingSortForRadix(inputArray, placeValue):
    """
    Сортування вибором для сортування LSD
    """
    countArray = [0] * 10
    inputSize = len(inputArray)

    for i in range(inputSize): 
        placeElement = (inputArray[i] // placeValue) % 10
        countArray[placeElement] += 1

    for i in range(1, 10):
        countArray[i] += countArray[i-1]

    outputArray = [0] * inputSize
    i = inputSize - 1
    while i >= 0:
        currentEl = inputArray[i]
        placeElement = (inputArray[i] // placeValue) % 10
        countArray[placeElement] -= 1
        newPosition = countArray[placeElement]
        outputArray[newPosition] = currentEl
        i -= 1
        
    return outputArray

def radixSort(inputArray: list) -> list:
    op_count = 0
    # Знаходження максимального елементу у введенному масиві
    maxEl = max(inputArray)
    print("[INFO] Max element: ", maxEl)

    # Знайти число серед цифр яке буде найбільшим
    D = 1
    while maxEl > 0:
        op_count += 1
        maxEl /= 10
        D += 1
    print("[INFO] Max number: ", maxEl)


    # Ініціалізувати місце для значення
    placeVal = 1

    # Виконання сортування
    outputArray = inputArray
    print("D\tArray")
    while D > 0:
        op_count += 1
        print(D, outputArray)
        outputArray = countingSortForRadix(outputArray, placeVal)
        placeVal *= 10  
        D -= 1

    print("[INFO] The result is ", outputArray)
    print("[INFO] Operation count: ", op_count)
    return outputArray 


def Menu() -> None:
    print("""
    - 0. Show menu
    - 1. Set  array
    - 2. Show array
    - 3. Gen  array
    - 4. Counting sort
    - 5. LSD sort
    - 6. Exit
    """)
   
    
def main():
    op = 0
    arr = [] 
    while True:
        if not arr and op in [4,5]:
            print("You forget to enter the array")
            op = 0
        match op:
            case 0:
                Menu()
            case 1:
                arr = list(map(int, input("Enter array by space: ").split(" ")))
            case 2:
                print(arr)
            case 3:
                start = 0
                end = int(input("How many elements?: "))
                step = 1
                startNum = 0
                endNum = 500
                # startNum = int(input("Min number: "))
                # endNum = int(input("Max number: "))
                arr = genArray(arr,start,end,step,startNum,endNum)

                print("\nResult: ", arr)
            case 4:
                start_time = time()
                print("Counting sort")
                countingSort(arr)
                print("Time: ", time() - start_time)
            case 5:
                start_time = time()
                print("LSD sort")
                radixSort(arr)
                print("Time: ", time() - start_time)
            case 6:
                print("Exiting...")
                break
            case _:
                print("Invalid operation")
        op = int(input("\nEnter operation: "))


if __name__ == "__main__":
    main()
    print("Program finished")
