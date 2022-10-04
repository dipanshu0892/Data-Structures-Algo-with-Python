class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
    
        hashMap = {}
        
        #example 2 and 3
        if len(strs) == 1 and (strs[0] == "" or len(strs[0]) == 1):
            return [strs]

        for i in range(0,len(strs)):                  #iterate through the list
            ordered_key =''.join(sorted(strs[i]))     #sorting each character in the current str and joining them to a string
            if ordered_key not in  hashMap.keys():    #if this key is not in the dictionary/hash map
                 hashMap[ordered_key] = [strs[i]]     # add the key and value
            else:
                 hashMap[ordered_key].append(strs[i]) # or append the word to existing key
        return  hashMap.values()                      #return the dictionary values
