interface TreeNode {
    val: number,
    left: TreeNode | null,
    right: TreeNode | null,
}

type SerializedNode = string


function findDuplicateSubtrees(root: TreeNode | null): Array<TreeNode> {
    const counter: Record<SerializedNode, { root: TreeNode, count: number }> = {}
    const traverse = (node: TreeNode | null): SerializedNode => {
        if (node === null) return 'nil'

        const serialized = `${node.val}|${traverse(node.left)}|${traverse(node.right)}`
        if (!counter[serialized]) {
            counter[serialized] = {
                root: node,
                count: 1,
            }
        } else {
            counter[serialized].count++
        }

        return serialized
    }

    traverse(root)

    return Object.values(counter)
        .filter(({ count }) => count > 1)
        .map(({ root }) => root)
}
