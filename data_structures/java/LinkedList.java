package main;

public class LinkedList {
  public Node head;
  public Node tail;

  public LinkedList() {
    head = null;
    tail = null;
  }

  public void insert(int data) {
    Node node = new Node(data);
    if (head == null) {
      head = node;
      tail = node;
    } else {
      tail.next = node;
      tail = node;
    }
  }

  public void insertAt(int data, int index) {
    Node node = new Node(data);
    if (index == 0) {
      node.next = head;
      head = node;
    } else {
      Node current = head;
      for (int i = 0; i < index - 1; i++) {
        current = current.next;
      }
      node.next = current.next;
      current.next = node;
    }
  }

  public void insertAfter(int data, int target) {
    Node node = new Node(data);
    Node current = head;
    while (current.data != target) {
      current = current.next;
    }
    node.next = current.next;
    current.next = node;
  }

  public void insertBefore(int data, int target) {
    Node node = new Node(data);
    Node current = head;
    while (current.next.data != target) {
      current = current.next;
    }
    node.next = current.next;
    current.next = node;
  }

  public void delete(int index) {
    if (index == 0) {
      head = head.next;
    } else {
      Node current = head;
      for (int i = 0; i < index - 1; i++) {
        current = current.next;
      }
      current.next = current.next.next;
    }
  }

  public void print() {
    Node node = head;
    while (node != null) {
      System.out.print(node.data + " ");
      node = node.next;
    }
    System.out.println();
  }

  public void reverse() {
    Node node = head;
    Node prev = null;
    Node next = null;
    while (node != null) {
      next = node.next;
      node.next = prev;
      prev = node;
      node = next;
    }
    head = prev;
  }

  public void reverseRecursive() {
    head = reverseRecursive(head);
  }

  private Node reverseRecursive(Node node) {
    if (node == null || node.next == null) {
      return node;
    }
    Node next = node.next;
    node.next = null;
    Node newHead = reverseRecursive(next);
    next.next = node;
    return newHead;
  }
}
