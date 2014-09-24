import json
from pprint import pprint
with open('velib.json', 'r') as vfile:
    vdata = json.load(vfile)
pprint(vdata)
