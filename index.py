def firstDigitZero(string1): # F(x) --> if the first digit is Zero
    returnVal = True
    if string1[0] != '0':
        returnVal = False
    return returnVal
def makeIt8Bit(string1): # F(x) --> Given String returns with length 0 (adding 0s in front)
    missingBits = 8 - len(string1)
    for i in range(0, missingBits):
        string1 = '0' + string1
    
    return string1
def convert_to_binary_pos(decimal): # F(x) --> Convert Decimal To Binary (Non-Fractional Part)
    # Placeholders
    binary_string = ''
    while decimal != 0:
        if decimal % 2 == 0:
            binary_string += '0'
            decimal = decimal / 2
        else:
            binary_string += '1'
            decimal = (decimal - 1) / 2
    if len(binary_string) == 0:
        binary_string = '0'
    return binary_string[::-1]
def convert_to_binary_neg(decimal): # F(x) --> Convert Decimal To Binary (Fractional Part)
    # Placeholders
    binary_string = ''
    i = 0
    while i != 40:
        if not firstDigitZero(str(decimal * 2)):
            binary_string += str(decimal * 2)[0]
            decimal = float(str(decimal * 2)[1:])
        else:
            binary_string += '0'
            decimal = float(decimal * 2)
        i += 1
    return binary_string
""" !========================================================== The Programme Starts Here !==========================================================>"""
print("IEEE 754 Converter. 22/03/01. Author: Sandaru Rasanjana")
print("Input Number to Convert & 'q' to Quit.\n")
while True:
    user_input = input("Enter number to convert to IEEE:").strip()
    # ERROR CHECKING GETTING A VALID NUMBER TO CONVERT
    if user_input != "q":
        try:
            float(user_input)
        except:
            print("Please Enter a Valid Number")
            break
        finally: 
            pass
    if user_input == "q":
        print("Quitting!")
        break
    elif float(user_input) == 0:
        print("Enter a number Not equal 0")
    else:
        # Error Checking Finished
        theres_dot = '.' in user_input
        # Getting the Sign Binary
        input_is_positive = float(user_input) >= 0
        sign_binary = '0'
        if not input_is_positive:
            sign_binary = '1'
        user_input = str(abs(float(user_input)))
        # Splitting By Dot If EXIST
        if theres_dot:
            index_of_dot = user_input.index('.')

        if theres_dot:
            # Splitting the Input into 2 BY DOT
            user_input_split = [user_input[0:index_of_dot], ("."+user_input[index_of_dot + 1:])]
            # Calculating the binary number
            binary_number = f"{convert_to_binary_pos(float(user_input_split[0]))}.{convert_to_binary_neg(float(user_input_split[1]))}"
            binary_number_without_dot = binary_number.replace(".", "")
            # ============================================== Getting the index of the DOT
            position_of_dot = str(binary_number).index(".")
            # ============================================== Getting the 2's Exponent
            split_by_dot_0 = binary_number.split('.')[0]
            split_by_dot_1 = binary_number.split('.')[1]
            # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
            if '1' in split_by_dot_0:
                pos_first_valued = split_by_dot_0.index('1')
                power_of_2 = position_of_dot - (pos_first_valued + 1)
            else:
                # print(binary_number)
                pos_first_valued = split_by_dot_1.index('1')
                # print({pos_first_valued})
                power_of_2 = -(((pos_first_valued - position_of_dot)+2))
                # print({power_of_2})
            # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
            # if pos_first_valued <= position_of_dot:
            # else:
            # Out
            # print(127+power_of_2)
            # print(convert_to_binary_pos((127+power_of_2)))
            print(f"{sign_binary}.{makeIt8Bit(convert_to_binary_pos(127+power_of_2))}.{binary_number_without_dot[1:24]}")
        else:
            binary_number = (convert_to_binary_pos(float(user_input)))
            exp_of_2 = len(binary_number) - 1
            # Mantissa Normalization
            mantissa = binary_number[1:]
            if len(mantissa) < 25:
                i = len(mantissa)
                while i != 25:
                    mantissa += '0'
                    i += 1
            # Out
            print(f"IEEE 754: {sign_binary}.{makeIt8Bit(convert_to_binary_pos(127+exp_of_2))}.{mantissa[:23]}")