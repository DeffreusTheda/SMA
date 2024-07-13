# Expo

## Object 1: Binary Representation of Fraction

![Object 1](Object%201.png)

Some decimal fraction can't be perfectly presented in the form of binary.
When you're converting the decimals of a denary number to binary, the accuracy of the value is limited by the amount of bits you have.
In C, there's two type of decimal number: float and double.
Float has 32 bits whereas double has 64 bits.
These bits are further down split for mantissa and exponent: 24 with 8 and 53 with 11 for float and double, respectively.
Thus, any binary representation of a fraction has an uncertainty:
Float is ± $2^{-8}$ or $3.90625 \cdot 10^{-3}$, whereas double is ± $2^{-11}$ or $4.8828125 \cdot 10^{-4}$

## Object 2: Unit Test in Java


