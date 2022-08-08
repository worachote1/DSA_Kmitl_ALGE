def isPalindrome(strng):
    if(len(strng)<1):
        return True;

    if(strng[0]!=strng[len(strng)-1]):
        return False;

    return  isPalindrome(strng[1:len(strng)-1])

print(isPalindrome('awesome'));
print(isPalindrome('tacocat'));
print(isPalindrome('amanaplanacanalpanama'));
print(isPalindrome('amanaplanacanalpandemonium'));
# isPalindrome('awesome') # false
# isPalindrome('foobar') # false
# isPalindrome('tacocat') # true
# isPalindrome('amanaplanacanalpanama') # true
# isPalindrome('amanaplanacanalpandemonium') # false