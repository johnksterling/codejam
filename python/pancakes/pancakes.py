def flip_range(stack, start, to):
	stack_array = list(stack)
	for idx in range(start, to):
		stack_array[idx] = '+' if stack_array[idx] == '-' else '-'
	return ''.join(stack_array)

inputname = input('Inputfile: ')
f = open(inputname)
o = open(inputname + '.out', 'w')
count = int(f.readline())
print('processing ' + str(count) + ' entries')
for entry in range(count):
	print('Case ' + str(entry))
	test_stack = f.readline().strip()
	flip_count = 0
	idx = 1
	last_char = test_stack[0]
	while idx < len(test_stack):
		print('character ' + str(idx))
		while  idx < len(test_stack) and test_stack[idx] == last_char:
			idx += 1
		if idx < len(test_stack):
			print('    found a sub stack: ' + test_stack + ' from ' + str(0) + ' to ' + str(idx))
			flip_count += 1
			test_stack = flip_range(test_stack, 0, idx)
			last_char = test_stack[idx]
			idx += 1
	if test_stack[0] == '-':
		print('    Finished, flipping all: ' + test_stack)
		test_stack = flip_range(test_stack, 0, len(test_stack))
		flip_count += 1
	o.write('Case #' + str(entry+1) + ': ' + str(flip_count) + '\n')
f.close()
o.close()
