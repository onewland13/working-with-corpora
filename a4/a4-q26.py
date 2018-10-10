# Natural Language Toolkit: code_baseline_tagger
import nltk
import pylab
from nltk.corpus import brown

def performance_with_unigram_tagger(orig_data, size): 
    # Training data is from the start of data to the size value
    unigram_tagger = nltk.UnigramTagger(orig_data[:size])
    # Testing data is what's left after braking up training data
    return unigram_tagger.evaluate(orig_data[size:])

def display():
    # Get our gold standard
    brown_tagged_sents = brown.tagged_sents(categories='news')
    # The number of sizes we want to test
    number_of_sizes = 100
    max_size = int(len(brown_tagged_sents) * 0.9)
    # get our list of sizes
    sizes_of_training = range(1, max_size, int(max_size / number_of_sizes)) 
    # Get a performance for each size
    perfs = [performance_with_unigram_tagger(brown_tagged_sents, size) for size in sizes_of_training]
    pylab.plot(sizes_of_training, perfs, '-bo')
    pylab.title('Unigram Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()

if __name__ == '__main__': 
    display()