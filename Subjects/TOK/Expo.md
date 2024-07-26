# Expo

## Prompt: To what extent is certainty attainable?

## Object 1: Binary Representation of Fraction

![Object 1](Object%201.png)

Main point: Some decimal fraction can't be perfectly presented in the form of binary.
Binary is the representation of a number with base of 2, as opposed to base of 10 as it's widely used.
When you're converting the decimals of a denary number to binary, the accuracy of the value is limited by the amount of bits you have.
In C, a widely-used and old language, there's two type of decimal number: float and double.
Float has 32 bits whereas double has 64 bits.
These bits are further down split for mantissa and exponent: 24 with 8 and 53 with 11 for float and double, respectively.
Thus, any binary representation of a fraction has an uncertainty:
Float is ± $2^{-8}$ or $3.90625\times10^{-3}$, whereas double is ± $2^{-11}$ or $4.8828125\times10^{-4}$
The main concern here is the difference in accuracy of base 10 and base 2 at representing fraction with the same amount of digits.

## Object 2: A Digital Photograph and its Metadata

Metadata refer to 'data about data', that provides context and describe the characteristics, structure, and contents of a particular information.
It summarizes essential information about the data, making it easier to find, use, and reuse.
For a digital photograph, this can include latest file modification time, image size, camera model, GPS location, etc.
In current society, metadata is seen as factual and reliable.
But when downloading it from the internet, these metadata might be altered and modified intentionally.
This require technical knowledge to be performed, but technology has developed and software such as EasyTag make this process much easier.
This raise the doubt about the certainty of the metadata contained in the digital photograph.
The metadata might be removed to preserve privacy or modified for malicious purpose.
For example, the author metadata of an original music file is changed to steal copyright,
or modification of GPS metadata on an crime photograph, which might be used as an forged evidence in a court.
Metadata is uncertain, especially from unverified sources like the internet.

## Object 3: Digital Signatures

Digital signatures are a type of cryptographic primitive that uses advanced technology to ensure integrity and authenticity of a digital documents.
Digital signatures also verify the identity of the sender and ensure that the data originated from a trusted source.
It is commonly used for software distribution, financial transactions, and case where it's important to detect forgery.
Digital signatures are more secure than traditional electronic signatures and are widely recognized as a compliant form of online signature.
It uses asymmetric cryptography, which uses different key for encryption and decryption, promoting more security.
In relation to the second object, digital signatures can used to prevent tampering of metadata and thus ensure certainty.

