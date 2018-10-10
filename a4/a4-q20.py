import nltk 
from nltk.corpus import brown
import functools
# 1. Produce an alphabetically sorted list of the distinct words tagged as MD.
def unique_instances_of_pos(tagged_text, pos): 
    """ unique_instances_of_pos
    Parameters: 
        tagged_text: List of tuples containing text and it's POS tag
        pos: The part of speech we want instances of
    Returns: 
        pos_sorted_instances: Sorted list of unique instances of the POS provided 
    """
    pos_terms = [
        term.lower() 
        for (term, tag) 
        in tagged_text 
        if tag == pos
    ]
    pos_sorted_instances = sorted(list(set(pos_terms)))
    return pos_sorted_instances

# 2. Identify words that can be plural nouns or third person singular verbs (e.g. deals, flies).
def words_with_both_pos(tagged_text, pos1, pos2): 
    """ words_with_both_pos
    
    Given a tagged_text and two parts of speech, return all words that 
    can are tagged with both parts of speech

    Parameters: 
        tagged_text: List of tuples containing text and it's POS tag
        pos1: The first part of speech our words should have 
        pos2: The second part of speech our words should have 
    
    Returns: 
        terms_with_both: List of all terms with both POS 
    """
    # For all terms, get all POS 
    terms_with_pos1 = set()
    terms_with_pos2 = set()
    for (word, tag) in tagged_text: 
        if tag == pos1: 
            terms_with_pos1.add(word.lower())
        if tag == pos2: 
            terms_with_pos2.add(word.lower())
    terms_with_both = list(terms_with_pos1.intersection(terms_with_pos2))
    return terms_with_both
	
# 3. Identify three-word prepositional phrases of the form IN + AT + NN (eg. in the lab).
def trigams_with_pos(tagged_text, pos1, pos2, pos3): 
    """ trigams_with_pos

    Given a tagged_text and three parts of speech, return all trigrams that 
    contain those POS in order

    Parameters: 
        tagged_text: List of tuples containing text and it's POS tag
        pos1: The first part of speech in our trigram 
        pos2: The second part of speech in our trigram 
        pos3: The third part of speech in our trigram 
    Returns: 
        trigrams_with_all_pos: List of all trigrams with the pos in order 
    """
    trigrams = nltk.trigrams(tagged_text)
    trigrams_with_all_pos = [
        f"{tri[0][0]} {tri[1][0]} {tri[2][0]}"
        for tri
        in nltk.trigrams(tagged_text) 
        if tri[0][1] == pos1 and tri[1][1] == pos2 and tri[2][1] == pos3
    ]
    return trigrams_with_all_pos

# 4. What is the ratio of masculine to feminine pronouns?
# Known masc and fem pronouns based on an exploration of the brown text we care about
masc_pronouns = ["his", "hisself", "him", "himself", "he", "hymselfe", "hym", "'im", "himselfe"]
fem_pronouns = ["herself", "her", "hers", "she"]

def masc_fem_count_fn (count_tuple, pronoun): 
    """ masc_fem_count_fn

    Given a running count of masc and fem pronouns, and a new pronoun, 
    return an updated count based on the type of pronoun received

    Parameters: 
        tagged_text: List of tuples containing text and it's POS tag
    Returns: 
        ratio_masc_to_fem: The ratio of masculine to feminine pronouns
    """
    (masc_count, fem_count) = count_tuple;
    if pronoun in masc_pronouns:
        return (masc_count + 1, fem_count)
    elif pronoun in fem_pronouns:
        return (masc_count, fem_count + 1)
    else: 
        return (masc_count, fem_count) 

def ratio_masc_fem_pronouns(tagged_text):
    """ ratio_masc_fem_pronouns

    Given a tagged_text and three parts of speech, 
    return the ratio of masculine and feminine pronouns in that text

    Parameters: 
        tagged_text: List of tuples containing text and it's POS tag
    Returns: 
        ratio_masc_to_fem: The ratio of masculine to feminine pronouns
    """
    pronouns = [
        term.lower() 
        for (term, tag) 
        in nltk.corpus.brown.tagged_words(tagset="universal") 
        if tag == "PRON"
    ]
    (masc_count, fem_count) = functools.reduce(masc_fem_count_fn, pronouns, (0,0))
    print("masc_count: ", masc_count)
    print("fem_count: ", fem_count)
    ratio_masc_to_fem = masc_count/fem_count; 
    return ratio_masc_to_fem

if __name__ == '__main__':
    brown_tagged = brown.tagged_words();
    sample_number = 10
    print("--- 1: A sample of unique instances of MD")
    print(unique_instances_of_pos(brown_tagged, "MD")[:sample_number], "...")
    print("\n--- 2: A sample of words that can be plural nouns or 3rd person singular verbs")
    print(words_with_both_pos(brown_tagged, "NNS", "VBZ")[:sample_number], "...")
    print("\n--- 3: A sample of trigrams of form IN + DET + NN")
    print(trigams_with_pos(brown_tagged, "IN", "AT", "NN")[:sample_number], "...")
    print("\n--- 4: Ratio of masculine to feminine (based on universal tagset)")
    print(ratio_masc_fem_pronouns(brown.tagged_words(tagset="universal")))
    