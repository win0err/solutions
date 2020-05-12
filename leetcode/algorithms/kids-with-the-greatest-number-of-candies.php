<?php

class Solution {
    /**
     * @param Integer[] $candies
     * @param Integer $extraCandies
     * @return Boolean[]
     */
    function kidsWithCandies(array $candies, int $extraCandies): array
    {
        $maxCandies = max($candies);
        
        $result = [];
        foreach($candies as $c) {
            array_push($result, $c + $extraCandies >= $maxCandies);
        }
        
        return $result;
    }
}