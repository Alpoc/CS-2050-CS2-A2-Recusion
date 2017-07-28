"""Dalton Wiebold"""
import unittest
class palindrome_recursive:
    global main
    main = ('__main__' == __name__)
    
    
    def remove_spaces(self, word):
        if word == None: return None
        if word == "": return word
        if type(word) is not str: raise TypeError("Not a string")
        if len(word) == 1:
            if word[0] == " ":
                return ""
            else:
                return word
        newWord = ''
        if word[0] != " ": 
            return newWord + word[0] + self.remove_spaces(word[1:])
        else:
            return newWord + self.remove_spaces(word[1:])
        
    def palindrome(self, string):
        if string == None:
            return False
        string = self.remove_spaces(string)
        string = self.to_lowercase(string)
        if len(string) == 1 or len(string) == 0:
            return True
        if string[0] == string[-1]:
            string= string[1]
            string = string[:-1]
            return self.palindrome(string)
        else:
            return False   
        if main:
            print stripWord
        return stripWord
    
    
    def to_lowercase(self, lword):
        if lword == None: return None
        if lword == "": return lword
        fchar = lword[0]
        newlWord = ""
        if 'A' <= fchar <= 'Z':
            return newlWord + chr(ord(fchar)-ord('A') + ord('a')) + self.to_lowercase(lword[1:])
        else:
            return newlWord + fchar + self.to_lowercase(lword[1:])
        
        
    

class test_remove_spaces (unittest.TestCase):
    global pr
    pr = palindrome_recursive()
    
    def test_remove_space_none(self):
        self.assertEquals (pr.remove_spaces(None), None)
    def test_remove_space_empty(self):
        self.assertEquals (pr.remove_spaces (""), "")
    def test_remove_space_one(self):
        self.assertEquals (pr.remove_spaces (" "), "")
    def test_remove_space_two(self):
        self.assertEquals (pr.remove_spaces ("  "), "")
    def test_remove_space_inside(self):
        self.assertEquals (pr.remove_spaces ("a b c"), "abc")
    def test_remove_space_before(self):
        self.assertEquals (pr.remove_spaces (" a b c"), "abc")
    def test_remove_space_after(self):
        self.assertEquals (pr.remove_spaces ("a b c "), "abc")
    def test_remove_space_before_and_after(self):
        self.assertEquals (pr.remove_spaces (" a b c "), "abc")

    
    def test_raise_typerror(self):
        self.assertRaises (TypeError, lambda: pr.remove_spaces (1))
        
    # Added my own test to raise type error.
    def test_raise_typerror2(self):
        self.assertRaises (TypeError, lambda: pr.remove_spaces ([123]))
        

class test_palindrome (unittest.TestCase):
    global pr
    pr = palindrome_recursive()
    
    def test_none(self):
        self.assertFalse (pr.palindrome (None))
    def test_empty(self):
        self.assertTrue (pr.palindrome (""))
    def test_one_letter(self):
        self.assertTrue (pr.palindrome ("v"))
    def test_two_letters(self):
        self.assertTrue (pr.palindrome ("vv"))
    def test_toyota(self):
        self.assertTrue (pr.palindrome ("atoyota"))
    def test_toyota_with_spaces(self):
        self.assertTrue (pr.palindrome (pr.remove_spaces ("a toyota")))
    def test_odd_even(self):
        self.assertTrue (pr.palindrome (pr.remove_spaces ("never odd or even")))
    def test_rat(self):
        self.assertTrue (pr.palindrome (pr.remove_spaces ("Was It a Rat I saW")))
    def test_not(self):
        self.assertFalse (pr.palindrome (pr.remove_spaces ("i'm not a palindrome")))
    # Test below i added for removing white spaces and changing to lowercase recursivly
    def test_upper_and_spaces(self):
        self.assertTrue (pr.palindrome ("A mm a"))

class test_to_lowercase(unittest.TestCase):
    # Added these test to test making lower case
    global pr
    pr = palindrome_recursive()
    def test_none(self):
        self.assertEquals (pr.to_lowercase(None), None)
    def test_one_lower(self):
        self.assertEquals (pr.to_lowercase("a"), "a")
    def test_one_upper(self):
        self.assertEquals (pr.to_lowercase("B"), "b")
    def test_multiple_lower(self):
        self.assertEquals (pr.to_lowercase("abcdz"), "abcdz")
    def test_mix(self):
        self.assertEquals (pr.to_lowercase("Hip Replacement"), "hip replacement")
    
if __name__ == '__main__':
    unittest.main()
    
    # testing output
    #pr = palindrome_recursive()
    #pr.remove_spaces("A car a ")
    