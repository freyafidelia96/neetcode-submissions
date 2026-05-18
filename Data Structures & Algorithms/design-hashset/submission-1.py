class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        # self.items = []
        self.set = [ListNode(0) for i in range(10**4)]
    

    def add(self, key: int) -> None:
        # if key in self.items:
        #     return
        # self.items.append(key)

        curr = self.set[key % len(self.set)]
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        # if key not in self.items:
        #     return
        # self.items.remove(key)  

        curr = self.set[key % len(self.set)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        

    def contains(self, key: int) -> bool:
        # return key in self.items

        curr = self.set[key % len(self.set)]
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)