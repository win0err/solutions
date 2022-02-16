<?php

class Solution {
    /**
     * @param int[] $nums
     * @param int   $target
     *
     * @return int[]
     *
     * @throws \InvalidArgumentException
     */
    function twoSum(array $nums, int $target): array
    {
        $memo = [];

        foreach($nums as $position => $number) {
            $lookingFor = $target - $number;

            if(isset($memo[$lookingFor])) {
                return [$memo[$lookingFor], $position];
            }

            $memo[$number] = $position;
        }

        throw new \InvalidArgumentException("No solution");
    }
}