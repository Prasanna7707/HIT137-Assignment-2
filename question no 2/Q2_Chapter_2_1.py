def string_convert(input_string):
    numbers = ''.join(filter(str.isdigit, input_string))
    letters = ''.join(filter(str.isalpha, input_string))
    
    even_numbers = [int(n) for n in numbers if int(n) % 2 == 0]
    even_numbers_ascii = [ord(str(n)) for n in even_numbers]

    uppercase_letters = [l for l in letters if l.isupper()]
    uppercase_letters_ascii = [ord(l) for l in uppercase_letters]
    
    
    print(numbers)
    print(letters)
    print(even_numbers)
    print(even_numbers_ascii)
    print(uppercase_letters)
    print(uppercase_letters_ascii)

    return numbers, letters, even_numbers, even_numbers_ascii, uppercase_letters, uppercase_letters_ascii

input_string = "56aAww1984sktr235270aYmn145ss785fsq31D0"

string_convert(input_string)
