class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            if i in freq.keys():
                freq[i] += 1
            else:
                freq[i] = 1
        output = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        return output[:k]
