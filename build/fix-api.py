import json

fh = open("cloudendure-api.json")
j_data = json.load(fh)

##
##  Since the CE def is swagger 2.0, we can't use any kind of oneOf for the volume
## encryption keys.  Nothing will work via the json, so we'll have to fix the code.
##
# get rid of incorrect definition, and replace with correct one
# del j_data["definitions"]["Region"]["properties"]["volumeEncryptionKeys"]["items"][
#     "type"
# ]
# j_data["definitions"]["Region"]["properties"]["volumeEncryptionKeys"]["items"][
#     "oneOf"
# ] = [
#     {"type": "string"},
#     {"type": "object"},
# ]
# j_data["definitions"]["Region"]["properties"]["volumeEncryptionKeys"]["items"][
#    "AnyValue"
# ] = {}
# j_data["definitions"]["Region"]["properties"]["volumeEncryptionKeys"]["items"][

# write correct api json
with open("cloudendure-api-fixed.json", "w") as outfile:
    json.dump(j_data, outfile)
