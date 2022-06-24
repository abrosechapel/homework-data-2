import unittest
from unittest import TestCase, main
from homework4_test import pin_validation,operation,update_balance


class atm_program_ut(TestCase):
    #Validate if the pin is correct:
    def test_pin_validation(self):
        expected="True"
        result=pin_validation(pin_input="1192", pin_code={'1192':["Enrico",100],'1193':["Luciano",2000]})#1192
        self.assertEqual(expected, result)
    #validate the pin doesn't have four digits: 
    def test_pin_validation_len(self):
        expected="False"
        result=pin_validation(pin_input="119", pin_code={'1192':["Enrico",100],'1193':["Luciano",2000]})#119
        self.assertEqual(expected, result)
    #return the balance if the pin is correct --> when it runs in the first input is option 1
    def test_operation(self):
        expected=100
        result=operation(pin_input="1192",pin_code={'1192':["Enrico",100],'1193':["Luciano",2000]},act="y")#y #op 1
        self.assertEqual(expected, result)
    #if the option yes or no is incorrect 
    def test_operation_act(self):
        expected="transaction can't be done"
        result=operation(pin_input="1192",pin_code={'1192':["Enrico",100],'1193':["Luciano",2000]}, act=20)
        self.assertEqual(expected, result)
    #if the withdraw is more than balance--> when it runs in the second input use option 2 and amount 120
    def test_operation_balance(self):
        expected="The withdraw is more than the balance,transaction can't be done"
        result=operation(pin_input="1192", pin_code={'1192':["Enrico",100],'1193':["Luciano",2000]}, act="y")#y #op 2 #120
        self.assertEqual(expected, result)
    #if the balance is less than 0
    def test_operation_balance_neg(self):
        expected="incorrect ammount, You can't do an operation"
        result=operation(pin_input="1193", pin_code={'1192':["Enrico",100],'1193':["Luciano",-10]}, act="y")#y #op 1
        self.assertEqual(expected, result)



if __name__ == '__main__':
    main()