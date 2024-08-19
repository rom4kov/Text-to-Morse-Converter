from morse_code import morse_code 


class MorseConverter():
    def __init__(self) -> None:
        self.operation = input("Type e to encode text to morse or d to decode morse to text: ")
        self.op_choice()
        
    def op_choice(self):
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
                pass
        print(morse_code_string)


    def decode(self):
        pass


