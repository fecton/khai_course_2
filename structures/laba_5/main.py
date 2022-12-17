import math
from pprint import pprint
# File: main.py
# Author: Lytvynenko Andrii 525a
# Date: 27.11.2022

# Інтерва розподілу чисел [A,B]
Interval = [0,1000]
# Розмірність таблиці    
N = 83

# Рівномірно розподілені числа
Table1_Array = [23, 20, 90, 25, 60, 99, 1, 90, 25, 29]

# Для методу лінійних проб
N1 = 5 + 2*(5%2+1) # 9
# Для квадратичних проб
N2 = 5 + 3*(5%2+1) # 11
# Метод подвійного хешування
N3 = 5 + 4*(5%2+1) # 13
L = N3 - 3

# N1 = S+K(S % 2 + 1)
# N1 - номер першого ключа последовательности
# S - номер по списку
# K - порядковий номер метода відкритої адресації для дозволу колізії в табл 2

# Варіанти методів відкритої адресації
# 2) метод лінійниз проб (H.i = (H.i-1 + c) % N)
# 3) метод квадратичних проб
# 4) метод подвійного хешування

"""
Значенняя з презентації
Table1_Array = [1,0,13,26,39]
N = 13
c = 2
"""

def H(k: int) -> int:
    return k % N

def H1(k: int) -> int:
    return k % L

def print_decorator(text, func):
    print(text)
    func()
    print()

class Program:
    @classmethod
    def task_2():
        # 2) метод лінійниз проб (H.i = (H.i-1 + c) % N)
        """
        H0 = H(k)

        Hi = (H0 + i) % N, i = [1, ..., N-1]
            OR
        Hi = (H(i-1) + c) % N

        c - константа, така що c та N взаємно прості
        i - індекс повторного хешування
        """

        N = N1
        O_list = []
        kolizion = []
        d = {}

        tlength = int(math.sqrt(max(Table1_Array)))+2

        i = 0
        for k in range(tlength):
            d[i] = 0
            i += 1

        # Вставка
        for k in Table1_Array:
            hX = H(k)
            count = 1
            while hX in kolizion:
                hX = H(hX) + 2
                count += 1
                if count > tlength:
                    break

            kolizion.append(hX)
            d[hX] = k
            O_list.append(count)


        print("H = ", kolizion)
        print("O = ", O_list)

        pprint(d)
        print("Si = ", sum(O_list) / len(O_list))
        print("Alpha = ", round(len(O_list)/N, 4))

        # Пошук
        Oi = O_list
        print("Sf = ", sum(Oi) / len(Oi))

    @classmethod
    def task_3():
        # 3) метод квадратичних проб
        """
        H0 = H(k)
        
        Hi = (H0 + i**2) % N, i > 0
            OR
        Hi = (H0 + c1*i + c2*i) % N

        i - індекс повторного хешування
        """
        N = N2
        O_list = []
        kolizion = []
        d = {}

        i = 0
        for k in range(int(math.sqrt(max(Table1_Array)))+3):
            d[i] = 0
            i += 1

        # Вставка
        I = 1
        for k in Table1_Array:
            hX = H(k)
            count = 1
            while hX in kolizion:
                hX = (H(hX) + 1 ** 2) % N
                count += 1

            kolizion.append(hX)
            d[hX] = k
            O_list.append(count)

        print("H = ", sorted(kolizion))
        print("O = ", O_list)

        # print(d)
        pprint(d)

        print("Si = ", sum(O_list) / len(O_list))
        print("Alpha = ", round(len(O_list)/N, 4))

        # Пошук
        Oi = O_list
        print("Sf = ", sum(Oi) / len(Oi))
        
    @classmethod
    def task_4():
        """
        Використовується 2 функції:
            H(k)  = q(k) % N - исходня хеш-функція
            H1(k) = q(k) % L - додаткова хеш фукнція
                N та L вибираються взаємно простими

        Метод подвійного хешування:
            H0 = H(k) = q(k) % N
            Hi = ( H(k) + i*H1(k) ) % N, i>0
            i - індекс повторного хешування
        """
        # 4) метод подвійного хешування
        N = N3

        # example data
        O_list = []
        kolizion = []
        d = {}

        i = 0
        for k in range(int(math.sqrt(max(Table1_Array)))+3):
            d[i] = 0
            i += 1

        # Вставка
        I = 1
        kol_repeat = False
        for k in Table1_Array:
            hX = H(k)
            count = 1
            while hX in kolizion:
                if H(hX) not in kolizion:
                    hX = H(hX)
                else:
                    hX = (H(k) + I*H1(k)) % N
                    count += 1
                    I += 1
                if hX in kolizion:
                    kol_repeat = True
                    break

            if not kol_repeat:
                kolizion.append(hX)
                d[hX] = k
                O_list.append(count)
                kol_repeat = False


        print("H = ", sorted(kolizion))
        print("O = ", O_list)

        # print(d)
        pprint(d)

        print("Si = ", sum(O_list) / len(O_list))
        print("Alpha = ", round(len(O_list)/N, 4))

        # Пошук
        Oi = O_list
        print("Sf = ", sum(Oi) / len(Oi))

print_decorator("Task 2", Program.task_2)
print_decorator("Task 3", Program.task_3)
print_decorator("Task 4", Program.task_4)


