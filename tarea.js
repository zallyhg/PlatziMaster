function knowA0(array) {
    let a = 0,
        b = 0,
        c = 0,
        counter = 0;
    if (array[a] > array[b + 1]) {
        c = array[a]
        array[a] = array[b + 1]
        array[b + 1] = c
        a++
        b++
        knowA0()
    } else {
        return console.log(`Ṕosicion de a0: ${c}`)
    }
}