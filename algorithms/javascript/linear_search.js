function indexOfItem(collection, target) {
    for (var i = 0; i < collection.length; i++) {
        if (collection[i] === target) {
            return i;
        }
    }
    return null;
}


const names = ["Francina Vigneault", "Lucie Hansman", "Nancie Rubalcaba", "Elida Sleight"];
var index = indexOfItem(names, "Lucie Hansman");
console.log(index);
