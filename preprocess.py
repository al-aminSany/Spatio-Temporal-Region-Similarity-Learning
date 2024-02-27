import utils
from region import Region
import json
from datetime import datetime
import matplotlib.pyplot as plt

USER_ID = 0
POI_ID = 1
POI_CATEGORY_ID = 2
POI_CATEGORY_NAME = 3
LATITUDE = 4
LONGITUDE = 5
TIMEZONE_OFFSET = 6
UTC_TIME = 7

REGION_HEIGHT = 3 # 640m-3km
REGION_WIDTH = 3


with open('./data/NYC_test.txt', 'r', encoding='latin') as file:
    lines = file.readlines()

latitude_values = [float(line.split('\t')[LATITUDE]) for line in lines]
longitude_values = [float(line.split('\t')[LONGITUDE]) for line in lines]

category_count = len(set([line.split('\t')[POI_CATEGORY_ID] for line in lines]))
# print(category_count)


# spatial params
max_latitude = max(latitude_values)
min_latitude = min(latitude_values)
max_longitude = max(longitude_values)
min_longitude = min(longitude_values)


print(max_latitude, min_latitude)
print(max_longitude, min_longitude)

distance_x = abs(utils.degreeToKm(float(max_latitude) - float(min_latitude)))
distance_y = abs(utils.degreeToKm(float(max_longitude) - float(min_longitude)))
# 1 degree latitude = 111.32 km

# print(distance_x, distance_y)

regions = []
id = 0

current_long = min_longitude
while current_long < max_longitude:
    current_lat = min_latitude
    while current_lat < max_latitude:
        regions.append(Region(id, current_lat, REGION_WIDTH, current_long, REGION_HEIGHT))
        # if id == 2125 :
        #     print(regions[id])
        #     break
        id += 1
        current_lat += utils.kmToDegree(REGION_WIDTH)
    current_long += utils.kmToDegree(REGION_HEIGHT)


# print(len(regions))
# print(regions[0])

with open('./data/foursquare_taxonomy.json', 'r') as file:
    category_data = json.load(file)
    

lineCount = 0
for line in lines:
    lat = float(line.split('\t')[LATITUDE])
    long = float(line.split('\t')[LONGITUDE])
    ids = utils.getRegionAndGridId(lat, long, max_latitude, min_latitude, min_longitude, REGION_HEIGHT, REGION_WIDTH, regions)

    category = line.split('\t')[POI_CATEGORY_NAME]
    # print(lineCount, category)
    parent_category = category_data[category]

    # print(parent_category, regions[ids['region_id']].grids[ids['grid_id']].spatial_attr[parent_category])

    regions[ids['region_id']].grids[ids['grid_id']].spatial_attr[parent_category] += 1
    lineCount += 1
    # print(parent_category)

    # print(regions[ids['region_id']].grids[ids['grid_id']])
    # print(ids["grid_id"])

count = 0
total = 0
for region in regions:
    for grid in region.grids:
        if len(grid.spatial_attr) > 0:
            count+=1
        total+=1
        print(grid.spatial_attr)
    print("--------------------------------------\n\n")

print(count, total)
print(count/total)


    






