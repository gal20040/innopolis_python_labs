from InputReader import InputReader
from OutputWriter import OutputWriter
import Parser


# remove double breakspaces in the string and breakspace(s) in the begining of the string
def remove_redundant_breakspaces(string_curr):
    string_prev = ""
    while string_prev != string_curr:
        string_prev = string_curr
        string_curr = string_curr.replace(' ', '')  # remove all breakspaces in the string

    string_curr = string_curr.replace('q', ' q')  # add one breakspace before each 'q' char
    string_curr = string_curr.replace(' ', '', 1)  # remove one breakspace in the begining of the string

    return string_curr


if __name__ == "__main__":
    input_file_name = "input.txt"
    input_reader = InputReader(input_file_name)
    output_writer = OutputWriter()

    reg_exp = input_reader.read_one_line()
    ndfsa = Parser.reg_exp_parse(reg_exp)

    test_cases_list = input_reader.read_test_cases_from_input_file()

    for j in range(len(test_cases_list)):
        result_string = ""
        result = ndfsa.validate(test_cases_list[j])

        if not result:  # for cases: result = False
            result = ""

        if j != len(test_cases_list) - 1:
            result += "\n"
        result_string += result

        result_string = remove_redundant_breakspaces(result_string)
        output_writer.write_a_string(result_string)

    input_reader = input_reader.close_input_file()
    output_file = output_writer.close_output_file()
