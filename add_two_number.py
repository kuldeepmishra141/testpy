# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def crearNodo(self, val):
        nodo = ListNode(val)
        return nodo

    def insercion(self, head, val):
        nuevoNodo = self.crearNodo(val)

        if not head:
            head = nuevoNodo
        else:
            actual = head
            while actual.next:
                actual = actual.next
            actual.next = nuevoNodo

        return head

    def addTwoNumbers(self, head1, head2):
        head3 = None
        acarreo = 0

        while head1 or head2:
            suma = acarreo
            if head1:
                suma += head1.val
                head1 = head1.next
            if head2:
                suma += head2.val
                head2 = head2.next

            acarreo = suma // 10
            head3 = self.insercion(head3, suma % 10)

        if acarreo > 0:
            head3 = self.insercion(head3, acarreo)

        return head3