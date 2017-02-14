import itertools

def all_lead(lists):
	result = True
	for current in lists:
		for car in list(current):
			if car == 'G':
				result = False
				break
	return result

def get_lists_with_no_gold(lists, index):
	result = []
	for current in lists:
		if current[index] == 'L':
			result.append(current)
	return result

def get_next_favorite_index(lists, k):
	favorite_index = 0
	favorite_gold_count = 0
	for i in range(k):
		current_gold_count = 0
		for current in lists:
			if current[i] == 'G':
				current_gold_count += 1
		if current_gold_count > favorite_gold_count:
			favorite_index = i
	return favorite_index

def apply_function(input, original, k):
	result = ''
	print('processing: ' + input)
	for car in list(input):
		if car == 'L':
			result += original
		else:
			result += k * 'G'
	return result


inputname = input('Inputfile: ')
f = open(inputname)
o = open(inputname + '.out', 'w')
count = int(f.readline())
print('processing ' + str(count) + ' entries')
for entry in range(count):
	print('Case #' + str(entry+1) + '\n')
	perms = []
	current = f.readline().strip()
	(k,c,s) = current.split(' ')
	iterations = itertools.product('GL', repeat=int(k))
	for art in iterations:
		original = ''.join(art)
		test_input = original
		print(test_input)
		final = test_input
		if 'L' in final:
			for base in range(int(c)-1):
				final = apply_function(test_input, original, int(k))
				test_input = final
			perms.append(final)

	turned_indexes = []
	found = False
	current_perms = perms
	while len(turned_indexes) < int(s) and not found:
		favorite = get_next_favorite_index(current_perms, int(k))
		current_perms = get_lists_with_no_gold(current_perms, favorite)
		turned_indexes.append(favorite+1)
		found = all_lead(current_perms)
	answer = 'IMPOSSIBLE'
	if found:
		answer = ' '.join(map(str, turned_indexes))
	o.write('Case #' + str(entry+1) + ': ' + answer + '\n')
f.close()
o.close()
