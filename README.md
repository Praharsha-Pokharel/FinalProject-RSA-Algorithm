# FinalProject-RSA-Algorithm : RSA Algorithm implementation in python

DESCRIPTION:
When we talk about cybersecurity, we talk about securing our computer data 
and information from unauthorized access especially when banking, shopping, 
and communicating. We rely on encryption to keep cybercriminals out of our 
data, just as we secure our houses, restrict access to essential infrastructure, and 
protect our valuable property in the real world. Encryption is a process in 
which our data is encoded to hide it from unauthorized users. When our data is 
encrypted, even if someone gains access, they cannot decrypt it without a 
decryption code.

One such encryption method is using RSA algorithm. The RSA algorithm is an asymetric cryptography algorithm, which 
means it utilizes two mathematically related keys: a public and a private key. 
Everyone has access to the public key, while the private key is kept secret. The 
sender encrypts data using reciever's public key and the reciever decrypts it 
with their own private key. 
In this project, we will be implementing the RSA algorithm in an Excel 
based application.


**Project Goals:**
The primary goal of this project is to develop a program that encrypts a message using a public key 
which can be decrypted only by using the corresponding decryption key generated by the program. To add a extra layer of security the message is encrypted using a trigraph (3 letters) and decrypted with a quadgraph (4 letters).

**End users:**
Anyone who would like to just encrypt a message or learn about RSA algorithm.
This program is simple and easy to use. So, anyone with or without a technical background can use this program.

**Development Model:**
This program is developed using python programming language in a Pycharm IDE.

**Software requirements:**

Python: Download Link: https://www.python.org/downloads

Pycharm IDE: Download Link: www.jetbrains.com/pycharm/download || or any other IDE that can compile and run python programs.

MacOS: 10.14 or higher |
Windows: 64 Bit versions of Microsoft 10 or 8. |
2 GB Minimum RAM |
Python 2.7 or 3.5 or newer |

**Running the Code:**

1. After you run the code, first the program prompts you for two three-digit prime numbers. The program checks if the numbers are 3-digit prime and displays a "OK" message. 
Then the program calculates modulus(N) = p*q and Euler Totient(ET) = (p-1)*(q-1).
2. Next, the program asks for a public key (e). The rules for entering a public key is that it should be co-prime with N and ET.
3. Next, the program calculates a private key using Extended Euclidean Algorithm.
4. Then you are asked to enter a message to be encrypted. Please enter any length string with no spaces.
5. Press Y for encryption. Your message is encrypted and displayed.
6. Press Y for decryption. Your message is decrypted and displayed.

**References:**
1. Kyriacos, N., 2021. Understanding the Mathematics Behind Cryptography. Retrieved April 30, 2022 from https://scholars.carroll.edu/bitstream/handle/20.500.12647/10473/Kyriacos_Final_2021.pdf

2. Anon, 2021. Retrieved April 30, 2022 from GitHub - Mardokai/RSA-algorithm-. GitHub.

3. Brian Kell, 2010. 21-110: The extended Euclidean algorithm. Retrieved April 30, 2022 from Math.cmu.edu.









