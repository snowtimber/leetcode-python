'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        match = strs[0]

        #iterate through strings
        for j, str in enumerate(strs):

            if str == "":
                return ""

            if j == 0:
              continue

            match = match[:len(str)]

            #iterate letters in string
            for i, letter in enumerate(str):

                #see if even the first character matches the match
                if match[0] != str[0]:
                    return ""

                #break if length of str exceeds match length
                if i == len(match):
                    match = match[:i+1]
                    break

                #if letter does not match letter, set match to prior match
                if letter != match[i]:
                    print(match[i])
                    match = match[:i]
                    break

        return match
