class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in details:
            curr = int(i[11:13])
            if curr > 60:
                count+=1
        return count