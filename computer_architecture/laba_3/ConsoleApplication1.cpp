#include <stdio.h>
#include <iostream>
#include <iomanip>
using namespace std;

long int
    a = 0, b = 0, x = 0,
    a1, b1, x1, tmp;

int err;
int err_a;

# define ONE 1
# define FIVE 5
# define TWENTY_FIVE 25

# define VAR 5

int main()
{
    printf("\n\t\t(C) Lytvynenko Andrii, 2022");
    printf("\n\t a > b: a/b-1");
    printf("\n\t a = b: -25");
    printf("\n\t a < b: (b*b*b-5)/a");
    printf("\nPlease, enter A,B: ");
    scanf("%li%li", &a, &b);

    a1 = a / (VAR + 2);
    b1 = b / (VAR + 3);
    err = 0;

    printf("a = %li b = %li\n", a1, b1);

    if (a1 == b1) {
        x = -TWENTY_FIVE;
    }
    else {
        if (a1 > b1) {
            if (b1 == 0) {
                err = 1;
            }
            else {
                x = a1 / b1 - ONE;
            }
        }
        else {
            if (a1 == 0) {
                err = 1;
            }
            else {
                x = (b1 * b1 * b1 - FIVE) / a1;
            }
        }
    }

    __asm {
        mov err_a, 0
    }

    __asm {
        mov ebx, VAR+3
        mov eax, b
        cdq
        idiv ebx
        mov edi, eax

        mov ebx, VAR+2
        mov eax, a
        cdq
        idiv ebx
    }

    __asm {
        cmp eax,edi
        je Equal
        jl Less
        
    
                Greater:
            // if b == 0
            test edi, edi
            je Error
            // else
            // x = a / b - ONE;
            cdq
            idiv edi
            sub eax, ONE
            mov x1, eax
            jmp End

                Equal:
            // if a == b
            mov eax, TWENTY_FIVE
            neg eax
            mov x1, eax
            jmp End
            // if a < b
                Less:
            // if a == 0
            test eax, eax
            je Error
            // x = (b1 * b1 * b1 - FIVE) / a;
            mov tmp, edi
            imul edi, edi
            imul edi, tmp
            sub edi, FIVE
            cdq
            xchg edi, eax
            idiv edi
            mov x1, eax
            jmp End
                Error:
            inc err_a
                End:
        // a - edi
        // b - ebx

    }

    if (err) {
        printf("[ERROR] [C] Divided by zero!\n");
    }
    else {
        printf("[SUCCESS] [C] The result: %li\n", x);
    }

    if (err_a) {
        printf("[ERROR] [ASM] Divided by zero!\n");
    }
    else {
        printf("[SUCCESS] [ASM] The result: %li!\n", x1);
    }
}


