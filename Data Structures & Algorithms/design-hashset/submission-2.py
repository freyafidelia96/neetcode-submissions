class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:
    def __init__(self):
        # create the set space with dummy nodes
        self.set = [ListNode(0) for i in range(10 ** 4)]

    def add(self, key: int) -> None:
        curNode = self.set[key % len(self.set)]
        while curNode.next:
            if curNode.next.key == key:
                return
            curNode = curNode.next
        curNode.next = ListNode(key) 

    def remove(self, key: int) -> None:
        curNode = self.set[key % len(self.set)]
        while curNode.next:
            if curNode.next.key == key:
                curNode.next = curNode.next.next
                return
            curNode = curNode.next

    def contains(self, key: int) -> bool:
        curNode = self.set[key % len(self.set)]
        while curNode.next:
            if curNode.next.key == key:
                return True
            curNode = curNode.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)