with open('pi_million.txt') as file_object:
	lines = file_object.readlines()

pi=''

for line in lines:
	pi += line.strip()

birthday = input('Your birthday: ')
if birthday in pi[:1000000]:
	print('Your birthday in 1 million digits pi!!!')
	print(pi.index(birthday))
else:
	print('(((')

