#!/usr/bin/env python

from collections import OrderedDict
from functools import reduce
from ruamel.yaml import YAML
import argparse
import json
import operator
import sys

def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)

def setInDict(dataDict, mapList, value):
    getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value

# read json from file and return nested list
def readJsonFromFile(jsonFile):
    with open(jsonFile) as json_file:
        try:
            data = json.load(json_file)
            data = OrderedDict(sorted(data.items()))
        except Exception as e:
            print(repr(e))
            sys.exit(1)

    nestedList = []

    for el in data:
        templ = []
        for v in el.split('.'):
            # append nested keys as list elements to temp list
            templ.append(v)
        
        # last list element is value, append value to temp list
        templ.append(data[el])

        # add to list
        nestedList.append(templ)

    return nestedList

# from nested list generate structured nested dictionary with data
def genData(l, d):
    for path in l:
        current_level = d

        # last element in list is value
        #  we don't need it rigth now to create nested map
        for part in path[:-1]:
            if part not in current_level:
                current_level[part] = {}

            current_level = current_level[part]

    # iterate creted nested dictionary and set values from list
    for path in l:
        setInDict(d, path[:-1], path[-1])

def genYamlFile(outFile):
    yaml = YAML()
    yaml.explicit_start = True
    with open(outFile, "w") as fp:
        yaml.dump(dataDict, fp)


if __name__ == '__main__':
    dataDict = {}

    parser = argparse.ArgumentParser(
        description='Convert JSON to formatted YAML')
    parser.add_argument('input', type=argparse.FileType('r'), 
        help='inuput JSON file')
    parser.add_argument('output', type=argparse.FileType('w'),
        help='output YAML file')
    args = parser.parse_args()

    genData(readJsonFromFile(args.input.name), dataDict)
    genYamlFile(args.output.name)
