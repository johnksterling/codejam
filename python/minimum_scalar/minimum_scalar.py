def process_entry(vector_one, vector_two):
	lowest_product = None
	vector_one.sort()
	vector_two.sort(reverse=True)
	current_product = 0
	for index in range(len(vector_one)):
		current_product += vector_one[index] * vector_two[index]
	return current_product

inputname = raw_input('Inputfile: ')
f = open(inputname)
o = open(inputname + '.out', 'w')
count = int(f.next())
print('processing ' + str(count) + ' entries')
for entry in range(count):
	entry_size = int(f.next())
	print('entry ' + str(entry) + ' has ' + str(entry_size) + ' entries')
	vector_one = [int(n) for n in f.next().split(' ')]
	vector_two = [int(n) for n in f.next().split(' ')]
	entry_output = process_entry(vector_one, vector_two)
	o.write('Case #' + str(entry+1) + ': ' + str(entry_output) + '\n')
f.close()
o.close()
