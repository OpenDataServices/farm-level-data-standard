import json
import json_merge_patch
import os
import glob
from collections import OrderedDict


schema = {}

for file in glob.glob("components/*.JSON") + glob.glob("components/*.json"):
    try:
        with open(file,'r') as schema_file:
            print("Merging "+ file)
            schema_element = json.loads(schema_file.read(),object_pairs_hook=OrderedDict)
            schema = json_merge_patch.merge(schema, schema_element)
    except Exception:
        print("Problem merging from " + file)
        pass

with open("first-mile-farm-data-schema.json","w") as outfile:
    outfile.write(json.dumps(schema,indent=2))

print("Full schema in first-mile-farm-data-schema.json updated")
