package main;

public class BubbleSorter {
  public static void sort(int[] array) {
    int n = array.length;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n - 1; j++) {
        if (array[j] > array[j + 1]) {
          int temp = array[j];
          array[j] = array[j + 1];
          array[j + 1] = temp;
        }
      }
    }
  }
}
