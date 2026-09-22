
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for i in strs:
            output[''.join(sorted(i))].append(i)
        return list(output.values())