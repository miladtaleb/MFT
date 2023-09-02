# input_string = "alireza,alavi,23,tehran"
def opt_string(s):
    s = input_string.split(",")
    s[2] = int(s[2])
    return s

input_string = input("Please enter your string: ")
res = opt_string(input_string)
print(res)
