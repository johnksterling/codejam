inputname = input('Inputfile: ')
f = open(inputname)
o = open(inputname + '.out', 'w')
count = int(f.readline())
print('processing ' + str(count) + ' entries')
for entry in range(count):
    print('Case ' + str(entry))
    test_stack = f.readline().strip().split(' ')
    idx = 1
    n = int(test_stack[0])
    r = float(int(test_stack[1])/1000000)
    o.write('Case #' + str(entry+1) + ': ' + str(r) + '\n')
f.close()
o.close()
