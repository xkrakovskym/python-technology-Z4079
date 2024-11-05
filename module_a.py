import dis

import flask

test = "nejaky string"

def find_index(to_search, target):
    for index, value in enumerate(to_search):
        if value == target:
            return index
    return -1

dis.dis(find_index)