#!/usr/bin/python3

def read_data(filename):
    with open(filename,'r') as input_file:
        first_line = True
        substring = ""
        strings = []
        for line in input_file:
            if first_line:
                substring = line.rstrip()
                first_line = False
            else:
                strings.append(line.rstrip())

    input_file.close()
    return [substring,strings]

def save_data(filename, lines):
    f = open(filename, "w")
    for line_iter in range(0,len(lines)):
        f.writelines(lines[line_iter])
        if line_iter < len(lines)-1:
            f.writelines('\n')
    f.close()
    return 0

def count_substrings(substring,strings):
    data_lines = []
    for string in strings:
        non_overlap_count = string.count(substring)
        overlap_count = 0
        found = 0
        lastfound = -1
        while (found != -1):
            found = string.find(substring, lastfound+1, len(string))
            if (found != -1):
                lastfound = found
                overlap_count+=1
        data_lines.append(str(overlap_count)+" "+str(non_overlap_count))
    return data_lines

[substring, strings] = read_data("String.inp")
data = count_substrings(substring,strings)
print(data)
save_data("String.out", data)