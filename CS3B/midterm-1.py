import re
test1 = "This is a test"
test2 = "A test this is"
test3 = "1st test this is"
test4 = "66"
test5 = "This is test 1 not 2"


if re.match("[Tt]his", test1):            # regex1
   print("This or this")
else:
   print("no match")

if re.match("^This|this", test2):         # regex2
   print("A test this is")
else:
   print("no match")

if re.match(r'^\d\d$', test3):            # regex3
    print('A match test3')
elif re.match(r'^\d\d$', test4):
    print('A match test4')
elif re.match(r'^\d\d$', test5):
    print('A match test 5')
