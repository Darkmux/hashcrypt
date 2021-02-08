#!/bin/python
#-*- coding: utf-8 -*-
#librerías
import hashlib, time
import sys
from os import system
from pyfiglet import figlet_format
#listado de tipo de hash
hashes = [
        'md5',
        'sha1',
        'sha224',
        'sha256',
        'sha512'
        ]
#banner
def banner():
	system('clear')
	print ('\033[1;36m',figlet_format('Hash',font='small'))
	print ('\033[1;31m',figlet_format('Crypt-v.2',font='small'))
	time.sleep(1.5)
	print ('\n\033[1;30mCreated by: \033[1;36mF@br1x and \033[1;36mDarkmux\n')
banner()
palabra = input("\033[1;37m[?] Ingrese el texto a cifrar:\033[1;33m ")
time.sleep(2)

# Para que no este el bug de que te pasa hashes sin ningun valor
if palabra == "":
       print("[!] no recibio texto!, intentalo de nuevo")
       sys.exit()

print('\n\t\t\033[1;37mHASH TEXT')
#Iteramos el contenido de la lista para cifrar el texto en diferentes tipos de hash de la lista
for tipo_hash in hashes:
  print(f'[*] \033[1;32m{tipo_hash.upper()} \033[1;37m: \033[1;36m{hashlib.new(tipo_hash, palabra.encode()).hexdigest()}')


#Convertimos los hashes en hash reversos
print('\n\t\t\033[1;37mHASH REVERSE TEXT')
for tipo_hash in hashes:
    hash_text = hashlib.new(tipo_hash, palabra.encode()).hexdigest()
    hash_reverse = hash_text[::-1]
    print(f'[*] \033[1;32m{tipo_hash.upper()} \033[1;37m: \033[1;36m{hash_reverse}')
  

print ("\n\033[1;33m[!] Todos los cifrados mostrados correctamente :)\033[0m")
