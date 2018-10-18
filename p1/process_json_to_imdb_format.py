import os
import sys
import json

# TODO: Have fn take a path, and call fn multiple times
#       so we don't load all these JSON objects into memory at once.
def getCharacterToGender():
    print("getCharacterToGender")
    curDir = os.getcwd()
    directory = os.path.join(curDir, 'genders')
    return [
        json.load(open(os.path.join(directory, work), 'r'))
        for work in os.listdir(directory) 
        if os.path.isfile(os.path.join(directory, work))
    ]

def getCharacterToLines():
    print("getCharacterToLines")
    curDir = os.getcwd()
    directory = os.path.join(curDir, 'json')
    return [
        json.load(open(os.path.join(directory, work), 'r'))
        for work in os.listdir(directory) 
        if os.path.isfile(os.path.join(directory, work))
    ]

def buildVocabToNumMapping(vocab):
    """
    Create lookup tables for vocabulary used
    :param text: A list of text, corresponding to all the words in our vocabulary
    :return: A tuple of dicts (vocab_to_num, num_to_vocab)
    """
    # Index starts at one so we reseve 0 as a padding character 
    index = 1
    vocab_to_num = {}
    num_to_vocab = {}
    
    for word in vocab:
        if word not in vocab_to_num:
            vocab_to_num[word] = index
            num_to_vocab[index] = word
            index += 1
    print("Max index // length of vocab: %s" % index)
    
    return (vocab_to_num, num_to_vocab)

def labelEachLine(characterToGender, characterToLines):
    labeledLines = []
    for char in characterToGender:
        gender = characterToGender[char]
        lines = characterToLines
        for l in lines:
            labeledLines.append((l, gender))
    return labeledLines

if __name__ == '__main__':
	# split_text("gendered_shrew_test.txt", "shrew_test.txt")
	# split_text("gendered_data.txt", "raw_text_data.txt")
    print('run')

