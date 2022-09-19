# ONE way #HASHMAP
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag = True
        if len(s) != len(t): 
            flag = False
        else:
            letters = "abcdefghijklmnopqrstuvwxyz"
            for letter in letters:
                if s.count(letter) != t.count(letter):
                    flag = False
                    break
        return flag
        
        
#TWO way
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for ele in s:
            if ele not in dict:
                dict[ele] = 1
            else:
                dict[ele] += 1
        for ele in t:
            if ele not in dict:
                return False
            else:
                dict[ele] -= 1
        return False if any(dict.values()) else True
        
