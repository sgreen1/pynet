#!/usr/bin/env python

import yaml
import json

my_list = [range(9), 'whatever', 'blah', {'key0' : ['blah1', 'blah2', 'blah2'], 'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}]

with open("exercise6-1.yaml", 'w') as f:
    yaml.dump(my_list, f, default_flow_style=False)

with open("exercise6-1.json", 'w') as f2:
    json.dump(my_list, f2)



