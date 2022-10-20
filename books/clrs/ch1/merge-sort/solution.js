const mergeSort = (list) => {
    if (list.length <= 1) return list

    const mid = Math.floor(list.length/2)

    // in-place sort in merge_sort.c
    const left = sort(list.slice(0, mid))
    const right = sort(list.slice(mid, list.length))

    let i = 0, l = 0, r = 0
    while (l < left.length && r < right.length) {
        if (left[l] < right[r]) {
            list[i] = left[l]
            l++
        } else {
            list[i] = right[r]
            r++
        }

        i++
    }

    while (l < left.length) {
        list[i] = left[l]
        l++
        i++
    }

    while (r < right.length) {
        list[i] = right[r]
        r++
        i++
    }

    return list
}


const list = [-2, 99, 0, -743, 2, 3, 4]
sort(list)

console.log(JSON.stringify(list))
