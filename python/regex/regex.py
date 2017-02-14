inputname = input('Inputfile: ')
f = open(inputname)
o = open(inputname + '.out', 'w')
count = int(f.readline())
print('processing ' + str(count) + ' entries')


def get_end_idx(tokens):
    end_idx = 0
    matching_parens = 0
    for peak in tokens:
        if peak == ')':
            matching_parens -= 1
        elif peak == '(':
            matching_parens += 1
        if matching_parens == 0:
            break
        else:
            end_idx += 1
    return end_idx


def parse_string(elem_string):
    result = []
    idx = 0
    while idx < len(elem_string):
        next_node = dict()
        if elem_string[idx] == '(':
            end_idx = get_end_idx(elem_string[idx:])
            end_idx += idx
            if max_depth and '|' in elem_string[idx+1:end_idx]:
                next_node['type'] = '|'
                or_elems = []
                final_elements = elem_string[idx+1:end_idx].split('|')
                for fin_elems in final_elements:
                    sub_node = dict()
                    sub_node['data'] = list(fin_elems)
                    sub_node['type'] = '='
                    or_elems.append(sub_node)
                next_node['data'] = or_elems
            else:
                next_node['data'] = parse_string(elem_string[idx+1:end_idx])
            if end_idx+1 < len(elem_string):
                if elem_string[end_idx+1] == '*':
                    next_node['type'] = '*'
                    end_idx += 1
            idx = end_idx + 1
        else:
            next_node['data'] = elem_string[idx]
            next_node['type'] = '='
            idx += 1
        result.append(next_node)
    return result


def match_char(subreg, char):
    result = True
    if char != subreg:
        result = False
    return result


def match(regex, string):
    c_arr = list(string)
    result = True
    for char in c_arr:
        if not match_char(regex, char):
            result = False
            break
    return result


for entry in range(count):
    print('Case ' + str(entry))
    range_min, range_max = f.readline().strip().split(' ')
    regex = f.readline().strip()
    regex_array = parse_string(regex)
    for reg in regex_array:
        print(reg['type'] + str(reg['data']))
#    for idx in range(int(range_min), int(range_max)):
#        match(regex, str(idx))
f.close()
o.close()

