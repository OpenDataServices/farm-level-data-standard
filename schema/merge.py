import json
import json_merge_patch
import os
import glob
from collections import OrderedDict
from flattentool import create_template, unflatten, flatten

schema = OrderedDict()

for file in glob.glob("firstmilefarmdataframe/*.json") + glob.glob("components/*.json"):
    try:
        with open(file,'r') as schema_file:
            print("Merging "+ file)
            schema_element = json.loads(schema_file.read(),object_pairs_hook=OrderedDict)
            schema = json_merge_patch.merge(schema, schema_element,position='last')
    except Exception:
        print("Problem merging from " + file)
        pass

with open("first-mile-farm-data-schema.json","w") as outfile:
    outfile.write(json.dumps(schema,indent=2))

create_template(schema="first-mile-farm-data-schema.json",output_name="../csv",output_format='csv')


print("Full schema in first-mile-farm-data-schema.json updated")

for file in glob.glob("marsadoptionobservations/*.json") + glob.glob("components/*.json"):
    try:
        with open(file,'r') as schema_file:
            print("Merging "+ file)
            schema_element = json.loads(schema_file.read(),object_pairs_hook=OrderedDict)
            schema = json_merge_patch.merge(schema, schema_element,position='last')
    except Exception:
        print("Problem merging from " + file)
        pass

with open("first-mile marsadoptionobservations.json","w") as outfile:
    outfile.write(json.dumps(schema,indent=2))

create_template(schema="first-mile marsadoptionobservations.json",output_name="../csv",output_format='csv')


print("Full schema in first-mile marsadoptionobservations.json updated")
