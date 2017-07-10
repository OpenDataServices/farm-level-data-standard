import json
import json_merge_patch
import os
import glob


schema = {}

for file in glob.glob("components/*.JSON") + glob.glob("components/*.json"):
    try:
        with open(file,'r') as schema_file:
            print("Merging "+ file)
            schema_element = json.loads(schema_file.read())
            schema = json_merge_patch.merge(schema, schema_element)
    except Exception:
        print("Problem merging from " + file)
        pass

with open("first-mile-schema.json","w") as outfile:
    outfile.write(json.dumps(schema,indent=2))

print("Full schema in first-mile-schema.json updated")