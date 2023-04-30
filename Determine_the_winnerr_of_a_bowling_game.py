"""
1 if the score of player 1 is more than the score of player 2,
2 if the score of player 2 is more than the score of player 1, and
0 in case of a draw.
"""
"""
n == player1.length == player2.length
1 <= n <= 1000
0 <= player1[i], player2[i] <= 10
"""


class Solution:
    def isWinner(self, player1: list[int], player2: list[int]) -> int:
        if len(player1) != len(player2):
            return -1
        else:
            n = len(player1)
            if 1 <= n <= 1000:
                sum1 = sum2 = 0
                for i, j in zip(player1, player2):
                    if i and j > 10:
                        return -1
                for index1 in player1:
                    if index1 == 10:
                        itr = player1.index(10)
                        itr += 1
                        while itr > len(player1):
                            sum1 = sum1 + player1[itr]
                            print(sum1)
                        break
                    else:
                        sum1 = sum1 + index1
                        print(sum1)
                for index2 in player2:
                    if index2 == 10:
                        itr = player2.index(10)
                        itr += 1
                        while itr > len(player2):
                            sum2 = sum2 + player2[itr]
                        break
                    else:
                        sum2 = sum2 + index2
                if sum1 == sum2:
                    return 0
                elif sum1 > sum2:
                    return sum1
                else:
                    return 2
            else:
                return -1


p1 = input("Enter player values: ").split()
p2 = input("Enter player values: ").split()
player1 = []
player2 = []
for i in p1:
    player1 += [int(i)]
for i in p2:
    player2 += [int(i)]
s = Solution()
k = s.isWinner(player1, player2)
if k == 2:
    print('Winner is player2')
elif k == 1:
    print('Winner is player1')
elif k == 0:
    print('Match is draw')
else:
    print('please enter valid values')



