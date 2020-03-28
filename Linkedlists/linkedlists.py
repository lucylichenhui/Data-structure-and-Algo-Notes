"""

这道题让我们合并k个有序链表，
最终合并出来的结果也必须是有序的，
之前做过一道 Merge Two Sorted Lists，
是混合插入两个有序链表。这道题增加了难度，
变成合并k个有序链表了，但是不管合并几个，
基本还是要两两合并。
那么首先考虑的方法是能不能利用之前那道题的解法来解答此题。
答案是肯定的，但是需要修改
，怎么修改呢，最先想到的就是两两合并，
就是前两个先合并，合并好了再跟第三个，
然后第四个直到第k个。这样的思路是对的，
但是效率不高，没法通过 
OJ，所以只能换一种思路，
这里就需要用到分治法 Divide and Conquer Approach。
简单来说就是不停的对半划分，
比如k个链表先划分为合并两个 k/2 个链表的任务，
再不停的往下划分，
直到划分成只有一个或两个链表的任务，
开始合并。
举个例子来说比如合并6个链表，
那么按照分治法，
首先分别合并0和3，
1和4，
2和5。
这样下一次只需合并3个链表，
再合并1和3，
最后和2合并就可以了。
代码中的k是通过 (n+1)/2 计算的，
这里为啥要加1呢，
这是为了当n为奇数的时候，
k能始终从后半段开始，
比如当 n=5 时，
那么此时 k=3，
则0和3合并，
1和4合并，
最中间的2空出来。
当n是偶数的时候，
加1也不会有影响，
比如当 n=4 时，此时 k=2，
那么0和2合并，
1和3合并
，完美解决问题，
参见代码如下：

"""

# Q1: merge k sortedlists 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#attempt 1: 
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists is None: 
            return -1
        n=len(lists)
        while n>1: 
            if n%2==1: 
                mid=n//2
                for i in range(n//2): 
                    final= merge2lists(lists[i],list[n-i])
                return merge2list(merge2lists(list[n//2],final)

            else:
                for i in range(n//2): 
                    merge2lists(lists[i],list[n-i])


            """

            k=(n+1)//2 # both even and odd cases, get even/2 
            for i in range(0,n//2): #at best n//2 will be equal to (n+1)//2, if not, smaller
                merge2lists(lists[i],lists[]
                
            """

        def merge2lists(self,a,b): 
            if a and b: 
                if a.val>b.val: 
                    a,b=b,a 
                a.next=self.merge2lists(a.next,b)
            return a or b


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#attempt 2: 
class Solution:
    
    def merge2lists(self,a,b): 
        
        result = dummy = ListNode() 
        while a: 
            if b and a.val>b.val: 
                dummy.next=b
                b=b.next
            else: 
                dummy.next=a
                a=a.next
            dummy=dummy.next 
        if b: 
            dummy.next=b 
        return result.next 
        
        """
        if a and b: 
            if a.val>b.val: 
                a,b=b,a 
            a.next=self.merge2lists(a.next,b)
        return a or b
    
        """


    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists is None: 
            return -1
        n=len(lists)
        if n==1:
            final=lists
        while n>1: 
            if n%2==1: 
                mid=n//2
                for x in range(n//2): 
                    for y in range(n//2, -1):
                        e=self.merge2lists(lists[x],lists[y])
                        
                final=self.merge2lists(lists[mid],e)
            if n%2==0:
                for i in range(n//2): 
                    final=self.merge2lists(lists[i],lists[n-i])
        
        return final


#=========#=========#=========#=========#=========#=========#=========#=========#=========#=========#=========#=========#=========#=========
#=========#=========#=========#=========#=========#=========#=========#=========#=========#=========#=========#=========#=========#=========

                                                    #      NOTES     #


#singly linked lists 

class Node:  # create a Node
    def __init__(self, data):
        self.data = data  # given data
        self.next = None  # given next to None

    def __repr__(self):  # string representation of a Node
        return f"Node({self.data})"
  
    def traverse(self,head): #traverse list nodes
        currNode=head 
        while currNode is not None: 
            currNode=currNode.next

    def search(self,head): #linked list search 
        currNode=head
        while currNode is not None and currNode.data!=target: 
            currNode=currNode.next

class LinkedList:
    def __init__(self):
        self.head = None  # initialize head to None


    def insert_tail(self, data) -> None:
        if self.head is None:
            self.insert_head(data)  # if this is first node, call insert_head
        else:
            temp = self.head
            while temp.next:  # traverse to last node
                temp = temp.next
            temp.next = Node(data)  # create node & link to tail

    def insert_head(self, data) -> None:
        new_node = Node(data)  # create a new node
        if self.head:
            new_node.next = self.head  # link new_node to head
        self.head = new_node  # make NewNode as head

    def print_list(self) -> None:  # print every node data
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def delete_head(self):  # delete from head
        temp = self.head
        if self.head:
            self.head = self.head.next
            temp.next = None
        return temp

    def delete_tail(self):  # delete from tail
        temp = self.head
        if self.head:
            if self.head.next is None:  # if head is the only Node in the Linked List
                self.head = None
            else:
                while temp.next.next:  # find the 2nd last element
                    temp = temp.next
                # (2nd last element).next = None and temp = last element
                temp.next, temp = None, temp.next
        return temp

    def is_empty(self) -> bool:
        return self.head is None  # return True if head is none

    def reverse(self):
        prev = None
        current = self.head

        while current:
            # Store the current node's next node.
            next_node = current.next
            # Make the current node's next point backwards
            current.next = prev
            # Make the previous node be the current node
            prev = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end
        self.head = prev

    def __repr__(self):  # String representation/visualization of a Linked Lists
        current = self.head
        string_repr = ""
        while current:
            string_repr += f"{current} --> "
            current = current.next
        # END represents end of the LinkedList
        return string_repr + "END"

    # Indexing Support. Used to get a node at particular position
    def __getitem__(self, index):
        current = self.head

        # If LinkedList is empty
        if current is None:
            raise IndexError("The Linked List is empty")

        # Move Forward 'index' times
        for _ in range(index):
            # If the LinkedList ends before reaching specified node
            if current.next is None:
                raise IndexError("Index out of range.")
            current = current.next
        return current

    # Used to change the data of a particular node
    def __setitem__(self, index, data):
        current = self.head
        # If list is empty
        if current is None:
            raise IndexError("The Linked List is empty")
        for i in range(index):
            if current.next is None:
                raise IndexError("Index out of range.")
            current = current.next
        current.data = data


def main():
    A = LinkedList()
    A.insert_head(input("Inserting 1st at head ").strip())
    A.insert_head(input("Inserting 2nd at head ").strip())
    print("\nPrint list:")
    A.print_list()
    A.insert_tail(input("\nInserting 1st at tail ").strip())
    A.insert_tail(input("Inserting 2nd at tail ").strip())
    print("\nPrint list:")
    A.print_list()
    print("\nDelete head")
    A.delete_head()
    print("Delete tail")
    A.delete_tail()
    print("\nPrint list:")
    A.print_list()
    print("\nReverse linked list")
    A.reverse()
    print("\nPrint list:")
    A.print_list()
    print("\nString representation of linked list:")
    print(A)
    print("\nReading/changing Node data using indexing:")
    print(f"Element at Position 1: {A[1]}")
    A[1] = input("Enter New Value: ").strip()
    print("New list:")
    print(A)


if __name__ == "__main__":
    main()

#=========#=========#=========#=========#=========#=========#=========#=========#=========#=========#=========#=========#=========#=========
#=========#=========#=========#=========#=========#=========#=========#=========#=========#=========#=========#=========#=========#=========

from typing import Any


class Node:
    """
    Class to represent a single node.
    Each node has following attributes
    * data
    * next_ptr
    """

    def __init__(self, data: Any):
        self.data = data
        self.next_ptr = None


class CircularLinkedList:
    """
    Class to represent the CircularLinkedList.
    CircularLinkedList has following attributes.
    * head
    * length
    """

    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self) -> int:
        """
        Dunder method to return length of the CircularLinkedList
        >>> cll = CircularLinkedList()
        >>> len(cll)
        0
        >>> cll.append(1)
        >>> len(cll)
        1
        """
        return self.length

    def __str__(self) -> str:
        """
        Dunder method to represent the string representation of the CircularLinkedList
        >>> cll = CircularLinkedList()
        >>> print(cll)
        Empty linked list
        >>> cll.append(1)
        >>> cll.append(2)
        >>> print(cll)
        <Node data=1> => <Node data=2>
        """
        current_node = self.head
        if not current_node:
            return "Empty linked list"

        results = [current_node.data]
        current_node = current_node.next_ptr

        while current_node != self.head:
            results.append(current_node.data)
            current_node = current_node.next_ptr

        return " => ".join(f"<Node data={result}>" for result in results)

    def append(self, data: Any) -> None:
        """
        Adds a node with given data to the end of the CircularLinkedList
        >>> cll = CircularLinkedList()
        >>> cll.append(1)
        >>> print(f"{len(cll)}: {cll}")
        1: <Node data=1>
        >>> cll.append(2)
        >>> print(f"{len(cll)}: {cll}")
        2: <Node data=1> => <Node data=2>
        """
        current_node = self.head

        new_node = Node(data)
        new_node.next_ptr = new_node

        if current_node:
            while current_node.next_ptr != self.head:
                current_node = current_node.next_ptr

            current_node.next_ptr = new_node
            new_node.next_ptr = self.head
        else:
            self.head = new_node

        self.length += 1

    def prepend(self, data: Any) -> None:
        """
        Adds a ndoe with given data to the front of the CircularLinkedList
        >>> cll = CircularLinkedList()
        >>> cll.prepend(1)
        >>> cll.prepend(2)
        >>> print(f"{len(cll)}: {cll}")
        2: <Node data=2> => <Node data=1>
        """
        current_node = self.head

        new_node = Node(data)
        new_node.next_ptr = new_node

        if current_node:
            while current_node.next_ptr != self.head:
                current_node = current_node.next_ptr

            current_node.next_ptr = new_node
            new_node.next_ptr = self.head

        self.head = new_node
        self.length += 1

    def delete_front(self) -> None:
        """
        Removes the 1st node from the CircularLinkedList
        >>> cll = CircularLinkedList()
        >>> cll.delete_front()
        Traceback (most recent call last):
        ...
        IndexError: Deleting from an empty list
        >>> cll.append(1)
        >>> cll.append(2)
        >>> print(f"{len(cll)}: {cll}")
        2: <Node data=1> => <Node data=2>
        >>> cll.delete_front()
        >>> print(f"{len(cll)}: {cll}")
        1: <Node data=2>
        """
        if not self.head:
            raise IndexError("Deleting from an empty list")

        current_node = self.head

        if current_node.next_ptr == current_node:
            self.head, self.length = None, 0
        else:
            while current_node.next_ptr != self.head:
                current_node = current_node.next_ptr

            current_node.next_ptr = self.head.next_ptr
            self.head = self.head.next_ptr

        self.length -= 1

    def delete_rear(self) -> None:
        """
        Removes the last node from the CircularLinkedList
        >>> cll = CircularLinkedList()
        >>> cll.delete_rear()
        Traceback (most recent call last):
        ...
        IndexError: Deleting from an empty list
        >>> cll.append(1)
        >>> cll.append(2)
        >>> print(f"{len(cll)}: {cll}")
        2: <Node data=1> => <Node data=2>
        >>> cll.delete_rear()
        >>> print(f"{len(cll)}: {cll}")
        1: <Node data=1>
        """
        if not self.head:
            raise IndexError("Deleting from an empty list")

        temp_node, current_node = self.head, self.head

        if current_node.next_ptr == current_node:
            self.head, self.length = None, 0
        else:
            while current_node.next_ptr != self.head:
                temp_node = current_node
                current_node = current_node.next_ptr

            temp_node.next_ptr = current_node.next_ptr

        self.length -= 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()