def calculate_count(ropes_a, ropes_b):
	intersections = 0
	for outer_idx in range(len(ropes_a)):
		outer_a = ropes_a[outer_idx]
		outer_b = ropes_b[outer_idx]
		for inner_idx in range(outer_idx, len(ropes_a)):
			inner_a = ropes_a[inner_idx]
			inner_b = ropes_b[inner_idx]
			product = (outer_a-inner_a) * (outer_b-inner_b)
			if( product < 0 ):
				intersections = intersections + 1
	return intersections

inputname = raw_input('Inputfile: ')
f = open(inputname)
o = open(inputname + '.out', 'w')
count = int(f.next())
print('processing ' + str(count) + ' entries')
for entry in range(count):
	rope_count = int(f.next())
	print('processing ' + str(rope_count) + ' ropes')
	ropes_a = []
	ropes_b = []
	for rope_idx in range(rope_count):
		(a,b) = [int(n) for n in f.next().split(' ')]
		print('  found a rope from ' + str(a) + ' to ' + str(b))
		ropes_a.append(a)
		ropes_b.append(b)
	result = calculate_count(ropes_a, ropes_b)
	o.write('Case #' + str(entry+1) + ': ' + str(result) + '\n')