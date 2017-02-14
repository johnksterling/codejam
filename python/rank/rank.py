inputname = input('Inputfile: ')
f = open(inputname)
o = open(inputname + '.out', 'w')
count = int(f.readline())
print('processing ' + str(count) + ' entries')
for entry in range(count):
	count_map = {}
	n = int(f.readline().strip())
	for idx in range(n*2-1):
		row = f.readline().strip().split(' ')
		for height in row:
			if height in count_map:
				count_map[height] += 1
			else:
				count_map[height] = 1
	a = []
	for h in count_map.keys():
		c = count_map[h]
		if c%2 != 0:
			a.append(int(h))
	if len(a) != n:
		print('entry ' + entry + ' is incorrect.')
		exit()
	a.sort()
	result = ' '.join(map(str, a))
	o.write('Case #' + str(entry+1) + ': ' + result + '\n')
f.close()
o.close()
