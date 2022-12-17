//+===================================================================
// File lab_2.cpp
// Линейная логическая программа
// Вариант 5
// Эта программа вычисляет три логические функции
//
// F1(x3,x2,x1,x0)=(4 5 6 7 8 9 10)
// F2(x3,x2,x1,x0)=(7 8 9 10 11 12)
// F3(x3,x2,x1,x0)=(3 4 5 6 7)
//
// (C) Литвиненко А.В., 2022
//-===================================================================

#include <stdio.h>
#include <iostream>
#include <iomanip>
using namespace std;

bool
	x3, x2, x1, x0,
	f1, f2, f3,
	f1_a, f2_a, f3_a;

int main() {
	printf("\n\t\t(C) Lytvynenko Andrii, 2022");
	printf("\n\tGetting the values of the logic functions:");
	printf("\n\tF1(x3,x2,x1,x0)=4 5 6 7 8 9 10");
	printf("\n\tF2(x3,x2,x1,x0)=7 8 9 10 11 12");
	printf("\n\tF3(x3,x2,x1,x0)=3 4 5 6 7");

	while(true) {
	
		printf("\nEnter x3,x2,x1,x0: ");
		cin >> x3 >> x2 >> x1 >> x0;

		/*
			F1 = (x0 & !x1 & !x2) v (x0 & !x1 &!x3 ) v (!x0 & x1)
			F2 = (!x0 & x1 & x2 & x3) v (x0 & !x2 & !x3) v (x0 & !x1)
			F3 = (!x0 & x2 & x3) v (!x0 & x1)
		*/

		// C
		f1 = (x0 && !x1 && !x2) || (x0 && !x1 && !x3) || (!x0 && x1);
		f2 = (!x0 && x1 && x2 && x3) || (x0 && !x2 && !x3) || (x0 && !x1);
		f3 = (!x0 && x2 && x3) || (!x0 && x1);

		// ASM
		__asm {

			// F1
			// (x0 && !x1 && !x2) || (x0 && !x1 && !x3) || (!x0 && x1)
			mov al,x1
			not al
			and al, 1
			mov ah,x2
			not ah
			and ah, 1
			and al,ah
			and al,x0

			mov bl,x1
			not bl
			and bl, 1
			mov ah,x3
			not ah
			and ah, 1
			and bl,ah
			and bl,x0

			or al,bl

			mov bl,x0
			not bl
			and bl, 1
			and bl,x1

			or al,bl
			and al,1
			mov f1_a,al
		}

		__asm {
			// F2
			// (!x0 && x1 && x2 && x3) || (x0 && !x2 && !x3) || (x0 && !x1)
			mov al,x0
			not al
			and al, 1
			and al,x1
			and al,x2
			and al,x3

			mov ah,x2
			not ah
			and ah, 1
			mov bl,x3
			not bl
			and bl, 1
			and ah,bl
			and ah,x0

			or al,ah

			mov ah,x1
			not ah
			and ah, 1
			and ah,x0

			or al,ah
			and al, 1
			mov f2_a,al
		}

		__asm {
			// F3
			// (!x0 & x2 & x3) v (!x0 & x1)

			mov al,x0
			not al
			and al, 1
			and al,x2
			and al,x3

			mov ah,x0
			not ah
			and al, 1
			and ah,x1

			or al,ah
			and al, 1
			mov f3_a,al
		}

		printf("[C] F1 = %d, F2 = %d, F3 = %d\n", f1, f2, f3);
		printf("[ASM] F1 = %d, F2 = %d, F3 = %d\n", f1_a, f2_a, f3_a);

	}

}