"""
This script load the bible data base, extract gospels and write them respective files 
"""

import json


def load_json(file_name):
    """
    Load the json file to a json object
    """
    return json.load(open(file_name))


def list_to_json(input_list, file_name):
    """
    Dump an input list as a json file
    """
    with open(file_name, 'w') as outfile:
        json.dump(input_list, outfile)


def extract_verses(start_index, stop_index, list_of_verse):
    """
    Extract the verses between start_index and stop_index (not included)
    List of verse is a list of dictionaries with key as field and values as verse 
    Output will be a list of list with chapter number, verse number and verses 
    """
    res_list = []
    for _, verse in enumerate(list_of_verse):
        if verse["field"][0] >= start_index and verse["field"][0] < stop_index:
            res_list.append(verse["field"])
    return res_list


VERSION = "ylt"
INPUT_FILE = "../bible_database/t_" + VERSION + ".json"
OUTPUT_FOLDER = "../raw_gospel_data/"+ VERSION + "/"
EXTENSION = "_" + VERSION + ".json"

if __name__ == "__main__":
    bible = load_json(INPUT_FILE)
    list_of_verse = bible["resultset"]["row"]
    matthew = extract_verses(40001001, 41001001, list_of_verse)
    mark = extract_verses(41001001, 42001001, list_of_verse)
    luke = extract_verses(42001001, 43001001, list_of_verse)
    john = extract_verses(43001001, 44001001, list_of_verse)
    list_to_json(matthew, OUTPUT_FOLDER + "matthew" + EXTENSION)
    list_to_json(mark, OUTPUT_FOLDER + "mark" + EXTENSION)
    list_to_json(luke, OUTPUT_FOLDER + "luke" + EXTENSION)
    list_to_json(john,  OUTPUT_FOLDER + "john" + EXTENSION)