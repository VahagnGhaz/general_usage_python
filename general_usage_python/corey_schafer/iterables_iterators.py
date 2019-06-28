class Sentence:
    def __init__(self, sent: str):
        self.sentence = sent
        self.words = self.sentence.split()
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.idx >= len(self.words):
            raise StopIteration  # always raise stop iteration in next method

        current_idx = self.idx
        self.idx += 1
        return self.words[current_idx]


# the same implementation with generator (much easier :) )
def sentence(sent: str):
    for word in sent.split():
        yield word


if __name__ == '__main__':
    s = 'this is a sentance'

    for w in Sentence(s):
        print(w)

    print('With generator')
    for w in sentence(s):
        print(w)

    # inst = Sentence(s)
    # print(next(inst))
    # print(next(inst))
    # print(next(inst))
    # print(next(inst))
    #
    #