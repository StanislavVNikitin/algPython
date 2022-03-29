
### Две задачи на префиксное дерево:
### 2) https://leetcode.com/problems/replace-words/

import collections

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        trie = {}

        for root in dictionary:
            current = trie
            for letter in root:
                current = current.setdefault(letter, {})
            current['_end_'] = root

        def replace(word):
            current = trie
            for letter in word:
                if letter not in current or '_end_' in current: break
                current = current[letter]
            return current.get('_end_', word)

        return ' '.join(map(replace, sentence.split()))     
        
        
### 3) https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary:

    def __init__(self):
        self.word_dict = collections.defaultdict(list)
        

    def addWord(self, word: str) -> None:
        if word:
            self.word_dict[len(word)].append(word)
        

    def search(self, word: str) -> bool:
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for v in self.word_dict[len(word)]:
            # match xx.xx.x with yyyyyyy
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else: # if no break in previous for loop;
                return True
        return False
        