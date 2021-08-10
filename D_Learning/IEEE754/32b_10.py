##--------------------------------------------------------------##
## This program is made to demonstrate conversion of number 
## between IEEE754 32-bit single precision and decimal number
## @Author: <Phichayut N.>
##--------------------------------------------------------------##
import time
import math

def thing_to_dec():
    print("\nThe input of the binary will be splitted automatically")
    input_val = input("Please provide the 32-bit Number \n>>> ")
    if len(input_val) == 32 and input_val.isdecimal():
        sign = input_val[0]
        sign_expo = input_val[1]
        bin_exponent = input_val[1:9]
        mantissa = input_val[9:32]
        print(f"\nThe Number is splitted into: \n>>Sign bit: {sign} \n>>exponential bit: {bin_exponent} \n>>Mantissa: {mantissa}")

        print("###################################################")
        print(f"Converting binary exponential: {bin_exponent} to Decimal")
        dec_exponent = 0
        ex = 7
        for n in bin_exponent:
            if n == "1":
                dec_exponent += 2 ** ex
                print(f"At exponent step {ex} the bit is {n}: 2 powered by {ex}         >>> {dec_exponent}")
            elif n == "0":
                print(f"At exponent step {ex} the bit is {n}: will skip the exponent >>> {dec_exponent}")
            ex -= 1
        print(f"The exponential number is {dec_exponent} (Normalized = {dec_exponent - 127})")

        print("###################################################")
        print(f"Converting binary mantissa: {mantissa} to decimal")
        dec_mantissa = 0
        ex = -1
        for i in mantissa:
            if i =="1":
                dec_mantissa += 2 ** ex
                print(f"At exponent step {ex} the bit is {i}: 2 powered by {ex}         >>> {dec_mantissa}")
            elif i == "0":
                print(f"At exponent step {ex} the bit is {i}: will skip the exponent >>> {dec_mantissa}")
            ex -= 1
        dec_mantissa += 1
        print(f"The mantissa number is {dec_mantissa}")
        print("###################################################")
        
        if sign == "0": shitty = 1
        elif sign == "1": shitty = -1

        final = shitty * (dec_mantissa) * (2 ** (dec_exponent - 127))
        print(f"The final answer is: (-1 ^ {sign}) x {dec_mantissa} x 2 ^ ({dec_exponent} -127)")
        print(f"The final answer is: {final}")
    else:
        print("Invalid format!")
    pass

def dec_to_thing():
    print("\nThe input of the decimal will be splitted automatically")
    input_val = input("Please provide the decimal Number \n>>> ")

    sign_bit = 0

    if float(input_val) > 0:
        sign_bit = 0
        print(f"The value is positive, sign bit will be: {sign_bit}")
    else: 
        sign_bit = 1
        input_val = input_val[1::]
        print(f"The value is negative, sign bit will be: {sign_bit}")

    exponent = math.log(float(input_val)) / math.log(2)
    expo_bin = "{0:b}".format(127 + int(exponent))
    print(f"Exponent will be calculated from: log({input_val}) / log(2)")
    print(f"Exponent result is: {int(exponent)}")
    print(f"Exponent binary is: {expo_bin}")

    dec_mantissa = (float(input_val) / (2 ** int(exponent))) - 1
    print(f"Mantissa will be calculated from: {input_val} / (2 ^ {int(exponent)})")
    print(f"Mantissa decima is: {dec_mantissa} (1 is removed)")
    mantissa = ""

    for n in range(24):
        print(dec_mantissa, " x 2 >>", end = " ")
        dec_mantissa *= 2
        print(dec_mantissa,">>", end = " ")
        if dec_mantissa < 1:
            mantissa += "0"
        elif dec_mantissa >= 1:
            mantissa += "1"
            dec_mantissa -= 1
        elif dec_mantissa == 0:
            mantissa += ("0" * (24 - n))
        print(mantissa)

    print(f"Final mantissa : {mantissa} [{len(mantissa)}]")

    print(f"Final Answer is >>> {str(sign_bit) + expo_bin + mantissa}")


def main():
    x = True

    print("IEEE754 32-bit single precision and decimal number converter (Step by step)")

    # Prompting start of the program
    while(x):
        choice = input("\nDecimal to IEEE754, please type: A \nIEEE754 to Decimal, please type: B \nTo Exit try: Q \n>>> ")

        if   choice == "A" or choice == "a":
            dec_to_thing()
        elif choice == "B" or choice == "b":
            thing_to_dec()
        elif choice == "Q" or choice == "q":
            print("Bye!")
            time.sleep(1)
            quit()
        else:
            print(">>> READ PROPERLY, I DID NOT STUTTER! <<<")
            time.sleep(1)
        
if __name__ == "__main__":
    #main()
    thing_to_dec()
    #dec_to_thing()