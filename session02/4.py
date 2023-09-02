# input_string = """Gott mit uns - metal -
#    Preihelion - psychedelic rock -
#    killer Queen - rock -
#    Primo Victoria - metal -"""

input_string = input("Please enter music strings: ").split('\n')
rock_strings = list(filter(lambda string: 'rock' in string, input_string))
metal_strings = list(filter(lambda string: 'metal' in string, input_string))
print("Count of rock music is:", len(rock_strings),"\n" + "Count of metal music is:",len(metal_strings))