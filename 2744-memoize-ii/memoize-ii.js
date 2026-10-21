function memoize(fn) {
const cache = new Map();


return function (...args) {
    let currentMap = cache;

    for (const arg of args) {
        if (!currentMap.has(arg)) {
            currentMap.set(arg, new Map());
        }

        currentMap = currentMap.get(arg);
    }

    if (currentMap.has("result")) {
        return currentMap.get("result");
    }

    const result = fn.apply(this, args);
    currentMap.set("result", result);

    return result;
};


}
