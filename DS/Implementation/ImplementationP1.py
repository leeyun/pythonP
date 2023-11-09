class Solution:
    def ImplementationP1(self, size, movement):
        location = [0, 0]
        flag = True
        move = {'L':[0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}
        for m in movement:
            goto = location[0] + move[m][0], location[1] + move[m][1]
            if goto[0] < 0 or goto[1] < 0:
                flag = False
            if goto[0] > size - 1 or goto[1] > size - 1:
                flag = False
            if flag:
                location[0], location[1] = goto[0], goto[1]
            flag = True
        location[0] += 1
        location[1] += 1
        return location
             
size = int(input())
movement = list(map(str, input().split()))
answer = Solution()
print(answer.ImplementationP1(size, movement))
