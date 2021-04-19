from .functionalPart import makeSquare, cutter, removeTransform
from .cypher import cypher
from .uncypher import uncypher


class TextCypher(object):

    def __init__(self, text, key, spacer, is_cypher=False):
        self.text = cutter(text, spacer)
        self.key = makeSquare(key)
        self.is_cypher = is_cypher

    def text_cypher(self):
        return cypher(self.text, self.key)

    def text_uncypher(self):
        return uncypher(self.text, self.key)

    def __next__(self):

        if self.is_cypher:
            return self.text_uncypher(), self.text

        else:
            return self.text_cypher(), self.text
