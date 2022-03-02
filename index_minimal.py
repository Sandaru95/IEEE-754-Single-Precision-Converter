def firstDigitZero(string1):
    return (True if string1[0] == '0' else False)
def convert_to_binary_neg(decimal): # F(x) --> Convert Decimal To Binary (Fractional Part)
    binary_string, i = '', 0
    while i != 40:
        if not firstDigitZero(str(decimal * 2)):
            binary_string += str(decimal * 2)[0]
            decimal = float(str(decimal * 2)[1:])
        else:
            binary_string += '0'
            decimal = float(decimal * 2)
        i += 1
    return binary_string
while True:
    print("IEEE 754 Converter. 22/03/02. Author: Sandaru Rasanjana\n");user_input = input("Enter number to convert to IEEE:").strip()
    if float(user_input) == 0:
        print("Enter a number Not equal 0")
    else:
        theres_dot = '.' in user_input
        sign_binary = '1' if not (float(user_input) >= 0) else '0'
        user_input = str(abs(float(user_input)))
        if theres_dot:
            index_of_dot = user_input.index('.')
            user_input_split = [user_input[0:index_of_dot], ("."+user_input[index_of_dot + 1:])]
            binary_number = f"{bin(int(int(user_input_split[0]))).replace('0b', '')}.{convert_to_binary_neg(float(user_input_split[1]))}"
            binary_number_without_dot = binary_number.replace(".", "") # =================================== Getting the index of the DOT
            position_of_dot = str(binary_number).index(".") # ============================================== Getting the 2's Exponent
            split_by_dot_0 = binary_number.split('.')[0]
            split_by_dot_1 = binary_number.split('.')[1] # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
            if '1' in split_by_dot_0:
                pos_first_valued = split_by_dot_0.index('1')
                power_of_2 = position_of_dot - (pos_first_valued + 1)
            else:
                pos_first_valued = split_by_dot_1.index('1')
                power_of_2 = -(((pos_first_valued - position_of_dot)+2))
            print(f"{sign_binary}.{(bin((127+power_of_2)).replace('0b', '')).zfill(8)}.{binary_number_without_dot[1:24]}")
        else:
            binary_number = bin(int(float(str(user_input)))).replace("0b", "")
            exp_of_2 = len(binary_number) - 1
            mantissa = binary_number[1:] # Mantissa Normalization
            if len(mantissa) < 25:
                mantissa = "{:<023s}".format(mantissa)
            print(f"IEEE 754: {sign_binary}.{(bin(int(127+exp_of_2)).replace('0b', '')).zfill(8)}.{mantissa[:23]}")
