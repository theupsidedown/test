# teststr = 'Mary had a little lamb and little'
# fetch = 'little'
#
# print(teststr.find(fetch, teststr.find(fetch) + 1))
# i = 0
# for c in teststr:
#     #print(i, c)
#     i = i + 1

# x = 383.89327
# strx = str(x)
# after = strx[strx.find('.') + 1]
# before = strx[0:strx.find('.')]
# print(after)
# print(before)
# if int(after) < 5:
#     print(before)
# else:
#     print(int(before) + 1)

# marker = "AFK"
# replacement = "away from keyboard"
# line = "I will now go to sleep and be AFK until lunch time tomorrow."
#
# len_marker = len(marker)
# pos_marker = line.find(marker)
# replaced = line[:pos_marker] + replacement + line[pos_marker + len_marker:]
# print(replaced)

# # word = 'adaM'
# # rev_word = word[::-1]
# # print(rev_word.find(word))
#
#
# a = 10
# b = 20
#
# # def find_second(teststr, targetstr):
# #     return teststr.find(targetstr, teststr.find(targetstr) + 1)
# #
# # def stamps(num):
# #     fives, twos, ones = 0, 0, 0
# #     fives = num // 5
# #     num = num % 5
# #     twos = num // 2
# #     num = num % 2
# #     ones = num
# #     return  fives , twos, ones
# #
# # print (stamps(5))
#
# def biggest(a, b, c):
#     max = a
#     if b > max:
#         max = b
#     if c > max:
#         max = c
#     return max
#
#
# def least(a, b, c):
#     min = a
#     if min > b:
#         b = min
#     if min > c:
#         min = c
#     return min
#
#
# def set_range(a, b, c):
#     # Your code here
#     return biggest(a, b, c) - least(a, b, c)
#
#
# print(set_range(10, 2, 7) )

# teststr = "telegram"
# t = 'telegram'
# def func(teststr,t):
#     i = 0
#     while True:
#         if teststr.find(t[i]) == -1:
#             return False
#         i = i + 1
#         if i == len(t):
#             return True
# r = func(teststr,t)
# print(r)


def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    if month == 12 and day == 30:
        year += 1
        month = 1
        day = 1
    elif day == 30:
        month += 1
        day = 1
    else:
        day += 1
    return year, month, day

nextDay(1999,12,30)


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    # YOUR CODE HERE!
    days = 0
    while year1 != year2 and day1 != day2 and month1 != month2:
        year1, month1, day1 = nextDay(year1, month1, day1)
        print (year1, month1, day1)
        days += 1
    return days
print (daysBetweenDates(2012,9,30,2012,10,30))








