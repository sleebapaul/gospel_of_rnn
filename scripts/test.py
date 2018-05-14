import json

with open("data/training_luke.json") as fp:
    data = json.load(fp)
data = data["vocab"]

ting = []
for verse in data:
    verse_ = verse.replace("<EOV>", "")
    verse_ = verse_.replace("<EOC>", "")
    verse_ = verse_.replace("<SOV>", "")
    ting.append(verse_)
    
def list2txt(some_list,path):
    """
    Writes a text file from the input list (into split lines)
    Specify the path as string
    Specify the column names as a list of string
    """
    with open(path, "w",encoding="utf-8") as text_file:
        for i in range(len(some_list)):
            text_file.write(some_list[i]+"\n")

list2txt(ting, "input.txt")