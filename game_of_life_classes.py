class Cell:

    def __init__(self, height_coord, width_coord):
        self.__cell_id = "".join(["h", str(height_coord), "w", str(width_coord)])
        self.__height_coord = height_coord
        self.__width_coord = width_coord
        self.__is_alive = False 
        self.__neighbors_ids = None
        self.__neighbors = None

    def get_cell_id(self):
        return self.__cell_id

    def get_cell_height(self):
        return self.__height_coord

    def get_cell_width(self):
        return self.__width_coord

    def get_cell_status(self):
        return self.__is_alive

    def get_neighbors_ids(self):
        return self.__neighbors_ids

    def get_neighbors(self):
        return self.__neighbors

    def add_neighbors_ids(self, neighbors_set):
        self.__neighbors_ids = neighbors_set

    def set_cell_status(self, new_status):
        self.__is_alive = new_status

    def add_neighbors(self, neighbors_set):
        self.__neighbors = neighbors_set
