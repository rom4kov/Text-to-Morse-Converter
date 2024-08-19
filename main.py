from morse_code import morse_code 


class MorseConverter():
    def __init__(self) -> None:
        self.operation = ""
        self.op_choice()
        
    def op_choice(self):
        while self.operation != "e" and self.operation != "d":
            self.operation = input("Type 'e' to encode text to morse or 'd' to decode morse to text: ")
        if self.operation == "e":
            self.encode()
        elif self.operation == "d":
            self.decode()

    def encode(self):
        morse_code_string = ""
        text = list(input("Type text to convert to morse code: ").lower())

        for char in text:
            if char == " ":
                morse_code_string += "   "
            else:
                morse_code_string += morse_code[char] + " "
        print(morse_code_string)

    def decode(self):
        reverse_morse_code = {value: key for key, value in morse_code.items()}

        plain_text_string = ""
        morse_words = input("Please provide morse code to decode to text: ").split("   ")

        for word in morse_words: 
            morse_letters = word.split()
                    
            text_word = ''.join(reverse_morse_code[letter] for letter in morse_letters)
            plain_text_string += text_word + " "

        print(plain_text_string)

morse_converter = MorseConverter()

