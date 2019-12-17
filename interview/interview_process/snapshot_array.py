import collections

class SnapshotArray:

    def __init__(self, length: int):
        self.snapshots = [collections.defaultdict(int)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.snapshots[self.snap_id][index] = val

    def snap(self) -> int:
        new_dic = collections.defaultdict(int)
        self.snapshots.append(new_dic)
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        val = 0
        for i in range(snap_id, -1, -1):
            snap_dic = self.snapshots[i]
            if index in snap_dic:
                return snap_dic[index]
        return val


import unittest


class TestSolution(unittest.TestCase):

    def testSolution(self):
        sol = SnapshotArray(3)
        sol.set(0, 5)
        sol.snap()
        sol.set(0, 6)
        sol.get(0, 0)


# class SnapshotArray:
#
#     def __init__(self, length: int):
#         self.snapshots = [[0] * length]
#         self.snap_id = 0
#
#     def set(self, index: int, val: int) -> None:
#         self.snapshots[self.snap_id][index] = val
#
#     def snap(self) -> int:
#         self.snapshots.append(self.snapshots[self.snap_id].copy())
#         self.snap_id += 1
#         return self.snap_id - 1
#         pass
#
#     def get(self, index: int, snap_id: int) -> int:
#         return self.snapshots[snap_id][index]