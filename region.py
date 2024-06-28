import utils
from grid import Grid

GRID_SIZE = utils.GRID_SIZE

class Region:
    def __init__(self, id, start_lat, width, start_long, height):
        self.id = id
        self.start_lat = start_lat
        self.end_lat = start_lat + utils.kmToDegree(width)
        self.start_long = start_long
        self.end_long = start_long + utils.kmToDegree(height)

        self.grids = []
        current_long = self.start_long
        count = 0
        while current_long <= self.end_long:
            current_lat = self.start_lat
            while current_lat <= self.end_lat:
                self.grids.append(Grid(count,GRID_SIZE, GRID_SIZE, current_long, current_lat))
                current_lat += utils.kmToDegree(GRID_SIZE)
                count += 1
            current_long += utils.kmToDegree(GRID_SIZE)

    def __str__(self):
        return "Region: " + str(self.id) + " " + str(self.start_lat) + " " + str(self.end_lat) + " " + str(self.start_long) + " " + str(self.end_long)