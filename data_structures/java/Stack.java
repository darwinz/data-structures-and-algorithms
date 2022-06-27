package main;

public class Stack {
  public Node head;
  public Node tail;

  public Stack() {
    head = null;
    tail = null;
  }

  public void push(int data) {
    Node node = new Node(data);
    if (head == null) {
      head = node;
      tail = node;
    } else {
      node.next = head;
      head = node;
    }
  }

  public int pop() {
    int data = head.data;
    head = head.next;
    return data;
  }

  public int peek() {
    return head.data;
  }

  public boolean isEmpty() {
    return head == null;
  }
}
