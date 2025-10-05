"""
Given two numbers represented by linked lists, where each node
contains a single digit, write a function that adds the two
numbers and returns the sum as a linked list. The digits are
stored in reverse order, meaning the 1's digit is at the
head of the list.

Explanation from GeeksForGeeks: https://www.geeksforgeeks.org/dsa/add-number-and-its-reverse-represented-by-linked-list/
"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class ListNode:
    value: int = 0
    next_node: ListNode | None = None


def create_linked_list(values: list[int]) -> ListNode | None:
    """
    Helper function to create a linked list from a list of values.
    """
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:    
        current.next_node = ListNode(value)
        current = current.next_node
    return head


def linked_list_to_list(head: ListNode | None) -> list[int]:
    """
    Helper function to convert a linked list to a list of values.
    """
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next_node
    return values


def sum_linked_lists(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """
    Adds two numbers represented by linked lists and returns the sum as a linked list.

    Args:
        l1: The head of the first linked list.
        l2: The head of the second linked list.
    Returns:
        The head of the linked list representing the sum of the two numbers.
    """
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.value if l1 else 0
        val2 = l2.value if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        current.next_node = ListNode(total % 10)
        current = current.next_node

        if l1:
            l1 = l1.next_node
        if l2:
            l2 = l2.next_node

    return dummy_head.next_node