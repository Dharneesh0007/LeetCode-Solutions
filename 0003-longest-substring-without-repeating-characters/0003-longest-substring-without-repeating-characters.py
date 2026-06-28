class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index_map = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            if current_char in char_index_map and char_index_map[current_char] >= left:
                left = char_index_map[current_char] + 1
                
            char_index_map[current_char] = right
            
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
                
        return max_len
        