class SnapshotArray:

    def __init__(self, length: int):
        self.array=[0]*length
        self.c=1
        self.currarray=[0]*length

    def set(self, index: int, val: int) -> None:
        self.array[index]=val
        return self.array
        

    def snap(self) -> int:
        self.c+=1
        self.currarray[self.c]=self.array
        print(self.currarray)
        return self.c
        

    def get(self, index: int, snap_id: int) -> int:
        return self.currarray[snap_id][index]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)