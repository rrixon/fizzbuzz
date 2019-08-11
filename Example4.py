def ask_for_a_number(message):
    return int(input(message))


def does_it_divide_exactly(test_number, test_divisor, success_result):
    return success_result if test_number % test_divisor == 0 else ""


def noises_or_numbers(test_string, current_number):
    return test_string if test_string != "" else str(current_number)


start = ask_for_a_number("Choose a start number: ")
finish = ask_for_a_number("Choose an end number: ")
noises_array = [(3, "Fizz "), (5, "Buzz "), (7, "Quack "), (8, "Moo "), (10, "Splat "), (11, "Kapowee ")]

for x in range(start, (finish + 1)):
    string = ""
    for noise in noises_array:
        string += does_it_divide_exactly(x, noise[0], noise[1])
    print(noises_or_numbers(string, x))
