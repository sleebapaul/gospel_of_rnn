"""
This script will help us to generate training data from raw gospel data
"""

import json
import spacy
import os
nlp = spacy.load("en_core_web_md")


def load_json(file_name):
    """
    Load the json file to a json object
    """
    return json.load(open(file_name))


def tokenize_sentence(input_sentence, spacy_object):
    """
    Tokenize a give sentence and return tokens as a list
    """
    return [token.text for token in spacy_object(input_sentence)]


def generate_training_data(raw_data, spacy_object):
    """
    Tokenize, add structure tokens <SOV>, <EOV>, <SOC>, <EOC> 
    Returns a single string with tokens seperated by space

    verse_data[4] = Verse ID
    verse_data[2] = Book ID
    verse_data[2] = Chapter NUmber
    verse_data[3] = Verse Number
    verse_data[4] = Verse string

    """

    training_data = ""
    chapter_number = 1
    chapter_start = 1

    for i, verse_data in enumerate(raw_data):
        tokens = tokenize_sentence(verse_data[4], spacy_object)
        temp = ["<SOV>"] + tokens + ["<EOV>"]
        if chapter_number == verse_data[2] and chapter_start == verse_data[3]:
            temp = ["<SOC>"] + temp
        elif i+1 < len(raw_data) and raw_data[i+1][2] == chapter_number+1:
            temp = temp + ["<EOC>"]
            chapter_number += 1
        elif i+1 == len(raw_data):
            temp = temp + ["<EOC>"]
        temp = " ".join(temp)
        training_data = training_data + temp + " "
    return training_data


# Change the version to generate training data for files in each folders
VERSION = "ylt"

IN_FOLDER = "../raw_gospel_data/" 
OUT_FOLDER = "../training_data/"

if __name__ == "__main__":

    files = os.listdir(IN_FOLDER + VERSION)
    # Load raw data folder wise 
    for i, file in enumerate(files):
        f_name, _ = os.path.splitext(file)
        raw_data = load_json(IN_FOLDER + VERSION + "/" + file)
        training_data = generate_training_data(raw_data, nlp)
        training_data = training_data.replace("`", "'")
        with open(OUT_FOLDER + f_name + ".txt", "w") as text_file:
            text_file.write(training_data)
        print("{}/{} is done, filename: {}".format(i+1, len(files), f_name))

