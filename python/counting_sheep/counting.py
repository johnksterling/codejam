import itertools

def is_done(bitmap):
	return bitmap[0] and bitmap[1] and bitmap[2] and bitmap[3] and bitmap[4] and bitmap[5] and bitmap[6] and bitmap[7] and bitmap[8] and bitmap[9]

inputname = input('Inputfile: ')
f = open(inputname)
o = open(inputname + '.out', 'w')
count = int(f.readline())
print('processing ' + str(count) + ' entries')
for entry in range(count):
	bitmap = [False,False,False,False,False,False,False,False,False,False]
	test_start = int(f.readline())
	print('    start: ' + str(test_start))
	entry_output = 'INSOMNIA'
	if test_start != 0:
		multiplier = 1
		while not is_done(bitmap):
			next_number = multiplier*test_start
			number_string = str(next_number)
			''.join(ch for ch, _ in itertools.groupby(number_string))
			for ch in number_string:
				bitmap[int(ch)] = True
			multiplier += 1
		entry_output = str(next_number)
	o.write('Case #' + str(entry+1) + ': ' + str(entry_output) + '\n')
f.close()
o.close()
