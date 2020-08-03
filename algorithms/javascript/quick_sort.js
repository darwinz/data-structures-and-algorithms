function quicksort(values) {
    if (values.length <= 1) {
        return values
    }
    var lessThanPivot = [];
    var greaterThanPivot = [];
    var pivot = values[0];
    for (var i = 1; i < values.length; i++) {
        if (values[i] <= pivot) {
            lessThanPivot.push(values[i]);
        } else {
            greaterThanPivot.push(values[i]);
        }
    }
    return quicksort(lessThanPivot).concat(pivot, quicksort(greaterThanPivot));
}


const testValues = [32, 100, 1, 2, 29, 28, 88, 3, 50, 67, 37, 1, 57, 20];
var sorted = quicksort(testValues);
console.log(sorted);
