def firstDigitZero(string1):
    return (True if string1[0] == '0' else False)
def con_to_bin_fra(decimal): # F(x) --> Convert Decimal To Binary (Fractional Part)
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
print("IEEE 754 Converter. 22/03/02. Author: Sandaru Rasanjana\n")
while True:
    ui = input("Enter number to convert to IEEE:").strip()
    if float(ui) == 0:
        print("Enter a number Not equal 0")
    else:
        theres_dot, sign_binary, ui = ('.' in ui), ('1' if not (float(ui) >= 0) else '0'), (str(abs(float(ui))))
        if theres_dot:
            index_of_dot = ui.index('.')
            ui_split = ([ui[0:index_of_dot], ("."+ui[index_of_dot + 1:])])
            binary_number = (f"{bin(int(int(ui_split[0]))).replace('0b', '')}.{con_to_bin_fra(float(ui_split[1]))}")
            bin_num_wd = binary_number.replace(".", "")
            position_of_dot, split_by_dot_0, split_by_dot_1 = str(binary_number).index("."), binary_number.split('.')[0], binary_number.split('.')[1]
            if '1' in split_by_dot_0:
                power_of_2 = (position_of_dot - (split_by_dot_0.index('1') + 1))
            else:
                power_of_2 = -((((split_by_dot_1.index('1')) - position_of_dot)+2))
            print(f"{sign_binary}.{(bin((127+power_of_2)).replace('0b', '')).zfill(8)}.{bin_num_wd[1:24]}")
        else:
            binary_number = bin(int(float(str(ui)))).replace("0b", "")
            exp_of_2, mantissa = (len(binary_number) - 1), binary_number[1:]
            mantissa = "{:<023s}".format(mantissa)
            print(f"IEEE 754: {sign_binary}.{(bin(int(127+exp_of_2)).replace('0b', '')).zfill(8)}.{mantissa[:23]}")
