#include <iostream>
#include <iomanip>

using namespace std;

unsigned long	x, W, W_a;
signed long		y, Q, Q_a;

// VARIANT: 5
#define a 55
#define b  8

void line() {
	printf("=====================\n");
}

// 55 = 32 + 16 + 4 + 2 + 1 = 2**5 + 2**4 + 2**2 + 2**1 + 2**0
// 8 = 8 = 2**3

int main()
{


	printf("<Separate to power of two>\n\ta = 55 = 32 + 16 + 4 + 2 + 1 = 2**5 + 2**4 + 2**2 + 2**1 + 2**0\n");
	printf("\tb = 8 = 8 = 2**3\n");
	printf("\nFormulas:\n\tW = x * a/b - unsigned number\n\tQ = y * a/b - signed number in additional code\n");
	line();
	printf("Infinity loop begins!\n");

	while (1) {
		printf("Enter x,y: ");
		scanf("%u%u", &x, &y);
		line();
		printf("You entered:\n\tX = %u\n\tY = %d\n", x, y);
		line();

		W = W_a = Q = Q_a = 0;

		W = ((x << 5) + (x << 4) + (x << 2) + x) >> 3;
		Q = ((y << 5) + (y << 4) + (y << 2) + y) >> 3;

		__asm {
			mov		esi, x
			mov		eax, esi
			shl		eax, 5 // x << 5

			mov		ebx, esi
			shl		ebx, 4 // x << 4
			add		eax, ebx

			mov		ebx, esi
			shl		ebx, 2 // x << 2
			add		eax, ebx

			add		eax, esi
			shr		eax, 3

			mov		W_a, eax



			mov		esi, y
			mov		eax, esi
			shl		eax, 5 // x << 5

			mov		ebx, esi
			shl		ebx, 4 // x << 4
			add		eax, ebx

			mov		ebx, esi
			shl		ebx, 2 // x << 2
			add		eax, ebx

			add		eax, esi
			shr		eax, 3

			mov		Q_a, eax
		}

		printf("[Standart division] W = %u\n", x * a / b);
		printf("[Standart division] Q = %d\n", y * a / b);
		line();

		printf("[C] W = %u\n", W);
		printf("[C] Q = %d\n", Q);
		line();

		printf("[ASM] W = %u\n", W_a);
		printf("[ASM] Q = %d\n", Q_a);
		line();
		printf("\n");
	}

}
