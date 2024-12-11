"""
Ved hjælp af nedenstående skal I lave en hash ud af teksten "password123":
Byg gerne en funktion til det, så den kan genbruges.

import hashlib
md5_hash = hashlib.md5(input_text.encode()).hexdigest()

--------------------

Kopier nu hash koden der kommer ud og indsæt den i en fil (hashes.txt) 
og forsøg nu at knække koden ved hjælp af hashcat på jeres Kali Linux:

--------------------

hashcat -m 0 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt

Forklaring:
-m 0: MD5-hash.
-a 0: Ordbogsangreb.
hashes.txt: Filen med hashen.
/usr/share/wordlists/rockyou.txt: En ordbog med mulige adgangskoder (fx rockyou.txt).

Bemærk, hvis ikke allerede rockyou.txt er pakket ud, gøres det ved: 
    gunzip /usr/share/wordlists/rockyou.txt.gz

---------------------

Hvis Hashcat finder adgangskoden, vises resultatet i terminalen og kan gemmes i hashcat.potfile.
Du kan tilføje --show til kommandoen for at se de dekrypterede hashes bagefter

---------------------

Gentag nu øvelsen med et par andre brugte passwords, som:
- newpass
- homework
- monkey
- summer
"""



