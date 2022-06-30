# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 12:27:45 2022

@author: Carla Bailon Rosas
"""

#3. Write a function that can define whether a word is a Palindrome or
#not ( a word, phrase, or sequence that reads the same backwards
#as forwards, e.g. madam)


#word="madam"
#word="hannah"           
def Palindrome(word):
    word=str(word)
    reverse = ''.join(reversed(word))
    if (word == reverse):
        return True
    else:
        return False
    
def Palindrome2(word):
    word=str(word)
    first = 0
    second=len(word)-1
    # traverse the array for the two elements
    while first<second:
        if (word[first] != word[second]):
            return False
            break
        else:
            first += 1
            second -=1
    return True
            
            
            

     
            
#4. Write tests for the newly created Palindrome function. Provide a
#brief explanation for your test case options.

import unittest
from unittest import TestCase, main
from Assesment_2_code_py import Palindrome,Palindrome2

class palindrome_test(TestCase):
    #if a word is palindrome return True:
    def test_ispalindrome(self):
        expected=True
        result=Palindrome(word="madam")
        self.assertEqual(expected, result)
    #if a word is not Palindrome return False
    def test_notPalindrome(self):
        expected=False
        result=Palindrome(word="Rome")
        self.assertEqual(expected, result)
    #if a phrase is not palindrome return False
    def test_PhrasenotPalindrome(self):
        expected=False
        result=Palindrome(word="Flowers for Algernon")
        self.assertEqual(expected, result)
    #if a number is palindrome return True, in this case is false
    def test_numberPalindrome(self):
        expected=False
        result=Palindrome(word=123)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()
    
    
#9. TWO NUMBER SUM:
#● Write a function that takes in a non-empty array of distinct integers
#and an integer representing a target sum. If any two numbers in the
#input array sum up to the target sum, the function should return
#them in an array, in any order. If no to numbers sum up to the target
#sum, the function should return an empty array.
#● Note that the target sum has to be obtained by summing two
#different integers in the array. You cannot add a single integer to
#itself in order to obtain the target sum.
#● You can assume that there will be at most one pair of numbers
#summing up to the target sum.
#Sample Input: numbers = [3, 5, -4 ,8, 11, 1, -1, 6] target_sum = 10
#Sample Output: [-1, 11] the numbers can be in any order, it does not matter.



def sum_twonumbers(my_numbers, target_sum):
    twonumbers=[]
    first=0
    try: 
       for i in range(len(my_numbers)):
           first_num=my_numbers[first]
           others=my_numbers[first+1:len(my_numbers)]
           for i in others:
              sum=i+first_num
              if sum == target_sum:
                twonumbers.append(i)
                twonumbers.append(my_numbers[first])
           else:
               first+=1
               
       return twonumbers
     
    except:
         twonumbers=[]
         return twonumbers

sum_twonumbers(my_numbers = [3, 5, -4 ,8, 11, 1, -1, 6], target_sum = 10)