string = ""
number = int(input("Choose a number: "))

for x in range(1, (number + 1)):
    if x % 3 == 0:
        string = string + "Fizz "
    if x % 5 == 0:
        string = string + "Buzz "
    if x % 7 == 0:
        string = string + "Quack "
    if x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
        string = string + str(x)

    string = string + "\n"
print(string)
