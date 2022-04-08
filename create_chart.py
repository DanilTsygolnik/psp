def get_neighbors_ids(cell, chart_height, chart_width):
    cell_height = cell.get_cell_height()
    cell_width = cell.get_cell_width()
    neighbors_ids = set()
    height_modifiers = [-1, 0 , 1]
    width_modifiers = [-1, 0 , 1]
    for h_mod in height_modifiers:
        neighbor_height = cell_height + h_mod
        for w_mod in width_modifiers:
            neighbor_width = cell_width + w_mod
            not_cell_coordinates = (neighbor_height != cell_height) or \
                                   (neighbor_width != cell_width)
            all_parameters_valid = all([neighbor_height >= 1,
                                   neighbor_height <= chart_height,
                                   neighbor_width >= 1,
                                   neighbor_width <= chart_width,
                                   not_cell_coordinates])
            if all_parameters_valid:
                new_id = "".join(["h", str(neighbor_height), "w", str(neighbor_width)])
                neighbors_ids.add(new_id)
    return neighbors_ids
