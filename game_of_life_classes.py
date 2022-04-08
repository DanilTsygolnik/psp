class Cell:

    def __init__(self, cell_id, height_coord, width_coord, status, neighbors_ids):
        self.__cell_id = cell_id
        self.__height_coord = height_coord
        self.__width_coord = width_coord
        self.__is_alive = status
        self.__neighbors_ids = neighbors_ids
        self.__neighbors = None

    def get_cell_height(self):
        return self.__height_coord

    def get_cell_width(self):
        return self.__width_coord

    def set_cell_status(new_status):
        self.__is_alive = new_status

    def add_neighbors(neighbors_set):
        self.__neighbors = neighbors_set
