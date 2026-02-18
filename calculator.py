print("Simple Calculator")

num1 = float(input("Birinci ədədi daxil edin: "))
operator = input("Operatoru daxil edin (+, -, *, /): ")
num2 = float(input("İkinci ədədi daxil edin: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "0-a bölmək olmaz!"
else:
    result = "Yanlış operator!"

print("Nəticə:", result)