class AlphabetIterator:
    def __init__(self):
        self.alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.alphabets):
            raise StopIteration
        letter = self.alphabets[self.index]
        self.index += 1
        return letter

alphabet_iterator = AlphabetIterator()
for letter in alphabet_iterator:
    print(letter)
