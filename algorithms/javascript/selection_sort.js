function indexOfMin(list) {
    var minIndex = 0;
    for(var i = 0; i < list.length; i++) {
        if (list[i] < list[minIndex]) {
            minIndex = i;
        }
    }
    return minIndex;
}
function selectionSort(list) {
    var sortedList = [];
    while(list.length > 0) {
        var indexToMove = indexOfMin(list);
        sortedList.push(list.splice(indexToMove, 1)[0]);
    }
    return sortedList;
}

const testValues = [29, 100, 1, 2, 57, 28, 88, 3, 50, 67, 37, 1, 32, 20];
var sorted = selectionSort(testValues);
console.log(sorted);
