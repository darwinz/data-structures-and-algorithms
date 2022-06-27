package main;

public class Heap {
  public static void sort(int[] array) {
    int n = array.length;
    for (int i = n / 2 - 1; i >= 0; i--) {
      heapify(array, n, i);
    }
    for (int i = n - 1; i >= 0; i--) {
      int temp = array[0];
      array[0] = array[i];
      array[i] = temp;
      heapify(array, i, 0);
    }
  }

  public void insert(int[] array, int value) {
    int n = array.length;
    array[n] = value;
    int i = n;
    while (i > 0 && array[i] > array[(i - 1) / 2]) {
      int temp = array[i];
      array[i] = array[(i - 1) / 2];
      array[(i - 1) / 2] = temp;
      i = (i - 1) / 2;
    }
  }

  public void delete(int[] array, int i) {
    int n = array.length;
    array[i] = array[n - 1];
    array[n - 1] = 0;
    heapify(array, n - 1, i);
  }

  public static void heapify(int[] array, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    if (left < n && array[left] > array[largest]) {
      largest = left;
    }
    if (right < n && array[right] > array[largest]) {
      largest = right;
    }
    if (largest != i) {
      int temp = array[i];
      array[i] = array[largest];
      array[largest] = temp;
      heapify(array, n, largest);
    }
  }
}
