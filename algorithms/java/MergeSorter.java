package main;

public class MergeSorter {
  public static void sort(int[] array) {
    int[] temp = new int[array.length];
    sort(array, temp, 0, array.length - 1);
  }

  private static void sort(int[] array, int[] temp, int left, int right) {
    if (left < right) {
      int mid = (left + right) / 2;
      sort(array, temp, left, mid);
      sort(array, temp, mid + 1, right);
      merge(array, temp, left, mid, right);
    }
  }

  private static void merge(int[] array, int[] temp, int left, int mid, int right) {
    int i = left;
    int j = mid + 1;
    int k = left;
    while (i <= mid && j <= right) {
      if (array[i] < array[j]) {
        temp[k++] = array[i++];
      } else {
        temp[k++] = array[j++];
      }
    }
    while (i <= mid) {
      temp[k++] = array[i++];
    }
    while (j <= right) {
      temp[k++] = array[j++];
    }
    for (int l = left; l <= right; l++) {
      array[l] = temp[l];
    }
  }
}
