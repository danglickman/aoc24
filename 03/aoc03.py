import re

def naive_sum(stuff):
    instructions = re.findall(r'mul\((\d+),(\d+)\)', stuff)
    result = 0
    for a, b in instructions:
        result += int(a) * int(b)
    return result

def main():

    with open('input') as f:
        input_data = f.read()

    result = naive_sum(input_data)

    print(result)


    # part 2
    result = 0
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r'don\'t\(\)')

    position = 0
    while position < len(input_data):
        dont_match = dont_pattern.search(input_data[position:])
        if dont_match:
            stop_position = position + dont_match.start()
            result += naive_sum(input_data[position:stop_position])
        else:
            result += naive_sum(input_data[position:])
            break
        position += dont_match.end()
        do_match = do_pattern.search(input_data[position:])
        if do_match is None:
            break
        position += do_match.end()

    print(result)




if __name__ == '__main__':
    main()