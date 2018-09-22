from nltk.corpus import wordnet as wn
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

