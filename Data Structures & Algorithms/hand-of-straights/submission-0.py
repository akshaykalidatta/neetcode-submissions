class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hmap = {}
        for i in hand:
            if i not in hmap:
                hmap[i] = 1
            else:
                hmap[i] += 1

        hand = sorted(hand)

        for i in hand:
            if hmap[i]==0:
                continue
            for j in range(i, i+groupSize):
                if j not in hmap:
                    return False
                hmap[j] -= 1

        return True