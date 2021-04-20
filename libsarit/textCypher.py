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

    def _text_cypher(self):
        return cypher(self.text, self.key)

    def _text_uncypher(self):
        return uncypher(self.text, self.key)

    def __repr__(self):
        return self._text_uncypher() if self.is_cypher else self._text_cypher()
        
