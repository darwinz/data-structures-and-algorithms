package main;

public class Node {
  public int data;
  public Node next;

  public Node(int data) {
    this.data = data;
  }

  public static Node setNext(Node next) {
    this.next = next;
    return this;
  }

  public String toString() {
    return String.valueOf(data);
  }
}

