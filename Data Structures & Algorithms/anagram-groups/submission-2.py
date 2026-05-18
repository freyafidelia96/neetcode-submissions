from collections import defaultdict
class Solution:
    def countLetters(self, word):
        wordLetterCount = defaultdict(int)

        for i in range(len(word)):
            wordLetterCount[word[i]] += 1

        return wordLetterCount


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringLen = defaultdict(dict)
        stringLenDict = defaultdict(list)

        id = 1
        for word in strs:
            match = False
            wordLetterCount = self.countLetters(word)
    
            for key, value in stringLen.items():
                if wordLetterCount == value:
                    match = True
                    stringLenDict[key].append(word)

            if not match:
                stringLen[id] = wordLetterCount
                stringLenDict[id].append(word)
                id = id + 1

                
        result= []

        for i in stringLenDict:
            result.append(stringLenDict[i])
        
        return result
