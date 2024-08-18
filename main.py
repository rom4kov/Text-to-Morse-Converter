from morse_code import morse_code 

text = list(input("Type text to convert to morse code: ").lower())

morse_code_string = ""

for char in text:
    if char == " ":
        morse_code_string += "   "
    else:
        morse_code_string += morse_code[char] + " "

print(morse_code_string)

