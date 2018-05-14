import json
import spacy 

nlp = spacy.load('en_core_web_lg')

def load_json(file_name):
    """
    Load the json file to a json object
    """
    return json.load(open(file_name))

def rearrange_data(data):
    """
    Rearrange the input json schema to more 
    convenient form
    """
    out_dict = {}
    for chapter in data['chapters']:
        chapter_num = chapter['chapter']
        verse_list = chapter['verses'] 
        temp_list = []
        for verse in verse_list:
            temp_list.extend(list(verse.values()))
        out_dict[chapter_num] = temp_list
    return out_dict

def build_vocabulary(corpus):
    vocab_dict = {}
    for verse in corpus:
        doc = nlp(verse)
        for token in doc:
            if token.text not in vocab_dict.keys():
                vocab_dict[token.text] = 1
            else:
                vocab_dict[token.text] = vocab_dict[token.text] + 1
    return vocab_dict

def create_trainable_seq(corpus):
    """
    Add <SOV>, <EOV> and <EOC> tags
    Separate each tokens by a space to use it directly for training with line.split()
    """
    corpus_with_flags = {}
    for chapter, verses in data_arranged.items():
        temp_list = []
        for i, verse in enumerate(verses):
            doc = nlp(verse)
            temp_verse = " "
            for token in doc:
                temp_verse = temp_verse + " " + token.text
            temp_verse = temp_verse.strip()
            if i != len(verses)-1:
                new_verse = "<SOV> " + temp_verse + " <EOV>"
            else:
                new_verse = "<SOV> " + temp_verse + " <EOV> <EOC>"
            temp_list.append(new_verse)
        corpus_with_flags[chapter] = temp_list
    return corpus_with_flags

if __name__ == "__main__":
    
    # Load the file 
    data = load_json('John.json')

    # Initial arrangement

    data_arranged = rearrange_data(data)

    # Build corpus which is a list of verses from all chapters
    corpus = []
    for i, j in data_arranged.items():
        corpus.extend(j)
    # Build vocabulary dictionary with key as word and value as count
    vocab_dict = build_vocabulary(corpus)

    # Write it to a json file 
    with open('John_vocab.json', 'w') as outfile:
        json.dump(vocab_dict, outfile)
    # Make trainable sequences 
    sequences = create_trainable_seq(corpus)
    with open('John_cleaned.json', 'w') as fp:
        json.dump(sequences, fp)

