from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        plate_count = Counter(c.lower() for c in licensePlate if c.isalpha())
        
        best_word = None
        
        for word in words:
            word_count = Counter(word)
            
            if all(word_count[char] >= count for char, count in plate_count.items()):
                if best_word is None or len(word) < len(best_word):
                    best_word = word
                    
        return best_word