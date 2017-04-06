#!/usr/bin/env python

from sys import argv
from pprint import pprint as pp
from ciscoconfparse import CiscoConfParse

script, arg = argv

#print("Script name is %s" % script)

#print("First variable is %s" % arg)

#print("Second variable is %s" % second)


#f = open(arg, 'r')

#dump = f.readlines()

ciscocfg = CiscoConfParse(arg)

helper_ints = ciscocfg.find_objects_w_child(parentspec=r"^interf", childspec="ip helper")

for helper in helper_ints:
    print helper.text
