import json

def load_json(file_name):
    """
    Load the json file to a json object
    """
    return json.load(open(file_name))


if __name__ == "__main__":
    # create the complete list of vocab by adding all the individual vocabularies

    matthew_vocab = load_json('Matthew_vocab.json')
    mark_vocab = load_json('Mark_vocab.json')
    luke_vocab = load_json('Luke_vocab.json')
    john_vocab = load_json('John_vocab.json')
    
    matthew_vocab = list(matthew_vocab.keys())
    mark_vocab = list(mark_vocab.keys())
    luke_vocab = list(luke_vocab.keys())
    john_vocab = list(john_vocab.keys())
    
    complete_vocab = list(set(matthew_vocab + mark_vocab + luke_vocab + john_vocab))
    complete_vocab = {"vocab": complete_vocab}
    
    with open('complete_vocab.json', 'w') as fp:
        json.dump(complete_vocab, fp)

    # create the complete list of vocab by adding all the individual vocabularies

    matthew_cleaned = load_json('data/Matthew_cleaned.json')
    mark_cleaned = load_json('data/Mark_cleaned.json')
    luke_cleaned = load_json('data/Luke_cleaned.json')
    john_cleaned = load_json('data/John_cleaned.json')

    matthew_cleaned = [item for sublist in matthew_cleaned.values() for item in sublist]
    mark_cleaned = [item for sublist in mark_cleaned.values() for item in sublist]
    luke_cleaned = [item for sublist in luke_cleaned.values() for item in sublist]
    john_cleaned = [item for sublist in john_cleaned.values() for item in sublist]

    complete_verses = {"vocab": matthew_cleaned}
        with open('data/training_matthew.json', 'w') as fp:
            json.dump(complete_verses, fp)
    complete_verses = {"vocab": mark_cleaned}
        with open('data/training_mark.json', 'w') as fp:
            json.dump(complete_verses, fp)

    complete_verses = {"vocab": luke_cleaned}
        with open('data/training_luke.json', 'w') as fp:
            json.dump(complete_verses, fp)

    complete_verses = {"vocab": john_cleaned}
    with open('data/training_john.json', 'w') as fp:
        json.dump(complete_verses, fp)

    single_big_corpus = matthew_cleaned + mark_cleaned + luke_cleaned + john_cleaned
    with open('data/single_big_corpus.json', 'w') as fp:
        json.dump(single_big_corpus, fp)