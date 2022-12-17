#include <stdio.h>
#include <intrin.h>

// TODO: зробити ділення для змінних a,b,c на асемблері

long int
	tmp = 0, tmp2 = 0,
	right = 0, left = 0,
	right_a = 0, left_a = 0,
	a, b, c,
	a_a, b_a, c_a;
int err;
int err_la;

#define VARIANT 12

int main() {
	printf("Lytvynenko Andrii 525a\n");
	printf("The equation: (a+b+c)**2 = a**2 + b**2 + c**2 + +2*a*b + 2*a*c + 2*b*c\n");

	for (;;) {
		printf("Please enter a,b,c: ");
		scanf("%li%li%li", &a, &b, &c);

		a_a = a;
		b_a = b;
		c_a = c;

		a = a / (VARIANT + 2);
		b = b / (VARIANT + 3);
		c = c / (VARIANT + 4);

		tmp = a + b + c;;
		left = tmp * tmp;

		right = a * a + b * b + c * c + 2*a*b + 2*a*c + 2*b*c;

		err = 0;

		// (a+b+c)**2 = a**2 + b**2 + c**2 + +2*a*b + 2*a*c + 2*b*c
		__asm {
			mov		ebx,0
			mov		right_a,ebx

			mov		ebx,0
			mov		left_a,ebx

			// a
			mov		eax,a_a
			mov		ebx,VARIANT
			add		ebx,2
			cdq
			idiv	ebx
			mov		a,eax

			// b
			mov		eax,b_a
			mov		ebx,VARIANT
			add		ebx,2
			cdq
			idiv	ebx
			mov		b,eax

			// c
			mov		eax,c_a
			mov		ebx,VARIANT
			add		ebx,2
			cdq
			idiv	ebx
			mov		c,eax

			// left
			mov		ebx,a
			add		ebx,b	// a + b
			mov		eax,c 
			add		ebx,eax	// a + b + c
			imul	ebx,ebx   // (a+b+c)**2
			mov		left_a,ebx // left_a = (a+b+c)**2

			// right
			mov		ebx,a
			imul	ebx,ebx
			add		right_a,ebx

			mov		ebx, b
			imul	ebx, ebx
			add		right_a, ebx

			mov		ebx, c
			imul	ebx, ebx
			add		right_a, ebx

			// (a+b+c)**2 = a**2 + b**2 + c**2 + +2*a*b + 2*a*c + 2*b*c
			mov		ebx,2
			imul	ebx,a
			imul	ebx,b
			add		right_a,ebx		// right_a = (a**2 + b**2 + c**2) + 2*a*b

			mov		ebx,2
			imul	ebx,a
			imul	ebx,c
			add		right_a,ebx		// right_a = (a**2 + b**2 + c**2) + 2*a*b + 2*a*c

			mov		ebx,2
			imul	ebx,b
			imul	ebx,c
			add		right_a,ebx		// right_a = (a**2 + b**2 + c**2) + 2*a*b + 2*a*c + 2*b*c

		}

		printf("A: %li\nB: %li\nC: %li\n", a,b,c);

		printf("[C] Left: %li \t Right: %li\n", left, right);
		printf("[ASM] Left: %li \t Right: %li\n", left_a, right_a);
	}


	return 0;
}

