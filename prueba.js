let counter = 0
let array = [5, 3, 4, 1, 2]

function sort(array) {
    for (let a = 0; a < array.length; a++) {
        for (let b = 0; b < array.length; b++) {
            if (array[b] > array[b + 1]) {
                let aux = array[b]
                array[b] = array[b + 1]
                array[b + 1] = aux
            }
        }
    }
}

sort(array)