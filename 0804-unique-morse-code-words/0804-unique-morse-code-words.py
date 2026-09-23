class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        unique_transformations = set()
        
        for word in words:
            transformation = "".join(morse_codes[ord(char) - ord('a')] for char in word)
            unique_transformations.add(transformation)
            
        return len(unique_transformations)