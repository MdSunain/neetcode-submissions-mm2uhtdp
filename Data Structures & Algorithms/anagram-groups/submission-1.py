class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}

        for i in strs:
            # classifying 
            sorted_string =  ''.join(sorted(i))

            # grouping 
            if sorted_string not in grp:
                grp[sorted_string] = []
            grp[sorted_string].append(i)

            # building output
        output = []
        for i in grp:
            output.append(grp[i])

        return output

