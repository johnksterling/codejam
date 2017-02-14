import itertools

inputname = input('Inputfile: ')
print('opening ',inputname) 
f = open(inputname)
o = open(inputname + '.out', 'w')
count = int(f.readline())
print('processing ' + str(count) + ' entries')
case_num = 1
for entry in range(count):
        current = f.readline().strip()
        (c,j) = current.split()
        c_arr = list(c)
        j_arr = list(j)
        running_c = '0'
        running_j = '0'
        for idx in range(len(c_arr)):
                #if neither are ? keep moving
                if c_arr[idx] != '?' and j_arr[idx] != '?':
                        running_c += c_arr[idx]                        
                        running_j += j_arr[idx]
                #if both are ? then give the current loser 9 and urrent winner 0
                elif c_arr[idx] == '?' and j_arr[idx] == '?':
                        if int(running_c) > int(running_j):
                                running_c += '0'
                                running_j += '9'
                        elif int(running_j) > int(running_c):
                                running_j += '0'
                                running_c += '9'
                        else:
                                running_j += '0'
                                running_c += '0'
                #if c is ? then if c is losing give it 9, if its winning 0, if its tied give it j's digit
                elif c_arr[idx] == '?':
                        if int(running_c) > int(running_j):
                                running_c += '0'
                        elif int(running_c) < int(running_j):
                                running_c += '9'
                        else:
                                #if there is another letter and each has a non qst mark then we need to use that to go up/down to j
                                if idx +1 < len(c_arr) and c_arr[idx+1] != '?' and j_arr[idx] != '0' and  j_arr[idx+1] != '?' and int(c_arr[idx+1]) > int(j_arr[idx+1]) and int(c_arr[idx+1])-int(j_arr[idx+1]) > 5:
                                        adjusted = int(j_arr[idx])
                                        adjusted -= 1
                                        running_c += str(adjusted)
                                else:
                                        running_c += j_arr[idx]
                        running_j += j_arr[idx]
                #if j is ? then if j is losing give it 9, if its winning 0, if its tied give it c's digit
                elif j_arr[idx] == '?':
                        if int(running_j) > int(running_c):
                                running_j += '0'
                        elif int(running_j) < int(running_c):
                                running_j += '9'
                        else:
                                #if there is another letter and each has a non qst mark then we need to use that to go up/down to j
                                if idx +1 < len(c_arr) and j_arr[idx+1] != '?' and c_arr[idx] != '0' and  c_arr[idx+1] != '?' and int(j_arr[idx+1]) > int(c_arr[idx+1]) and int(j_arr[idx+1])-int(c_arr[idx+1]) > 5:
                                        adjusted = int(c_arr[idx])
                                        adjusted -= 1
                                        running_j += str(adjusted)
                                else:
                                        running_j += c_arr[idx]
                        running_c += c_arr[idx]
                else:
                        print('UNEXPECTED SCENARIO for ' + current + ' at idx ' + str(idx))
        o.write('Case #' + str(case_num) + ': ' + running_c[1:] + ' ' + running_j[1:] + '\n')
        case_num += 1
f.close()
o.close()






