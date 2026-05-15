# Last updated: 5/15/2026, 11:22:59 AM
1class Solution(object):
2    def readBinaryWatch(self, turnedOn):
3        kq = []
4        for gio in range(12):
5            for phut in range(60):
6                if (bin(gio) + bin(phut)).count('1') == turnedOn:
7                    kq.append(str(gio) + ":" + str(phut).zfill(2))
8        return kq