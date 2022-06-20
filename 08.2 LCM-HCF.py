# This is a simple Calculator which finds out and displays the Least Common Multiple and the Highest Common Factor of the 2 numbers, the user inputs.

#LCM:
def lcm(num1, num2):
    max_num = max(num1, num2) #max_num

    while True:
        if max_num % num1 == 0 and max_num % num2 == 0:
            break

        max_num += 1
    lcm = max_num

    print(f"\nThe LCM of numbers {num1} & {num2} = {lcm}")

#HCF:
def hcf(num1, num2):
    hcf = max(num1, num2)

    while True:
        if num1 % hcf == 0 and num2 % hcf == 0:
            break

        hcf -= 1

    print(f"The HCF of numbers {num1} & {num2} = {hcf}")

def main():
    print("\nEnter the numbers below to find the HCF and LCM:")
    num1 = int(input("\nEnter the first number => ")) #user_input1
    num2 = int(input("Enter the second number => ")) #user_input2

    lcm(num1, num2)
    hcf(num1, num2)
    
    main()

main()