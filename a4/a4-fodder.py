import nltk 
from nltk import word_tokenize
brown = nltk.corpus.brown
def sep(): 
    print('\n --------- \n ')

brown_words = brown.words()

# Using a POS tagger:
#   Provides a mechanism for tagging  
text = word_tokenize("And now for something completely different")
pos = nltk.pos_tag(text)
print(pos)
# Don't know what these stupid symbols mean? 
# Look them up using the help.upenn_taget function, ya dummy
nltk.help.upenn_tagset('CC')
nltk.help.upenn_tagset('RB')
nltk.help.upenn_tagset('IN')
nltk.help.upenn_tagset('NN')
nltk.help.upenn_tagset('JJ')
print('\nThe same words can have differnt labels')
text2 = word_tokenize("They refuse to permit us to obtain the refuse permit")
pos_complex = nltk.pos_tag(text2)
# Interestingly, we can see that the pos_tag is aware enough to label refuse and permit using 
# two different parts of speech based on the context of the sentece
print(pos_complex)
sep()

# Text.similar function: 
#   Arg: A word for whom the function will provide similar terms, meaning that they
#       occur in similar instances to the previous word.
# 	
text = nltk.Text(word.lower() for word in brown_words)
print("Let's see how we can look at simliarity in a text")
print(brown_words)

print('--- woman')
# text.similar('woman')
print('--- bought')
# text.similar('bought')
print('--- over')
# text.similar('over')
print('--- the')
# text.similar('the')
sep()

# Tagged Tokenns:
#   Just a tuple with a word the associated Tag 
print("Let's take a look at tagged tokens")
tagged_token = nltk.tag.str2tuple('fly/NN')
print("--- tagged_token")
print(tagged_token)
print("--- term")
print(tagged_token[0])
print("--- tag")
print(tagged_token[1])
# We can also have plain text that is encoded to cotain the tagging, 
# this is what the textlooks like on 
sent = '''
The/AT grand/JJ jury/NN commented/VBD on/IN a/AT number/NN of/IN
other/AP topics/NNS ,/, AMONG/IN them/PPO the/AT Atlanta/NP and/CC
Fulton/NP-tl County/NN-tl purchasing/VBG departments/NNS which/WDT it/PPS
said/VBD ``/`` ARE/BER well/QL operated/VBN and/CC follow/VB generally/RB
accepted/VBN practices/NNS which/WDT inure/VB to/IN the/AT best/JJT
interest/NN of/IN both/ABX governments/NNS ''/'' ./.
'''
tagging_with_str2tuple = [nltk.tag.str2tuple(t) for t in sent.split()]
print(tagging_with_str2tuple)
print("\nSeveral of the corpora included with NLTK have been tagged for their part-of-speech.")
print("--- Plain text")
print(brown_words)
print("--- Tagged")
print(nltk.corpus.brown.tagged_words())
print("--- Tagged, but with a specified taget (e.g. tagset='universal')")
print(nltk.corpus.brown.tagged_words(tagset="universal"))
sep()

# Universal Tagset: 
#   Let's takea  slightly closer look there
print('Universal Tagset:')
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
print('What does the frequency dist of tags in the brown corpus look like?')
# FreqDist.most_common() - 
#   gives you an array of tuples (category, freq), sorted by freq 
print(tag_fd.most_common())
print('\nNew Question: Which type of POS most commonly precedes a NOUN?')
# nltk.bigrams(words) - args: an array of elements, [i_0, i_1, i_2, ...]
#   returns an array of tuples with elements [(i_0, i_1), (i_1, i_2), ...]
word_tag_pairs = nltk.bigrams(brown_news_tagged)
print("All bigrams of tagged terms")
print(word_tag_pairs, "...")
noun_preceders = [a[1] for (a, b) in word_tag_pairs if b[1] == 'NOUN']
print('All the preceders')
print(noun_preceders[:5], "...")
fdist = nltk.FreqDist(noun_preceders)
print(" The most common preceders, in order")
print([tag for (tag, _) in fdist.most_common()])
print('\n What about verbs')