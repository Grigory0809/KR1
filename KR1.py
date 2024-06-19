def filter_short_strings(input_array):

    result_array = []


    for string in input_array:

        if len(string) <= 3:

            result_array.append(string)

    return result_array




input_array = input("Введите строки через пробел: ").split()

filtered_array = filter_short_strings(input_array)


print("Строки длиной <= 3 символов:", filtered_array)