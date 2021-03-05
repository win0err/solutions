function calcFontSize(container, str, min, max) {
    const header = document.createElement('span');
    header.innerText = str;
    container.append(header);
    
    const containerSizes = container.getBoundingClientRect();

    let result = null;
    // TODO: Binary search
    for (let size = min; size < max; size++) {
        header.style.fontSize = `${size}px`;

        const headerSizes = header.getBoundingClientRect();
        if (headerSizes.width < containerSizes.width && 
            headerSizes.height < containerSizes.height ) {
                result = size;
            } else {
                break;
            }
    }

    return result;
}