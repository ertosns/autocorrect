class AutoCorrection(object):
    def __init__(self, words, alphabets, verbose=False, switch_on=False):
        self.word_l = words
        self.alphabets = alphabets
        self.switch_on=switch_on
        self.verbose = verbose
        self.vocab = set(self.word_l)
        self.counts = {}
        self.probs = {}
        self.__get_count()
        self.__get_probs()
    def __get_count(self):
        '''
        The counts dictionary where key is the word and value is its frequency.
        '''
        for w in self.word_l:
            self.counts[w]=self.counts.get(w,0)+1
    def __get_probs(self):
        '''
        probs dictionary where keys are the words and the values are the probability that a word will occur.
        '''
        M=sum(self.counts.values())
        for w, v in self.counts.items():
            self.probs[w] = v/M
    def __transform(self, word):
        split_l = []
        delete_l = []
        switch_l = []
        replace_l = []
        insert_l = []
        # delete
        for i in range(len(word)):
            split_l.append((word[:i], word[i:]))
            delete_l.append((word[:i]+ word[i:][1:]))

        if self.verbose: print(f"input word {word}, \nsplit_l = {split_l}, \ndelete_l = {delete_l}")
        # switch
        if self.switch_on:
            for i in range(len(word)):
                split_l.append((word[:i], word[i:]))
                if len(word[i:])>=2:
                    switch_l.append(word[:i]+word[i+1]+word[i]+word[i+2:])
            if self.verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nswitch_l = {switch_l}")
        # replace
        for i in range(len(word)):
            split_l.append((word[:i],word[i:]))
            for c in self.alphabets:
                if len(word)-i>=1 and word[i]!=c:
                    replace_l.append(word[:i]+c+word[i+1:])
        # turn the set back into a list and sort it, for easier viewing
        replace_l = sorted(list(replace_l))
        if self.verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nreplace_l {replace_l}")
        # insert
        for i in range(len(word)+1):
            split_l.append((word[:i], word[i:]))
            for c in self.alphabets:
                insert_l.append(word[:i]+c+word[i:])
        if self.verbose: print(f"Input word {word} \nsplit_l = {split_l} \ninsert_l = {insert_l}")
        return delete_l + switch_l + replace_l + insert_l

    def edit_one_letter(self, word):
        transforms = self.__transform(word)
        edit_one_set = set(transforms)
        return edit_one_set


    def edit_two_letters(self, word):
        edit_two_set = set()
        for w in self.edit_one_letter(word):
            for w2 in self.edit_one_letter(w):
                edit_two_set.add(w2)
        return edit_two_set

    def get_corrections(self, word):
        sug_dict = []
        n_best = []
        # if exists in vocabulary already
        invocab = self.vocab.intersection([word])
        # if exists in one letter edit
        l1=self.edit_one_letter(word)
        in1l=self.vocab.intersection(l1)
        # if exists in two letters edit
        l2 = self.edit_two_letters(word)
        in2l=self.vocab.intersection(l2)
        suggestions = {word: self.probs.get(word, 0) for word in invocab or in1l or in2l }
        n_best=sorted(suggestions.items(), key=lambda item: item[1], reverse=True)[0:2]
        if self.verbose: print("entered word = ", word, "\nsuggestions = ", suggestions)
        return n_best
