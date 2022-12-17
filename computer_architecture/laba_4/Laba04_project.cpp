/*
File: unpack.cc
Unpacking bytes group

This program unpacking byte groups from unsigned int

Input datta:
unsigned int value, which consts byte groups:

	12 + 6 + 5 + 9

	31						  0
	kop		reg		mod2	 reg2
	 12      6        5      9
*/


#include <iostream>
#include <iomanip>

using namespace std;

unsigned long value;
unsigned char mod2, reg, mod2_a, reg_a;
unsigned short kop, reg2, kop_a, reg2_a;

int main() {
	printf("\n\t\t(C) Lytvynenko A.V., 2022");
	printf("\n\tUnpacking byte groups");

	while (1) {
		printf("\n\tUnpacking 32-bit number Value");
		printf("\nPlease, enter 8 16-bits numbers (exp, 5a9db8e4) : ");
		scanf("%x", &value);

		reg2 = value & 0x1ff;
		mod2 = (value >> 9) & 0x1f;
		reg = (value >> 14) & 0x3f;
		kop = (value >> 20) & 0xfff;

		__asm {
			mov eax,value

			mov reg2_a, ax
			and reg2_a, 0x1ff
			shr eax, 9

			mov mod2_a, al
			and mod2_a, 0x1f
			shr eax, 5

			mov reg_a, al
			and reg_a, 0x3f
			shr eax, 6

			mov kop_a, ax
			and kop_a, 0xfff
		}

		cout << hex
			<< "Bytes group kop (C++): "   << (int)kop
			<< "\nBytes group reg (C++): " << (int)reg
			<< "\nBytes group mod2 (C++): " << (int)mod2
			<< "\nBytes group reg2 (C++): " << (int)reg2

			<< "\n\nBytes group kop (Asm): " << (int)kop_a
			<< "\nBytes group reg (Asm): " << (int)reg_a
			<< "\nBytes group mod2 (Asm): " << (int)mod2_a
			<< "\nBytes group reg2 (Asm): " << (int)reg2_a
			<< endl;
	}
	return 0;
} 