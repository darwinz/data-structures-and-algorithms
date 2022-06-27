package main;

public class Queue {
  public Node head;
  public Node tail;

  public Queue() {
    head = null;
    tail = null;
  }

  public void enqueue(int data) {
    Node node = new Node(data);
    if (head == null) {
      head = node;
      tail = node;
    } else {
      tail.next = node;
      tail = node;
    }
  }

  public int dequeue() {
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
