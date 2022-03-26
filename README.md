
**BACKEND.

I have executed a vigenere cipher algorithm using python3.6 programming language and pycharm community IDE. The algorithm has 3 sets of functions that:
 1)**create key.
 2)encrypts the source text.
 3)decrypts the encrypted text back to source text.

In the first function(create key),two arguments(string and key) are called.Since vigenere cipher is polyalphabet cryptographic,our key is not assigned one character but it is assigned a word with more than one character. 

Here we introduce the use of '**CONDITIONAL STATEMENT'- IF.

IF statement compares the length of the string and the length of the keyword then prints the key if both string and keyword are for instance,4 letters long each.For example, if our string says, 'is long' and our keyword says, 'shorter' the algorithm prints out the key because both keyword and string are of same number of characters.
Note:**LINE BREAKS and or WHITESPACES ARE COUNTED AS CHARACTERS.

Else when the if condition,is not met that is the length of string and length of keyword vary, the program goes ahead to get the difference in the lengths of string and keyword.if string is 7 characters long and keyword is 4 characters long,then the difference in their lengths is 3characters.This means that the loop will be iterated 3times. 

In the second function(encrypt text),we will assign variable X, the ordered string and ordered key iterations which go through 26 rows of alphabet A to z. The variable X will keep incrementing by 1,if say order starts from A.The value is then allocated to encrypted text.

In the third function(decrypt text), what had been encrypted, will go through the reverse process of encryption so as to return to the source or original text.


**GETTING STARTED:

To test and run this project, you are required to clone the project in your local machine, install all the dependencies like pycharm community edition IDE, python 3.6 and then execute the related COMMANDS on python shell.Also,note that when whitespaces and line breaks occur,the program automatically fills them with characters denoting the use of strips or replace functions.


**BUILT USING:
Python version 3.6 programming language.

**BRANCHES IN USE:

Master branch:

**Author:

edna-harriet : Harriet Auma Odima.

**Acknowledgement:

Challenge proposed by education@distributedlab.com


