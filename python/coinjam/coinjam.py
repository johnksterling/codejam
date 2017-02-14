import itertools
def factorizate(x):
	result = 0
	for i in range(2, x - 1):
		if x % i == 0:
			result = i
			break
		if i > 500:
			break
	return result

inputname = input('Inputfile: ')
f = open(inputname)
o = open(inputname + '.out', 'w')
count = int(f.readline())
print('processing ' + str(count) + ' entries')
for entry in range(count):
	current = f.readline().strip()
	(length, target) = current.split(' ')
	o.write('Case #' + str(entry+1) + ': \n')
	print('target: ' + target + ' length ' + length)
	iterations = itertools.product('01', repeat=int(length)-2)
	num_coins = 0
	for middle in iterations:
		test_input = '1' + ''.join(middle) + '1'
		proof = test_input
		is_coin = True
		for base in range(2, 11):
			result = int(test_input, base)
			divisor = factorizate(result)
			proof += ' ' + str(divisor)
			if divisor == 0:
				is_coin = False
				break
		if is_coin:
			num_coins += 1
			o.write(proof + '\n')
		if num_coins >= int(target):
			break
f.close()
o.close()
