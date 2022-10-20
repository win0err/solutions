const insertionSort = (list) => {
    for (let i = 1; i < list.length; i++) {
        let current = list[i]

        let j
        for (j = i-1; j >= 0 && list[j] >= current; j--) {
            list[j+1] = list[j];
        }

        list[j+1] = current
    }
}


const list = [-2, 99, 0, -743, 2, 3, 4]
sort(list)

console.log(JSON.stringify(list))