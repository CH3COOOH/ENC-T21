# 1st launch on 2021.02.01

import os
import sys

text = input('Content: ')

if sys.argv[1] == '-e':
	os.system('echo \'%s\' | openssl enc -e -aes-256-ctr -a -salt' % text)
elif sys.argv[1] == '-d':
	os.system('echo \'%s\' | openssl aes-256-ctr -d -base64' % text)