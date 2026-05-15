# Last updated: 5/15/2026, 10:35:52 AM
1class Solution(object):
2    def getIntersectionNode(self, headA, headB):
3        if not headA or not headB:
4            return None
5        pA = headA
6        pB = headB
7        while pA != pB:
8            pA = pA.next if pA else headB
9            pB = pB.next if pB else headA
10        return pA