from Lab12 import get_code_color, convert_code_into_colors, get_code_num, check_guess


def test_get_code_color():
    print("------ get_code_color test ------")
    hidden_code_1 = get_code_color(6, "n")
    print("Should have no repeats: ", hidden_code_1)
    hidden_code_2 = get_code_color(6, "y")
    print("Likely will have repeats: ", hidden_code_2)
    hidden_code_3 = get_code_color(10, "n")
    print("Should be a random combination of all nums 1-10: ", hidden_code_3)
    hidden_code_4 = get_code_color(10, "y")
    print("Should have repeats and only use 1-6: ", hidden_code_4)

def test_convert_code_into_colors():
    print("----- convert_code_into_colors test ------")
    test1 = [5, 4, 3, 3, 2, 6]
    convert_code_into_colors(test1)
    print("Should be [Pink, Yellow, Green, Green, Red, White]: ", test1)
    test2 = [7, 9, 5, 4, 1]
    convert_code_into_colors(test2)
    print("Should be [Black, Brown, Pink, Yellow, Blue]: ", test2)

def test_get_code_num():
    print("------ get_code_num test ------")
    hidden_code_1 = get_code_num(8, "n")
    print("Should have no repeats: ", hidden_code_1)
    hidden_code_2 = get_code_num(9, "y")
    print("Should likely have repeats: ", hidden_code_2)
    
def test_check_guess():
    print("------ check_guess test ------")
    result = check_guess(["5", "3", "2", "8", "4"], [5, 6, 8, 2, 9])
    print("Should be [1, 2]: ", result)
    result = check_guess(["Green", "Blue", "Red", "Yellow", "Purple"], ["Orange", "Blue", "Red", "White"])
    print("Should be Error: ", result)
    result = check_guess(["5", "6", "7", "8"], [5, 6, 7, 8])
    print("Should be [4, 0]: ", result)
    result = check_guess(["Blue", "Blue", "Red", "Red"], ["Green", "Yellow", "Blue", "Red"])
    print("Should be [1, 1]: ", result)

def main():
    test_get_code_color()
    test_convert_code_into_colors()
    test_get_code_num()
    test_check_guess()



main()