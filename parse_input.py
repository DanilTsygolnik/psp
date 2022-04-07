def get_chart_sizes(input_file):
    with open(input_file, "r", encoding="utf-8") as file:
        string_index = 0
        for string in file:
            if string_index == 1:
                string_with_sizes = string
                separated_sizes = string_with_sizes.split()
                height = int(separated_sizes[0])
                width = int(separated_sizes[1])
                chart_parameters = {}
                chart_parameters["height"] = height
                chart_parameters["width"] = width
                return chart_parameters
            string_index += 1
    return 0

def search_alive_in_string(string_num, string):
    alive_cells_ids = []
    char_num = 1
    for char in string:
        if char == "*":
            new_id = "".join(["h", str(string_num), "w", str(char_num)])
            alive_cells_ids.append(new_id)
        char_num += 1
    return alive_cells_ids

def get_alive_cells_ids(chart_parameters, input_file):
    wrong_input_type = not isinstance(chart_parameters, type({}))
    if wrong_input_type:
        raise TypeError

    alive_cells_ids = []
    with open(input_file, "r", encoding="utf-8") as file:
        string_index = 0
        for string in file:
            if string_index >= 2:
                string_num = string_index - 1
                current_string_ids = search_alive_in_string(string_num, string)
                alive_cells_ids += current_string_ids
            string_index += 1
    chart_parameters['alive_cells_ids'] = alive_cells_ids
    return chart_parameters
