module.exports = function (cities) {
    const createGraph = (cities) => {
        const destinations = cities.reduce(
            (dsts, city) => {
                const firstChar = city[0].toLowerCase()
                if (!dsts.has(firstChar)) dsts.set(firstChar, [])

                dsts.get(firstChar).push(city)

                return dsts
            },
            new Map(),
        )

        return cities.reduce(
            (graph, city) => {
                let lastChar = city[city.length-1].toLowerCase()
                if (lastChar === 'ъ' || lastChar === 'ь') {
                    lastChar = city[city.length-2].toLowerCase()
                }

                if (destinations.has(lastChar)) {
                    graph.set(city, destinations.get(lastChar))
                }

                return graph
            },
            new Map(),
        )
    }


    const topologicalSort = (graph) => {
        const path = []
        const visited = new Set()

        const dfs = (start) => {
            if(visited.has(start)) return;

            visited.add(start)

            if (graph.has(start)) {
                graph.get(start).forEach(dfs)
            }

            path.unshift(start)
        }

        for (const node of graph.keys()) {
            dfs(node)
        }

        return path
    }

    return topologicalSort(createGraph(cities))
}
