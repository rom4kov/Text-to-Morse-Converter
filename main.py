from morse_code import morse_code 

text = list(input("Type text to convert to morse code: "))

morse_code_string = ""

for char in text:
    morse_code_string += morse_code[char] + " "

print(morse_code_string)

