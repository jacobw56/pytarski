from inspect import signature

class BooleTruthTable:
    def __init__(self, sentence):
        s = sentence.split()
        self.atomics = []
        self.sentence = 'lambda '
        for c in s:
            if len(c) == 1 and not c.isalpha():
                raise NameError('Invalid atomic name. Must be alphabetic character.')
            if len(c) == 2 and c != 'or':
                raise NameError(f'Invalid connective name {c}.')
            if len(c) == 3 and (c != 'not' and c != 'and'):
                raise NameError(f'Invalid connective name {c}.')
            if len(c) != 1 and len(c) != 2 and len(c) != 3:
                raise NameError(f'Invalid sentence.')
        for c in s:
            if len(c) == 1:
                self.sentence += c + ', '
        self.sentence = self.sentence[:-2] + ' : ' + sentence
        self.evalSentence = exec(self.sentence)
        sig = signature(self.evalSentence)
        print(len(sig.parameters))

    def eval(self, l):
        for d in l:
            if l:
                pass
                