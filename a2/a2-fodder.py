from nltk.corpus import wordnet as wn
import time

# problem 4
from nltk.corpus import state_union
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in state_union.fileids()
    for w in state_union.words(fileid)
    for target in ['men', 'women', 'people']
    if w.lower().startswith(target)
)



cfd_terror = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in state_union.fileids()
    for w in state_union.words(fileid)
    for target in ['men', 'women', 'people', 'terror']
    if w.lower().startswith(target))



# problem 5
vocab_1 = list(set(w.lower() for w in text1 if len(w) >= 4))

for w in vocab_1[:600]:
    avail_synsets = wn.synsets(w)
    if len(avail_synsets) > 0:
        for synset in avail_synsets:
            member_m = synset.member_meronyms()
            part_m = synset.part_meronyms()
            substance_m = synset.substance_meronyms()
            member_h = synset.member_holonyms()
            part_h = synset.part_holonyms()
            substance_h = synset.substance_holonyms()
            if (member_m or part_m or substance_m or member_m or part_m or substance_m): 
                print('\n\nSynset: ', synset)
                if (member_m or part_m or substance_m): 
                    print("--- meronyms")
                    if len(member_m) > 0: print("member_m: A constituent member of the above Synset term: ", member_m)
                    if len(part_m) > 0: print("part_m: Part of the above Synset term: ", part_m)
                    if len(substance_m) > 0: print("substance_m: The substance of the above synset term: ", substance_m)
                if (member_h or part_h or substance_h): 
                    print("--- holonymss")
                    if len(member_h) > 0: print("member_h: The above Synset term is a member of: ", member_h)
                    if len(part_h) > 0: print("part_h: The above Synset term is a part of: ", part_h)
                    if len(substance_h) > 0: print("substance_h: The above Synset term is made of: ", substance_h) 


for w in vocab_1[:1600]:
    avail_synsets = wn.synsets(w)
    if len(avail_synsets) > 0:
        for synset in avail_synsets:
            substance_h = synset.substance_holonyms()
            if (substance_h): 
                print('\n\nSynset: ', synset)
                print("--- holonymss")
                print("substance_h: The above Synset term is made of: ", substance_h) 



# Problem 9 
whit = nltk.Text(nltk.corpus.gutenberg.words('whitman-leaves.txt'))
moby = nltk.Text(nltk.corpus.gutenberg.words('melville-moby_dick.txt'))
def vocab(txt): 
    return set(w.lower() for w in txt if w.isalpha())

def vocab_len(txt): 
    return len(vocab(txt))

def vocab_richness(txt): 
    return vocab_len(txt) / len(txt)

print("Vocab: ", vocab_len(whit), " Richness: ", vocab_richness(whit))
print("Vocab: ", vocab_len(moby), " Richness: ", vocab_richness(moby))
whit.collocations()
moby.collocations()

['new', 'good', 'high', 'old', 'great', 'big', 'American', 'small', 'large', 'national', 'young', 'different', 'black', 'long', 'little', 'important', 'political', 'bad', 'white', 'real', 'best', 'right', 'social', 'only', 'public', 'sure', 'low', 'early', 'able', 'human', 'local', 'late', 'hard', 'major', 'better', 'economic', 'strong', 'possible', 'whole', 'free', 'military', 'true', 'federal', 'international', 'full', 'special', 'easy', 'clear', 'recent', 'certain', 'personal', 'open', 'red', 'difficult', 'available', 'likely', 'short', 'single', 'medical', 'current', 'wrong', 'private', 'past', 'foreign', 'fine', 'common', 'poor', 'natural', 'significant', 'similar', 'hot', 'dead', 'central', 'happy', 'serious', 'ready', 'simple', 'left', 'physical', 'general', 'environmental', 'financial', 'blue', 'democratic', 'dark', 'various', 'entire', 'close', 'legal', 'religious', 'cold', 'final', 'main', 'green', 'nice', 'huge', 'popular', 'traditional', 'cultural']

count = 1
for adj in adjs[45:]:
    if count > 50: break
    print('\nAdj: ', adj)
    count += 1
    print("Whit: ")
    whit.similar(adj)
    print("Blake: ")
    moby.similar(adj)

whit.similar('cold')
moby.similar('cold')

whit.similar('dark')
moby.similar('dark')

whit.similar('main')
moby.similar('main')

# Problem 23 
from nltk.corpus import reuters
import pylab

r_words = reuters.words()

def zipf_plot(large_txt): 
    fdist = nltk.FreqDist(large_txt)
    pylab.plot(
        # Add one so we don't have 0 values in play
        range(1, fdist.B() + 1),      # fdist.B() is number of unique sample values (or bins)
        fdist.values()                # y-axis: word count
    )
    # Let's use a log scale per instructions 
    pylab.xscale('log')
    pylab.yscale('log')
    pylab.show()

zipf_plot(r_words)

rand_string = ""
for i in range(10000000):
    rand_string += random.choice("abcdefg ")

rand_text = rand_string.split()
zipf_plot(rand_text)