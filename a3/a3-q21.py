
import nltk, re, pprint, sys
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup

def sep(): 
    print('\n\n\n------------------------\n\n\n')

def unknown(url): 
    """ Unknown
    Parameters: 
        url: a url to a webpage 

    Returns: 
        unknown_words_removing_variations_on_lemmas: a list of lowercase words 
            that are mentioned on the webpage 
            that aren't found in the Words Corpus
            and aren't variations on lemmas found in the Word Corpus.
    """
    # Step 1: get HTML
    response = request.urlopen(url)
    html = response.read().decode('utf-8')
    # Step 2: Convert to raw text
    raw = BeautifulSoup(html).get_text()
    # Step 3: Get the difference  
    known_words = set([w for w in nltk.corpus.words.words('en') if w.islower()])
    words_on_webpage = set(re.findall(r"\b[a-z]+\b", raw))
    unknown_words = sorted(words_on_webpage.difference(known_words))

    print(f'Total Words from webpage: {len(words_on_webpage)}')
    print(f'Total unknown words: {len(unknown_words)}')
    print(f'Percentage unknown words: {len(unknown_words)/len(words_on_webpage)}')
    # Manual investigation of results highlights that the Words Corpus doesn't include variations on word lemmas 
    # Let's remove those variations for a better idea of how many new 'terms' appear on our webpage 
    word_versions = re.findall(r'\b[a-z]+(?:ing|ly|ed|ious|ies|ive|es|s|ment)', ' '.join(list(unknown_words)))
    unknown_words_removing_variations_on_lemmas = set(unknown_words).difference(set(word_versions))
    print(f'Total unknown words, removing common variations on word lemmas: {len(unknown_words_removing_variations_on_lemmas)}')
    print(f'Percentage unknown words, after removing common variations on word lemmas: {len(unknown_words_removing_variations_on_lemmas)/len(words_on_webpage)}')

    return unknown_words

if __name__ == '__main__':
    new_terms = unknown(sys.argv[1])
    print(new_terms)