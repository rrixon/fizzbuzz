def does_it_divide_exactly(test_number, test_divisor, success_result):
    return success_result if test_number % test_divisor == 0 else ""


def noises_or_numbers(test_string, current_number):
    return test_string if test_string != "" else str(current_number)


number = int(input("Choose a number: "))

for x in range(1, (number + 1)):
    string = ""
    string += does_it_divide_exactly(x, 3, "Fizz ")
    string += does_it_divide_exactly(x, 5, "Buzz ")
    string += does_it_divide_exactly(x, 7, "Quack ")
    print(noises_or_numbers(string, x))
