function getPropertyStyleVal(val) {
    return getComputedStyle(document.documentElement).getPropertyValue(val);
}

export function setPropertyStyleVal(property, reference) {
    let ref = getPropertyStyleVal(reference);
    document.body.style.setProperty(property, ref);
}

