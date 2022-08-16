import json
import os

faults=os.listdir("statics/fault data") #load all faults geojson file

combine_file={"type":"FeatureCollection","features":[]}
for file in faults:
    with open(f"statics/fault data/{file}") as f:
        data=json.load(f)
        combine_file["features"].append(data["features"][0])
with open("statics/combined_faults.geojson","w") as f:
    json.dump(combine_file,f)
