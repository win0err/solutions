/**
 * The knows API is defined in the parent class Relation.
 * isBadVersion(version: number): boolean {
 *	   ...
 * };
 */

function solution(isBadVersion: any) {
	return (n: number): number => {
		let l = 0, r = n
		let mid: number

		while (l <= r) {
			mid = Math.trunc((r - l) / 2) + l

			if (isBadVersion(mid)) r = mid - 1
			else l = mid + 1
		}

		return l
	}
}
