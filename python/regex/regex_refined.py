inputname = input('Inputfile: ')
f = open(inputname)
o = open(inputname + '.out', 'w')
count = int(f.readline())
print('processing ' + str(count) + ' entries')


def get_end_idx(tokens):
    end_idx = 0
    print('Getting end index: ' + tokens)
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
    # handle the trailing *
    if end_idx+1 < len(tokens) and tokens[end_idx+1] == '*':
        end_idx += 1
    print('Found: ' + str(end_idx))
    return end_idx


def tokenize_level(level_string):
    idx = 0
    tokens = []
    running_string = ''
    while idx < len(level_string):
        if level_string[idx] == '(':
            end = get_end_idx(level_string[idx:])
            running_string += level_string[idx:end]
            idx = end
        elif level_string[idx] == '|':
            tokens.append(running_string)
            running_string = ''
            idx += 1
        else:
            running_string += level_string[idx]
            idx += 1
    tokens.append(running_string)
    return tokens


def parse_string(elem_string):
    # parse tokens, each token is a node
    # node types:  =, |, *
    # terminal nodes have data (i.e.  number), parens have a list of child nodes
    this_level_type = '?'

    idx = 0
    children = []
    while idx < len(elem_string):
        if elem_string[idx] == '(':
            # recursively process child and skip to end
            end_idx = get_end_idx(elem_string[idx:])
            end_idx += idx
            sub_start = idx + 1
            sub_end = end_idx - 1
            if sub_end+1 < len(elem_string) and elem_string[sub_end+1] == '*':
                child_string = elem_string[sub_start:sub_end]
                this_level_type = '*'
                child_nodes = parse_string(child_string)
            else:
                sub_end += 1
                child_string = elem_string[sub_start:sub_end]
                this_level_type = '|'
                list_of_child_strings = tokenize_level(child_string)
                child_nodes = []
                for token in list_of_child_strings:
                    or_nodes = parse_string(token)
                    or_node = dict()
                    or_node['type'] = '|='
                    or_node['data'] = or_nodes
                    child_nodes.append(or_node)
            current_node = dict()
            current_node['type'] = this_level_type
            current_node['data'] = child_nodes
            children.append(current_node)
            idx = end_idx + 1
        else:
            # just add it to the current running list
            leaf = dict()
            leaf['type'] = '='
            leaf['data'] = int(elem_string[idx])
            children.append(leaf)
            idx += 1
    return children


def handle_star(star_nodes, index, input):
    result = False
    should_continue = True
    result_index = index
    while should_continue:
        for current_star in star_nodes:
            is_matched, new_index = match([current_star], result_index + 1, input)
            if is_matched:
                result_index = new_index
                result = True
                if result_index >= len(input) - 1:
                    should_continue = False
            else:
                should_continue = False
                break
    return result, result_index


def handle_or(or_nodes, index, input):
    result = False
    result_index = index
    for current_or in or_nodes:
        is_matched, new_index = match([current_or], result_index + 1, input)
        if is_matched:
            result = True
            result_index = new_index
            break
    return result, result_index


def match(regex_tree, index, input):
    result_index = index
    idx = index
    is_match = True
    for node in regex_tree:
        print('processing index: ' + str(idx))
        print(node)
        if node['type'] == '|':
            is_match, idx = handle_or(node['data'], idx, input)
        elif node['type'] == '=':
            is_match = int(input[idx]) == node['data']
            if is_match:
                idx += 1
        elif node['type'] == '*':
            is_match, idx = handle_star(node['data'], idx, input)
        elif node['type'] == '|=':
            is_match, idx = match(node['data'], idx, input)
        if is_match:
            result_index = idx
        elif node['type'] != '*':
            # failed to match if its not a star (which can zero match)
            break
        if idx >= len(input):
            # if we run out of regex and have more numbers then fall out
            break
        print('DONE PROCESSING: ' + str(is_match) + '  ' + str(result_index))
    return is_match, result_index


for entry in range(count):
    range_min, range_max = f.readline().strip().split(' ')
    regex = f.readline().strip()
    regex_array = parse_string(regex)
    print(regex)
    print(regex_array)
    count = 0
    for idx in range(int(range_min), int(range_max)+1):
        print('Testing ' + str(idx))
        is_match = False
        is_match, match_index = match(regex_array, 0, str(idx))
        if is_match and match_index == len(str(idx)):
            count += 1
            print('Matched!  ' + str(idx))
    print('Case ' + str(entry+1) + ': ' + str(count))
f.close()
o.close()
