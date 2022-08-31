# Basic Calculator
num1 = float(input("Number 1: "))
op = input('Operation:')
num2 = float(input("Number 2:"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else: print("Invalid operation.")

# Exponential Function

num1 = int(input("Number1:"))
num2 = int(input("Number2:"))

def raise_to_power(base_no, power_no):                         # It will multiply the base number with itself as many times as power number is mentioned.
    output = 1
    for index in range(power_no):
        output = output * base_no
    return output

print(raise_to_power(num1, num2))
# Other ways of getting the power of any number.
result = num1 ** num2
print(result)
print(pow(num1, num2))
