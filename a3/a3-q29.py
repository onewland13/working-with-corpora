import nltk 
from nltk.corpus import brown

def ARI_for_text(text, category=""): 
    """ ARI_for_text
    Parameters: 
        text: A nltk.Text object that we are computing the ARI score for 
    Returns: 
        ari: The Automated Readability Index (ARI) of the text. 
    """
    sents = text.sents(categories=category) if category != "" else text.sents()
    words = text.words(categories=category) if category != "" else text.words()
    chars = ''.join(words)
    #  the average number of letters per word 
    mu_w = len(chars) / len(words)
    # the average number of words per sentence
    mu_s = len(words) / len(sents)

    ari = (4.71 * mu_w) + (0.5 * mu_s) - 21.43
    return ari

if __name__ == "__main__":
    # print(ARI_for_text(nltk.corpus.brown))
    for category in brown.categories(): 
        print(f'ARI score for {category} is: {ARI_for_text(brown, category)}')