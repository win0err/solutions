const palindrome = (str) => { 
    const chars = str.trim().split('').filter(ch => ch !== ' ')

    return chars === chars.reverse()
}


export default {
    palindrome,
}