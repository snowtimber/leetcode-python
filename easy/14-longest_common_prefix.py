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
