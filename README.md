# El_gamal
Realization of El Gamal encryption and digital signature algorithms.


You need to install pycryptodome lib, try it using command: _pip install pycryptodome_

**"digital_sign.py"** is an implementation of El Gamal digital signification algorithm, that generates a sign for your message (variable "msg"), for example- "Hello World!". Variable "bits" is created to set the bit size (in my situation- 2048) and you can also change bit size to yours (for example- 256).

**"encryption.py"** is an implementation of Commutative El Gamal encryption algorithm. I used variable "bits" to set the bit size for key generation, and variable "M" to set the message.  
