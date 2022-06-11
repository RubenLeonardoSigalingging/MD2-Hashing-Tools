# Message: This Tool or Program Was Made Using Python Programming Language Version 3.8.10

# Created By: Ruben Leonardo Sigalingging.
# Created On: Saturday, June 11, 2022, 10:10 PM.
# Function: To Encrypt Messages, Passwords and Data Using the MD2 Hash Function.


# Pesan: Alat atau Program Ini Dibuat Menggunakan Bahasa Pemrograman Python Versi 3.8.10

# Dibuat Oleh: Ruben Leonardo Sigalingging.
# Dibuat Pada: Sabtu, 11 Juni 2022, 22:10.
# Fungsi: Untuk Mengenkripsi Pesan, Kata Sandi, dan Data Menggunakan Fungsi Hash MD2.
#!/usr/bin/env python3


def import_python_module():
	import os
	import sys
	from sys import version_info
	import hashlib
	import datetime
	from datetime import datetime
	from time import sleep
	import requests
	import json
	import urllib
	from urllib import request
	import Crypto.Hash
	from Crypto.Hash import MD2
import_python_module()


# Introduction or Pendahuluan
def introduction(by = "ruben leonardo sigalingging"):
	import pyfiglet
	tema = pyfiglet.figlet_format("MD2",font="slant")
	print(tema)
	print("---PENGANTAR or INTRODUCTION---")
	print("Source: https://en.wikipedia.org/wiki/MD2_(hash_function)")
	print("Sumber: https://en.wikipedia.org/wiki/MD2_(hash_function)")
	print("The MD2 Message-Digest Algorithm is a cryptographic hash function developed by Ronald Rivest in 1989.")
	print("MD2 Message-Digest Algorithm adalah fungsi hash kriptografi yang dikembangkan oleh Ronald Rivest pada tahun 1989.\n\n\n")
	print("---What is Hashing?---")
	print("Source: https://en.wikipedia.org/wiki/Hash_function")
	print("Sumber: https://en.wikipedia.org/wiki/Hash_function")
	print("A hash function is any function that can be used to map data of arbitrary size to fixed-size values.")
	print("Fungsi hash adalah fungsi apa pun yang dapat digunakan untuk memetakan data dengan ukuran arbitrer ke nilai ukuran tetap.\n\n\n")
	print("---What is MD2 Hashing in python?---")
	print("Source: https://text-id.123dok.com/document/8yd29wg1q-kegunaan-algoritma-fungsi-hash.html")
	print("Sumber: https://text-id.123dok.com/document/8yd29wg1q-kegunaan-algoritma-fungsi-hash.html")
	print("Message digest is a value derived from a message data that has unique properties.")
	print("Message digest adalah sebuah nilai yang berasal dari suatu data pesan yang memiliki sifat yang unik.")
	print("The message has a certain amount created by encrypting it.")
	print("Pesan tersebut mempunyai suatu besaran tertentu yang diciptakan dengan melakukan enkripsi.\n\n\n")
	print("Source: https://pycryptodome.readthedocs.io/en/latest/src/hash/md2.html")
introduction()


# file permission
import os
os.system("chmod 777 MD2HashFunction.py")


# time to code
def time_to_code(created_by = "ruben leonardo sigalingging"):
	import os
	import sys
	from sys import version_info
	import hashlib
	import datetime
	from datetime import datetime
	from time import sleep
	import requests
	import json
	import urllib
	from urllib import request
	import Crypto.Hash
	from Crypto.Hash import MD2
	print("\n\n\n")
	alamat_ip = requests.get("https://api.ipify.org/").text
	print(f"[!] Your Public IP Address: {alamat_ip}")
	plaintext = input("[!] Input Plaintext: ")
	MD2_hash_function = MD2.new()
	MD2_hash_function.update(plaintext.encode("ascii"))
	print(f"[!] The MD2 Hash Result From {plaintext} Is: {MD2_hash_function.hexdigest()}")
time_to_code()


# Kode warna di bahasa pemrogramman python 3.8.10
def color_code_in_python_programming():
	red = "\033[91m"
	blue = "\033[94m"
	underline = "\033[4m"
	bold_text = "\033[1m"
color_code_in_python_programming()