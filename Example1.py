def does_it_divide_exactly(test_number, test_divisor, success_result):
    return success_result if test_number % test_divisor == 0 else ""


string = ""
number = int(input("Choose a number: "))

for x in range (1, (number + 1)):
    string += does_it_divide_exactly(x, 3, "Fizz ")
    string += does_it_divide_exactly(x, 5, "Buzz ")
    string += does_it_divide_exactly(x, 7, "Quack ")
    if x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
        string = string + str(x)

    string = string + "\n"
print(string)
