from .functionalPart import makeSquare, cutter, removeTransform
from .cypher import cypher
from .uncypher import uncypher


class TextCypher:

    def __init__(self, text, key, spacer, is_cypher=False):
        
        self.text = cutter(text, int(spacer))
        self.key = makeSquare(key)
        self.cypher = is_cypher

    def _text_cypher(self):
        return cutter(cypher(self.text, self.key), 5).upper()

    def _text_uncypher(self):
        return uncypher(self.text, self.key).upper()

    def __repr__(self):
        if text == "" or not spacer.isdigit() or key == "" or text is None or key is None:
            return ""
        return self._text_uncypher() if self.cypher else self._text_cypher()
        
