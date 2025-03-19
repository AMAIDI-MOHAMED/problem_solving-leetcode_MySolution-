class Solution(object):
    def anagram(self, string1, string2):
        # Sort both strings and compare
        return sorted(string1) == sorted(string2)

    def groupAnagrams(self, strs):
        contain = {}  # Dictionary to store grouped anagrams
        
        # Iterate through the list of strings
        for s in strs:
            # Sort the string and use the sorted version as the key
            sorted_str = ''.join(sorted(s))
            
            # Append the string to the list of anagrams
            if sorted_str in contain:
                contain[sorted_str].append(s)
            else:
                contain[sorted_str] = [s]
        
        # Return the values (list of anagram groups)
        return list(contain.values())
