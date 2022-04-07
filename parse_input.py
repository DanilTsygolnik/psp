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
