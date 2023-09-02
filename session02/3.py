# keys = "name,family,age,location"
# values = "alireza,alavi,23,tehran"

def merge_string(k,v):
    res = {}
    k = k.split(',')
    v = v.split(',')
    res = dict(zip(k,v))
    return res

keys = input("Please enter your title string: ")
values = input("Please enter your value string: ")
res = merge_string(keys,values)
print(res)