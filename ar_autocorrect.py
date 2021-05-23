from autocorrect import AutoCorrection
import json

letters = 'ابتثجحخدذرزسشصضطظعغفقكلمنويءؤئإألإ'
ARZ_JSON = './data/ar_arz_wiki_corpus.json'

def process_wiki_arz_json_list(file):
    file = open(file)
    corpus_l = []
    for line in file:
        dline  = json.loads(line)
        corpus_l.append(dline['text'])
    corpus  = ' '.join(corpus_l)
    word_l = corpus.split()
    return word_l

word_l = process_wiki_arz_json_list(ARZ_JSON)
print(f"corpus with {len(word_l)} words")
AC = AutoCorrection(word_l, letters)

while True:
    my_word = input('write your sentence:\n')
    words = my_word.split()
    corrected = []
    for w in words:
        tmp_corrections = AC.get_corrections(w)
        suggestion = tmp_corrections[0][0]
        corrected.append(suggestion)
        print('suggestion for word{} is {}'.format(w, suggestion))
        #for i, word_prob in enumerate(tmp_corrections):
             #print(f"word {i}: {word_prob[0]}, probability {word_prob[1]:.6f}")
    #print(f"data type of corrections {type(tmp_corrections)}")
    print(' '.join(corrected))
