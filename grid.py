import utils
from collections import defaultdict

class Grid:
    def __init__(self, id,height, width, start_long, start_lat):
        self.id = id
        self.start_long = start_long
        self.start_lat = start_lat
        self.end_long = start_long + utils.kmToDegree(height)
        self.end_lat = start_lat + utils.kmToDegree(width)

        self.spatial_attr = defaultdict(int)
        self.temporal_attr = {}

        def __str__(self):
            return "Grid: " + str(self.start_lat)