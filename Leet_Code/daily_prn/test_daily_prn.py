class WordDictionary(object):
    
    def __init__(self):
        self.arr = []

    def addWord(self, word):
        self.arr.append(word)
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
