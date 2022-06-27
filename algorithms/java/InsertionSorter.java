package main;

public class InsertionSorter {
  public static void sort(int[] array) {
    int n = array.length;
    for (int i = 1; i < n; i++) {
      int j = i;
      while (j > 0 && array[j] < array[j - 1]) {
        int temp = array[j];
        array[j] = array[j - 1];
        array[j - 1] = temp;
        j--;
      }
    }
  }
}
