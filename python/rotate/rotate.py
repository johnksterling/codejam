def detect_board_winners(n,k,grids):
	is_red = False
	is_blue = False
	print("------")
	for grid in range(n):
		across_hits = 0
		prev = None
		for across in range(n):
			#skip .
			print("Hits across " + str(grid) + "x" + str(across) + ": " + str(across_hits) + " compared to " + str(k) + " prev: " + str(prev) + " cur: " + str(grids[grid][across]))
			if( grids[grid][across] != '.'):
				if(prev is None):
					prev = grids[grid][across]
					across_hits = 1
				else:
					if (prev == grids[grid][across]):
						print "    incrementing"
						across_hits = across_hits + 1
					else:
						prev = grids[grid][across]
						across_hits = 1
			if( across_hits >= k ):
				if(prev == 'R' ):
					is_red = True
				if(prev == 'B'):
					is_blue = True

	for grid in range(n):
		down_hits = 0
		prev_down = None
		for down in range(n):
			if( grids[down][grid] != '.'):
				if( prev_down is None ):
					prev_down = grids[down][grid]
					down_hits = 1
				else:
					if (prev_down == grids[down][grid]):
						down_hits = down_hits + 1
					else:
						prev_down = grids[down][grid]
						down_hits = 1
			if( down_hits >= k):
				if(prev_down == 'R' ):
					is_red = True
				if(prev_down == 'B'):
					is_blue = True
	result = 'Neither'
	if( is_red and is_blue ):
		result = 'Both'
	elif (is_red ):
		result = 'Red'
	elif (is_blue):
		result = 'Blue'


	return result

def process_entry(n,k,grids):
	return detect_board_winners(n,k,grids)

inputname = raw_input('Inputfile: ')
f = open(inputname)
o = open(inputname + '.out', 'w')
count = int(f.next())
print('processing ' + str(count) + ' entries')
for entry in range(count):
	(n,k) = [int(n) for n in f.next().split(' ')]
	grids = []
	for grid_idx in range(n):
		grids.append(list(f.next()))

	entry_output = process_entry(n,k, grids)
	o.write('Case #' + str(entry+1) + ': ' + entry_output + '\n')
f.close()
o.close()
