class InputReader(object):
    def __init__(self):
        input_file_name = "input.txt"
        self.input_file = open(input_file_name, 'r')  # 'r' - open for reading

    """read new line from input file and replace unnecessary signs - \n and { and }"""
    def __readline_and_cleanout(self):
        string = self.input_file.readline().replace('\n', '')
        string = string.replace('{', '').replace('}', '')
        return string

    def read_one_line(self):
        return self.input_file.readline().replace('\n', '')

    def read_description_from_input_file(self):
        automaton_description_lines = 5
        description_list = []

        """read the automaton description"""
        for i in range(automaton_description_lines):
            string_description = self.__readline_and_cleanout()
            description_list.append(string_description)

        return description_list

    def read_test_cases_from_input_file(self):
        test_case_number = int(self.__readline_and_cleanout())

        test_cases_list = []
        """read test strings for the automaton"""
        for j in range(test_case_number):
            test_cases_list.append(self.__readline_and_cleanout())

        return test_cases_list

    def close_input_file(self):
        self.input_file.close()
        self.input_file = None
