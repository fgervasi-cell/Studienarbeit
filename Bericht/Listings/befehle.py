def parse_line(line):
    reservoirs = [0] * 4
    line = re.sub(r'[,.!?]', '', line)
    words = line.split()
    for i in range(len(words)):
        if words[i] == 'Behaelter' or words[i] == 'Reservoir':
            for x in range(i+1, len(words)):
                if words[x].isdigit():
                    index = int(words[x]) - 1
                    break
            for x in range(i-1, 0, -1):
                if words[x].isdigit():
                    reservoirs[index] = int(words[x])
                    break
    return tuple(reservoirs)