from .functionalPart import makeSquare, cutter, removeTransform
from .cypher import cypher
from .uncypher import uncypher


class TextCypher:

    def __init__(self, text, key, spacer, is_cypher=False):
        if text == "" or not spacer.isdigit() or key == "" or text is None or key is None:
            return
        self.text = cutter(text, int(spacer))
        self.key = makeSquare(key)
        self.is_cypher = is_cypher

    def text_cypher(self):
        return cypher(self.text, self.key)

    def text_uncypher(self):
        return uncypher(self.text, self.key)

    def __iter__(self):

        if self.is_cypher:
            for e in self.text_uncypher(), self.text:
                if e.endswith(" "):
                    e = " ".join(e.split(" ")[:-1])
                yield e
        else:
            for e in self.text_cypher(), self.text:
                if e.endswith(" "):
                    e = " ".join(e.split(" ")[:-1])
                yield e
