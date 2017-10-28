
f1 = open(r"C:\Users\mohchaud\PycharmProjects\test\test.txt")

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_line(line_count, f):
    print(line_count, ":", f.readline())

print_all(f1)
rewind(f1)
line_num = 1
print_line(line_num, f1)
line_num += 1
print_line(line_num, f1)
line_num += 1
print_line(line_num, f1)
