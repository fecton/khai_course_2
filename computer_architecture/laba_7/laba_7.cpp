/*
* File: laba_7.cpp
* Долги - в начало. Задан числовой массив А[1..M]. Перенести все положительные
элементы в
* начало массива, а в остальном – порядок расположения элементов меняться не должен.
*
* (C) Lytvynenko A.V., 2022
*/
#include <iostream>
#include <iomanip>
using namespace std;
#define MAX_LENGTH 1024
long arr_c[1024] = { 0, };
long arr_asm[1024] = { 0, };
void show(long arr[], long n) {
	/// <summary>
	/// Виводить масив елементів через пробіл
	/// </summary>
	/// <param name="arr">Масив елементів</param>
	/// <param name="n">Довжина масиву</param>
	for (int i = 0;i < n;i++) {
		printf("%ld ", arr[i]);
	}
	printf("\n");
}
void equal(long arr1[], long arr2[], long n) {
	/// <summary>
	/// Прирівнює перший масив до другого. Масив2 = Масив1
	/// </summary>
	/// <param name="arr1">Масив 1</param>
	/// <param name="arr2">Масив 2</param>
	/// <param name="n">Довжина масиву</param>
	for (int i = 0;i < n;i++) {
		arr2[i] = arr1[i];
	}
}
void zeros(long arr[], long n) {
	/// <summary>
	/// Обнуляє повністю масив
	/// </summary>
	/// <param name="arr">Масив</param>
	/// <param name="n">Кількість елементів</param>
	for (int i = 0;i < n;i++) {
		arr[i] = 0;
	}
}
int main() {
	// Довжина масиву
	long n;
	// Індекс для встановлення наступного позитивного числа (можливий індекс)
	long allowed_index = 0;
	// Тимчасово змінна
	long tmp;
	// Ітераторний індекс
	long i;
	// Файловий вказівник
	FILE* file;
	// Якщо не вдається відкрити файл - завершення програми
	if ((file = fopen("in.txt", "r")) == NULL) {
		printf("[ERR] Can't open file!\n");
		return 1;
	}
	int j = 0;
	while (j < 10) {
		fscanf(file, "%ld\n", &n);
		if (n <= 0 || n > MAX_LENGTH) {
			printf("[ERR] Invalid paramaters!\n\n");
			j++;
			continue;
		}
		zeros(arr_c, n);
		zeros(arr_asm, n);
		allowed_index = 0;
		for (i = 0;i < n;i++) {
			fscanf(file, "%ld", &arr_c[i]);
		}
		equal(arr_c, arr_asm, n);
		// Виведення масивів до операцій
		printf("[BEFORE] [C] :\t\t");
		show(arr_c, n);
		printf("[BEFORE] [ASM] :\t");
		show(arr_asm, n);
		// Частина на Сі
		for (i = 0;i < n;i++) {
			// Якщо число позитивне, то обмінятися з числом на можливому індексі
				if (arr_c[i] > 0) {
					tmp = arr_c[allowed_index];
					arr_c[allowed_index] = arr_c[i];
					arr_c[i] = tmp;
					allowed_index++;
				}
		}
		/*
		eax - allowed_index
		ecx - arr_asm[eax]
		edx - arr_asm[esi]
		ebx - tmp
		esp
		ebp
		esi - I
		edi
		*/
			// Частина на асемблері
			__asm {
			// for(i = 0;i < n;i++)
			mov esi, 0 // i
			mov eax, 0 // allowed_index
			For1:
			cmp esi, n
				jge EndFor1
				cmp arr_asm[esi * 4], 0
				jg Exchange
				jmp Go
				Exchange :
			mov ebx, arr_asm[eax * 4]
				mov edx, arr_asm[esi * 4]
				mov arr_asm[eax * 4], edx
				mov arr_asm[esi * 4], ebx
				inc eax
				jmp Go
				Go :
			inc esi
				jmp For1
				EndFor1 :
		}
		// Виведення масивів після виконання операцій
		printf("[AFTER] [C] :\t\t");
		show(arr_c, n);
		printf("[AFTER] [ASM] :\t\t");
		show(arr_asm, n);
		printf("\n");
		j++;
	}

	scanf("%ld", &n);
	return 0;
}