import itertools
def decrement(counts, letters):
        for letter in letters:
                counts[letter] = counts[letter] - 1
        return counts

inputname = input('Inputfile: ')
print('opening ',inputname) 
f = open(inputname)
o = open(inputname + '.out', 'w')
count = int(f.readline())
print('processing ' + str(count) + ' entries')
for entry in range(count):
        current = f.readline().strip()
        letters = list(current)
        counts = {}
        results = []
        o.write('Case #' + str(entry+1) + ': ')
        for l in letters:
                print('Here: ',l)
                if l in counts:
                        counts[l] += 1
                else:
                        counts[l] = 1
        if 'Z' in counts:
                current_range = counts['Z']
                for index in range(current_range):
                        counts = decrement(counts, list('ZERO'))
                        results.append(0)
        if 'G' in counts:
                current_range = counts['G']
                for index in range(current_range):
                        counts = decrement(counts, list('EIGHT'))
                        results.append(8)
        if 'X' in counts:
                current_range = counts['X']
                for index in range(current_range):
                        counts = decrement(counts, list('SIX'))
                        results.append(6)
        if 'S' in counts:
                current_range = counts['S']
                for index in range(current_range):
                        counts = decrement(counts, list('SEVEN'))
                        results.append(7)
        if 'W' in counts:
                current_range = counts['W']
                for index in range(current_range):
                        counts = decrement(counts, list('TWO'))
                        results.append(2)
        if 'V' in counts:
                current_range = counts['V']
                for index in range(current_range):
                        counts = decrement(counts, list('FIVE'))
                        results.append(5)
        if 'H' in counts:
                current_range = counts['H']
                for index in range(current_range):
                        counts = decrement(counts, list('THREE'))
                        results.append(3)
        if 'U' in counts:
                current_range = counts['U']
                for index in range(current_range):
                        counts = decrement(counts, list('FOUR'))
                        results.append(4)
        if 'I' in counts:
                current_range = counts['I']
                for index in range(current_range):
                        counts = decrement(counts, list('NINE'))
                        results.append(9)
        if 'O' in counts:
                current_range = counts['O']
                for index in range(current_range):
                        counts = decrement(counts, list('ONE'))
                        results.append(1)
        results.sort()
        next_string = ''.join(map(str, results))
        o.write(next_string + '\n')
f.close()
o.close()
