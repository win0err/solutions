<?php

/**
 * Insertion sort algorithm
 *
 * @param array $A
 * @return void
 */
function insertion_sort(array &$A): void 
{
    for ($j = 1; $j < sizeof($A); $j++) { 
        $key = $A[$j];

        $i = 0;
        for ($i = $j - 1; $i >=0 && $i > $key; $i--) {
            $A[$i + 1] = $A[$i];
        }

        $A[$i + 1] = $key;
    }
}


$nums = [-2, 99, 0, -743, 2, 3, 4];
insertion_sort($nums);

echo json_encode($nums);