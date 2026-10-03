def number(num):

    if num % 2 == 0:
        return "It is even"
    else:
        return "It is odd"


num = int(input("Give any number 1-100: "))

print(number(num))



