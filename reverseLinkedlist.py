class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        to = None
        prev = head
        while hasattr(prev, "next"):
            temp = prev.next
            prev.next = to
            to = prev
            prev = temp
        return to
	def recurseList(prev, to):
		if prev == None:
			return to
		temp = prev.next
		prev.next = to
		return recurseList(temp, prev)