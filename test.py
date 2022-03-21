# A
with open('ex3_text.txt') as f:
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    str_f = str(f.read())
    f_rep = str_f.replace('.', ' ').replace('-', ' ').replace(',', ' ').replace('(', ' ').replace(')', ' ')
    list_f = f_rep.split()
    longest_list = []
    while len(longest_list) < 5:
        max_word = max(list_f, key=len)
        longest_list.append(max_word)
        list_f.remove(max_word)


# B
def read_line(n, file):
    if type(n) is not int:
        return "invalid input detected"
    try:
        f = open(file, 'r')
        lines = []
        for line in f:
            lines.append(line.rstrip())
        if n > len(lines):
            stuff_in_string = "line {} doesn't exist".format(n)
            return stuff_in_string
        else:
            return lines[n - 1]

    except:
        return "file not found"
