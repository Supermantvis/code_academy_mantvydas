'''
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
'''
# shitbat gay ass fuck Solution:
# def sleep_in(weekday, vacation):
#   if not weekday or vacation:
#     return True
#   else:
#     return False
#   This can be shortened to: return(not weekday or vacation)


'''
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
'''
# def monkey_trouble(a_smile, b_smile):
#     if a_smile == b_smile:
#         return True
#     else:
#         return False

# Solution:
# def monkey_trouble(a_smile, b_smile):
#   if a_smile and b_smile:
#     return True
#   if not a_smile and not b_smile:
#     return True
#   return False
  ## The above can be shortened to:
  ##   return ((a_smile and b_smile) or (not a_smile and not b_smile))
  ## Or this very short version (think about how this is the same as the above)
  ##   return (a_smile == b_smile)


'''
Given two int values, return their sum. Unless the two values are the same, then return double their sum.

sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
'''
# def sum_double(a, b):
#     if a != b:
#         return a + b
#     if a == b:
#         return (a + b)*2


# Solution:
# def sum_double(a, b):
#   # Store the sum in a local variable
#   sum = a + b
  
#   # Double it if a and b are the same
#   if a == b:
#     sum = sum * 2
#   return sum


'''
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
'''
# def diff21(n):
#     if n < 21:
#         return abs((21) - (n))
#     else:
#         return abs((21) - (n))*2


'''
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False
'''
# def parrot_trouble(talking, hour):
#     if talking and (hour < 7 or hour > 20):
#         return True
#     else:
#         return False


'''
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True
'''
# def makes10(a, b):
#     if a == 10 or b == 10 or (a + b) == 10:
#         return True
#     else:
#         return False


'''
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
'''
# def near_hundred(n):
#     if abs(n - 100) <= 10 or abs(n - 200) <= 10:
#         return True
#     else:
#         return False


'''
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
'''
# def pos_neg(a, b, negative):
#     if not negative and a < 0 and b > 0 or a > 0 and b < 0:
#         return True
#     else:
#         return False


    # elif not negative and a > 0 and b < 0:
    #     return True
    # elif negative and a < 0 and b < 0:
    #     return False

# GAIDZIU SALYGA HUJOWA batshitas ciulpia
# pydaru Solution:
# def pos_neg(a, b, negative):
#   if negative:
#     return (a < 0 and b < 0)
#   else:
#     return ((a < 0 and b > 0) or (a > 0 and b < 0))


'''
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
# '''
# def not_string(str):
#     if str[:4] != 'not ':
#         return 'not ' + str
#     else:
#         return str
    
# print(not_string('not shit'))

# # str = 'not bybys'
# # print(str[:4])

# Solution:
# def not_string(str):
#   if len(str) >= 3 and str[:3] == "not":
#     return str
#   return "not " + str
#   # str[:3] goes from the start of the string up to but not
#   # including index 3


'''
Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
'''
# def missing_char(str, n):
#     if (len(str)-1) <= n:
#         return str[n]

# shit site solution:
# def missing_char(str, n):
#   front = str[:n]   # up to but not including n
#   back = str[n+1:]  # n+1 through end of string
#   return front + back


'''
Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
'''
# def front_back(str):
#     if len(str)-1 >= 2:
#             sudas

# SOLUTION
# def front_back(str):
#   if len(str) <= 1:
#     return str
  
#   mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
#   # last + mid + first
#   return str[len(str)-1] + mid + str[0]