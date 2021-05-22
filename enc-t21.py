# 1st launch on 2021.02.01

import os
import getpass
from openssl_cmd import openssl_plaintext

plaintext = input('Content:\n')
algorithm = input('\nAlgorithm (a2c | a2c-p | as | a2c-as):\n')
direction = input('\nEncryption or decryption? (e | d) ')
while True:
	key = getpass.getpass('\nKey:')
	if direction == 'd':
		break
	key_ = getpass.getpass('\nInput again:')
	if key != key_:
		print('\n*** DIFFERENT KEY ***')
	else:
		break

print('\n[RESULT]\n')
os.system(openssl_plaintext(plaintext, key, algorithm, direction))
print('\n')
