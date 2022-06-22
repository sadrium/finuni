# 1
def fact(x):
    if x > 1:
        return x*fact(x-1)
    else:
        return 1

# 2
def filter_even(li):
    return list(filter(lambda x:x%2==0, li))

# 3
def square(li):
    return list(map(lambda x:x*x, li))

# 4
def bin_search(li, element):
    if element in li:
        return li.index(element)
    else:
        return -1

# 5
def is_palindrome(string):
    l = 0
    r = len(string) - 1
    is_pal = True

    while l < r:
        if not string[l].isalpha():
            l+=1
            continue
        if not string[r].isalpha():
            r-=1
            continue
        if string[l].lower() == string[r].lower():
            l+=1
            r-=1
        else:
            is_pal = False
            break

    return 'YES' if is_pal else 'NO'

# 6
def calculate(path2file):
    operations = {
        '+': lambda x,y:x+y,
        '-': lambda x,y:x-y,
        '*': lambda x,y:x*y,
        '//': lambda x,y:x//y,
        '%': lambda x,y:x%y,
        '**': lambda x,y:x**y,
    }

    with open(path2file, 'r') as f:
        lines = f.readlines()
        res = ''

        for line in range(len(lines)):
            elems = lines[line].split()
            res += str(operations[elems[0]](int(elems[1]), int(elems[2])))
            if line < len(lines)-1:
                if line < len(lines) - 1:
                    res += ','
    return res

# 7
def substring_slice(path2file_1,path2file_2):
    with open(path2file_1, 'r') as f1:
        lines1 = f1.readlines()
        with open(path2file_2, 'r') as f2:
            lines2 = f2.readlines()
            res = ''

            for line in range(len(lines1)):
                string = lines1[line]
                positions = lines2[line].split()

                res += string[int(positions[0]):int(positions[1])+1]
                if line < len(lines1) - 1:
                    res += ' '

    return res

# 8
import json

def decode_ch(string_of_elements):
    periodic_table = json.load(open('periodic_table.json', encoding="utf8"))

    res = ''
    elem = ''
    for i in range(len(string_of_elements)):
        if string_of_elements[i].isupper():
            if i < len(string_of_elements)-1 and string_of_elements[i+1].islower():
                elem = string_of_elements[i]
                continue
            res += periodic_table[string_of_elements[i]]
        elif string_of_elements[i].islower():
            res += periodic_table[elem+string_of_elements[i]]

    return res

print(decode_ch('NOTiFICaTiON'))

# 9
class Student:
    name = ''
    surname = ''
    fullname = ''
    grades = [4,5,5]

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.fullname = name + ' ' + surname

    def __add__(self, other):
        return self.name + ' is friends with ' + other.name

    def __str__(self):
        return self.fullname

    def greeting(self):
        return 'Hello, I am Student'

    def mean_grade(self):
        res = 0
        for i in self.grades:
            res += i

        return res/len(self.grades)

    def is_otlichnik(self):
        if self.mean_grade() >= 4.5:
            return 'YES'
        else:
            return 'NO'

# 10
class MyError(Exception):
    msg = ''

    def __init__(self, msg):
        self.msg = msg