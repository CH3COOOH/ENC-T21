def led(x, y, a, b):
	if x == y:
		return a
	else:
		return b


def openssl_plaintext(plaintext, key, algorithm, direction):
	if algorithm == 'a2c':
		return 'echo -e \'{pt}\' | openssl {dr}aes-256-ctr {pm} -pass pass:{key}'\
		.format(pt=plaintext, dr=led(direction, 'e', 'enc -e -', ''), pm=led(direction, 'e', '-a -salt', '-d -base64'), key=key)
	
	elif algorithm == 'a2c-p':
		return 'echo -e \'{pt}\' | openssl {dr}aes-256-ctr {pm} -pbkdf2 -pass pass:{key}'\
		.format(pt=plaintext, dr=led(direction, 'e', 'enc -e -', ''), pm=led(direction, 'e', '-a -salt', '-d -base64'), key=key)
	
	elif algorithm == 'as':
		return 'echo -e \'{pt}\' | ./asemica {dr} -c ./corpus.txt'\
		.format(pt=plaintext, dr=led(direction, 'e', 'enc', 'dec'))
	
	elif algorithm == 'a2c-as':
		if direction == 'e':
			return 'echo -e \'{pt}\' | openssl enc -e -aes-256-ctr -a -salt -pass pass:{key} | ./asemica enc -c ./corpus.txt'\
		.format(pt=plaintext, key=key)
		else:
			return 'echo -e \'{pt}\' | ./asemica dec -c ./corpus.txt | openssl aes-256-ctr -d -base64 -pass pass:{key} '\
		.format(pt=plaintext, key=key)


if __name__ == '__main__':
	import os
	os.system(openssl_plaintext('fuck you', 'P@ssw0rd', 'a2c', 'e'))
	print('\n')
	os.system(openssl_plaintext('U2FsdGVkX18IyFwRrWgB1zF5lbyegOkBXw==', 'P@ssw0rd', 'a2c', 'd'))
	print('\n')
	# os.system(openssl_plaintext('fuck you', 'P@ssw0rd', 'a2c-p', 'e'))
	# print('\n')
	# os.system(openssl_plaintext('U2FsdGVkX1+MQMuH60dz2PfR6ofGOeDDbg==', 'P@ssw0rd', 'a2c-p', 'd'))
	# print('\n')
	os.system(openssl_plaintext('fuck you', '', 'as', 'e'))
	print('\n')
	os.system(openssl_plaintext('his He Because don encourage After found about Kaya need check him Michael Cheryl Josepph more excited am Wow re beside and I Calm I Alright says Alex', '', 'as', 'd'))
	print('\n')
	os.system(openssl_plaintext('fuck you', 'P@ssw0rd', 'a2c-as', 'e'))
	print('\n')
	os.system(openssl_plaintext('and I Because and It He Alex says Herkins quietly stick and Kayla Damon Damon If Is I Because got by I Because didn have I Bottom I Can Damon After first they at It Emmett What are Shut guard don be It Emmett What been Who am Damon Christy that Doctor of I Alex says If could around feet it Emmett What around Mason He After couple days what I Calm or again do The Do Damon If can Kayla We She He Alex Tried do She It Love her What a BUt', 'P@ssw0rd', 'a2c-as', 'd'))
	print('\n')
