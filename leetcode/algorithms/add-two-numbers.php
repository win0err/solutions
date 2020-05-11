<?php

/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val) { $this->val = $val; }
 * }
 */
class Solution {
    /**
     * @param ListNode $l1
     * @param ListNode $l2
     * 
     * @return ListNode
     */
    function addTwoNumbers(ListNode $l1, ListNode $l2): ListNode
    {
        $current = new ListNode(0);
        $firstNode = $current;
        $head = $current;

        $accumulator = 0;

        while($l1 !== null || $l2 !== null) {
            $number = ($l1->val ?? 0) + ($l2->val ?? 0) + $accumulator;
            $accumulator = (int)$number >= 10;

            if ($number >= 10) {
                $number = $number % 10;
            }

            $current->next = new ListNode($number);
            $current = $current->next;
            
            $l1 = $l1 !== null ? $l1->next : null;
            $l2 = $l2 !== null ? $l2->next : null;
        }

        if($accumulator > 0) {
            $current->next = new ListNode($accumulator);
        }

        $head = $head->next;
        unset($firstNode);
        
        return $head;
    }
}