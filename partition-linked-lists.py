"""
Partitions a linked list around a value x such that all nodes less than x come before
nodes greater than or equal to x. The original relative order of the nodes in each
partition should be preserved. The partition value x can appear anywhere in the "right
partition" and it does not need to appear between the left and right partitions.

Explanation from GeeksforGeeks: https://www.geeksforgeeks.org/dsa/partitioning-a-linked-list-around-a-given-value-and-keeping-the-original-order/
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


def partition_linked_list(head: ListNode | None, partition: int) -> ListNode | None:
    """
    Args:
        head: The head of the linked list.
        x: The partition value.

    Returns:
        The head of the partitioned linked list.
    """
    if head is None:
        return None

    if head.next_node is None:
        return head

    left_head = ListNode(0)  # Dummy head for the left partition
    right_head = ListNode(0)  # Dummy head for the right partition
    left = left_head
    right = right_head

    current: ListNode | None = head
    while current:
        if current.value < partition:
            left.next_node = current
            left = current
        else:
            right.next_node = current
            right = current
        current = current.next_node

    right.next_node = None  # Terminate the right partition
    left.next_node = right_head.next_node  # Connect the two partitions

    return left_head.next_node  
