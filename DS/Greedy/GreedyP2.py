class Solution:
    def GreedyP2(self, row, col):
        answer = 0
        for i in range(row):
            cards = list(map(int, input().split()))
            card = min(cards)
            if answer < card:
                answer = card
        
        return answer

row, col = map(int, input().split())
answer = Solution()
print(answer.GreedyP2(row, col))