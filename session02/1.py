def calculate(s):
    res = 0
    if ('+' in s):
        a,b = s.split('+')
        res = int(a)+int(b)
    elif ('-' in s):
        a,b = s.split('-')
        res = int(a)-int(b)
    elif ('*' in s):
        a,b = s.split('*')
        res = int(a)*int(b)
    elif ('/' in s):
        a,b = s.split('/')
        res = int(a)/int(b)
    else:
        res = "your input is wrong"
    return res

input_string = input("Please enter your stering: ")
print("Result is:",calculate(input_string))
