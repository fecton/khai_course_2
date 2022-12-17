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

unsigned long value, value_a;

unsigned char mod2, reg,  mod2_a, reg_a;
unsigned short kop, reg2, kop_a, reg2_a;

unsigned short tmp_short;

int main() {
	printf("\n\t\t(C) Lytvynenko A.V., 2022");
	printf("\n\tPacking 32-bit number Value");

	while (1) {
		
		cout << "\nEnter 3 16-digest numbers for kop (for example, fff): ";
		cin >> hex >> kop;

		cout << "Enter 2 16-digest numbers for reg (for example, 3f): ";
		cin >> tmp_short; reg = tmp_short;

		cout << "Enter 2 16-digest numbers for mod2 (for example, 1f): ";
		cin >> tmp_short; mod2 = tmp_short;

		cout << "Enter 3 16-digest numbers for reg2 (for example, 1ff): ";
		cin >> reg2;
		
		kop_a = kop;
		reg_a = reg;
		mod2_a = mod2;
		reg2_a = reg2;



		reg2 &= 0x1ff;
		mod2 &= 0x1f;
		reg &= 0x3f;
		kop &= 0xfff;

		value = kop;
		value = (value << 6) | reg;
		value = (value << 5) | mod2;
		value = (value << 9) | reg2;

		__asm {
			and reg2_a, 0x1ff
			and mod2_a, 0x1f
			and reg_a, 0x3f
			and kop_a, 0xfff

			sub eax, eax

			mov ax,	kop_a
			shl eax, 6

			or al, reg_a
			shl eax, 5

			or al, mod2_a
			shl eax, 9
			
			or ax, reg2

			mov value_a, eax

		};

		cout << hex
			<< "Packed bytes group kop (C++): " << value
			<< "\nPacked bytes group kop (ASM): " << value_a;
	}
	return 0;
}