import random


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

GRID_SIZE = 1

def kmToDegree(km):
    return float(km/111.32)

def degreeToKm(degree):
    return float(degree*111.32)

def getRegionAndGridId(lat, long, max_lat,  min_lat, min_long, region_height, region_width, regions):
    offset_x = int(degreeToKm(abs(lat - min_lat)) / region_width)
    offset_y = int(degreeToKm(abs(long - min_long)) / region_height)
    delta = degreeToKm(abs(max_lat - min_lat)) / region_width
    row_size = int(delta) + (delta-int(delta) > 1e-6)

    region_id = offset_x + offset_y * row_size
    
    grid_offset_x = int(degreeToKm(abs(lat - regions[region_id].start_lat)) / GRID_SIZE)
    grid_offset_y = int(degreeToKm(abs(long - regions[region_id].start_long)) / GRID_SIZE)
    grid_delta = degreeToKm(abs(regions[region_id].end_lat - regions[region_id].start_lat)) / GRID_SIZE 
    grid_row_size = int(grid_delta) + (grid_delta-int(grid_delta) > 1e-6)

    # print(lat - regions[region_id].start_lat)

    grid_id = grid_offset_x + grid_offset_y * grid_row_size

    return {"region_id": region_id, "grid_id": grid_id}

def get_category_set(category_data):
    categories = set()
    for attr, val in category_data.items():
        categories.add(val)

    return categories
 
def addNoise(regions, shift, noise, categories):

    for region in regions:
        for grid in region.grids:

            delta_noise = int(noise * len(grid.spatial_attr))
            update_count = random.randint(int(delta_noise/2), delta_noise)

            i = 0
            while (i < update_count):
                remove_random_key = random.choice(list(grid.spatial_attr.keys()))
                random_category = random.choice(list(categories))
                grid.spatial_attr[random_category] = grid.spatial_attr.pop(remove_random_key)
                i += 1

                if random.randint(0, 10) > 4:
                    # push a random but not the removed key
                    random_category = random.choice(list(categories))
                    grid.spatial_attr[random_category] = 3
                    



                

            
    
 
                