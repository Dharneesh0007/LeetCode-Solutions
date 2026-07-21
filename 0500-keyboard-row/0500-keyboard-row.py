class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        for word in words:
            lower_word = word.lower()
            if set(lower_word) <= row1 or set(lower_word) <= row2 or set(lower_word) <= row3:
                result.append(word)
        
        result_str = str(result) 
        return result