inputname = input('Inputfile: ')
f = open(inputname)
o = open(inputname + '.out', 'w')
count = int(f.readline())
print('processing ' + str(count) + ' entries')
for entry in range(count):
	print('Case #' + str(entry+1) + '\n')
	perms = []
	current = f.readline().strip()
	print('git: ' + current)
	(k,c,s) = current.split(' ')
	numbers = list(range(1, int(k)))
	answer = ' '.join(map(str, numbers))
	o.write('Case #' + str(entry+1) + ': ' + answer + '\n')
