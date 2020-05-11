<?php

class Solution {

    /**
     * @param Integer[][] $A
     * @return Integer[][]
     */
    function transpose(array $A): array
    {
        $rows = count($A);
        $columns = count($A[0]);
        $T = [];
        
        for($r = 0; $r < $rows; $r++) {
            for($c = 0; $c < $columns; $c++) {
                $T[$c][$r] = $A[$r][$c];
            }
        }
                
        return $T;
    }
}