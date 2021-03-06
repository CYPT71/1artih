from libsarit.functionalPart import make_square, cutter, remove_transform
from libsarit.cypher import cypher
from libsarit.uncypher import uncypher


class TextCypher:

    def __init__(self, text, key, spacer, is_cypher=False):
        if isinstance(spacer, str):
            if not spacer.isdigit():
                spacer = "5"
            spacer = int(spacer)

        self.text = cutter(text, spacer)
        self.key = make_square(key)
        self.cypher = is_cypher

    def __text_cypher(self):
        return cutter(cypher(self.text, self.key), 5).upper()

    def __text_uncypher(self):
        return uncypher(self.text, self.key).upper()

    def __repr__(self):
        if self.text == "" or self.key == "" or self.text is None or self.key is None:
            return ""
        return self.__text_uncypher() if self.cypher else self.__text_cypher()