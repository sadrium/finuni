# 1.

def fact(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

#2

def filter_even(li):
    return list(filter(lambda x: True if (x % 2) == 0 else False, li))

#3

def square(li):
    return list(map(lambda x: x**2, li))

#4

def bin_search(li, element):
    middle = 0
    start = 0
    step = 0
    end = len(li)

    while (start <= end):
      step = step + 1
      mid = (start + end) // 2

      if element < li[mid]:
        end = mid - 1
      else:
        start = mid + 1
      if element == li[mid]:
      return mid

    return -1

#5

def is_palindrome(string):
    string_rev = ''
    for i in range(len(string) - 1, -1, -1):
      string_rev += string[i]
    if string == string_rev:
      return 'YES'
    else:
      return 'NO'

# 6

def calculate(path2file):
    with open(path2file, 'r', encoding='utf-8') as file:
        to_calc = file.read()
    answer = ''
    to_calc = to_calc.split('    ')
    for each in to_calc:
        each = each.split(' ')
        operation = each[0]
        numbers = [each[1], each[2]]
        try:
            numbers = list(map(int, numbers))
        except:
            if numbers[0][0] == '-':
                numbers[0] = -1 * int(numbers[0][1:])
            if numbers[1][0] == '-':
                numbers[1] = -1 * int(numbers[1][1:])
        if operation == '+':
            answer += str(numbers[0] + numbers[1])
        elif operation == '-':
            answer += str(numbers[0] - numbers[1])
        elif operation == '*':
            answer += str(numbers[0] * numbers[1])
        elif operation == '//':
            answer += str(numbers[0] // numbers[1])
        elif operation == '%':
            answer += str(numbers[0] % numbers[1])
        elif operation == '**':
            answer += str(numbers[0]** numbers[1])
        answer += ' '
    answer = answer[:-1]
    answer = answer.replace(' ', ', ')
    return answer

# 7

def substring_slice(path2file_1,path2file_2):
    with open(path2file_1, 'r', encoding='utf-8') as file:
        strings = file.read()
        strings = strings.split('\n')
    with open(path2file_2, 'r', encoding='utf-8') as file:
        indexes = file.read()
        indexes = indexes.split('\n')
    answer = ''
    for i in range(len(strings)):
        answer += strings[i][int(indexes[i].split(' ')[0]):int(indexes[i].split(' ')[1]) + 1] + ' '
    answer = answer[:-1]
    return answer

#8

def decode_ch(sting_of_elements):
    periodic_table = json.load(open('periodic_table.json'))
    for each in periodic_table:
        if each in sting_of_elements:
            sting_of_elements = sting_of_elements.replace(each, periodic_table[each])
    return sting_of_elements

#9

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

#10

class MyError(Exception):
    msg = ''

    def __init__(self, msg):
        self.msg = msg

