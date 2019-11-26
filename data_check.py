import json
import re

import pandas as pd

with open('20191116_wawa.json', 'r') as file:
    data = json.load(file)

data_clean = []

raw_any_num = re.compile(r"(\d+,\d+) m|\d+ m")
raw_number = re.compile(r"\d+")
raw_inside_strong = re.compile(r"<strong>(\w+|\w+\s\w+)</strong>")
raw_inside_strong_prop = re.compile(r"<strong>(...+)</strong>")
raw_district = re.compile(r".*?,\s*(w*?)(...+)")

for record in data:

    #Cleaning the title data
    title_clean = record["title"]

    #Cleaning the district data
    district = record["district"]


    #Cleaning the prices data
    price = record["price"].strip(" zł").replace(" ", "").replace(",", ".")
    if price == "Zapytajocenę":
         price_clean = None
    elif price.endswith("€"):
         price_clean = float(price.strip("€")) * 4.288
    else:
         price_clean = float(price)

    #Clean the rent data
    rent = list(filter(re.compile(r"Czynsz: <strong>").search, record["bag"]))
    if (len(rent) < 1) or (rent is None):
        rent_clean = None
    else:
        rent_clean = (float(raw_number.search(rent[-1]).group().strip(" zł").replace(",", ".")))


    #Clean the area data
    area = list(filter(re.compile(r"Powierzchnia: <strong>").search, record["bag"]))
    if (len(area) < 1) or (area is None):
        area_clean = None
    else:
        area_clean = (float(raw_any_num.search(area[-1]).group().strip(" m").replace(",", ".")))

    #Clean the room data
    chamber = list(filter(re.compile(r"Liczba pokoi: <strong>").search, record["bag"]))
    if (len(chamber) < 1) or (chamber is None):
        chamber_clean = None
    else:
        chamber_clean = int(raw_number.search(chamber[-1]).group())

    #Clean the market data
    market = list(filter(re.compile(r"Rynek: <strong>").search, record["bag"]))
    if (len(market) < 1) or (market is None):
        market_clean = None
    else:
       market_clean = raw_inside_strong.search(market[-1]).group(1)

    #Clean the building type data
    building = list(filter(re.compile(r"Rodzaj zabudowy: <strong>").search, record["bag"]))
    if (len(building) < 1) or (building is None):
        building_clean = None
    else:
        building_clean = raw_inside_strong.search(building[-1]).group(1)

    #Clean the floor data
    floor = list(filter(re.compile(r"Piętro: <strong>").search, record["bag"]))
    if (len(floor) < 1) or (floor is None) or ("poddasze" in floor[0]):
        floor_clean = None
    else:
        if "&gt;" in floor[0]:
            floor_clean = 11
        elif "parter" in floor[0]:
            floor_clean = 0
        elif "suterena" in floor[0]:
            floor_clean = 0
        else:
            floor_clean = int(raw_inside_strong.search(floor[-1]).group(1))

    #Clean the building floor number data
    building_floors = list(filter(re.compile(r"Liczba pięter: <strong>").search, record["bag"]))
    if (len(building_floors) < 1) or (building_floors is None):
        building_floors_clean = None
    else:
        building_floors_clean = int(raw_inside_strong.search(building_floors[-1]).group(1))

    #Clean the construction year data
    construction_year = list(filter(re.compile(r"Rok budowy: <strong>").search, record["bag"]))
    if (len(construction_year) < 1) or (construction_year is None):
        construction_year_clean = None
    else:
        construction_year_clean = int(raw_inside_strong.search(construction_year[-1]).group(1))

    #Clean the standard data
    standard = list(filter(re.compile(r"Stan wykończenia: <strong>").search, record["bag"]))
    if (len(standard) < 1) or (standard is None):
        standard_clean = None
    else:
        standard_clean = raw_inside_strong.search(standard[-1]).group(1)

    #Clean the property data
    property = list(filter(re.compile(r"Forma własności: <strong>").search, record["bag"]))
    if (len(property) < 1) or (property is None):
        property_clean = None
    else:
        property_clean = raw_inside_strong_prop.search(property[-1]).group(1)

    #Clean the window data
    window = list(filter(re.compile(r"Okna: <strong>").search, record["bag"]))
    if (len(window) < 1) or (window is None):
        window_clean = None
    else:
        window_clean = raw_inside_strong.search(window[-1]).group(1)

    #Clean the heating data
    heating = list(filter(re.compile(r"Ogrzewanie: <strong>").search, record["bag"]))
    if (len(heating) < 1) or (heating is None):
        heating_clean = None
    else:
        heating_clean = raw_inside_strong.search(heating[-1]).group(1)



    #Colect the data
    item = {
    "district": district,
    "area": area_clean,
    "chamber": chamber_clean,
    "market": market_clean,
    "building": building_clean,
    "floor": floor_clean,
    "building_floors": building_floors_clean,
    "construction_year": construction_year_clean,
    "standard": standard_clean,
    "property": property_clean,
    "window": window_clean,
    "heating": heating_clean,
    "url": record["url"],
    "rent": rent_clean,
    "price": price_clean,
    }

    data_clean.append(item)

clean_df = pd.DataFrame(data_clean)

clean_df.to_csv(f"20191117_data_clean_wawa.csv", index=False)

print("Processing task finished")
