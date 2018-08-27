# Python is about to Ssstrike
# def is_leap(year):
#     if year % 4 == 0: #Checks for divisible by 4 (all must pass)
#         if year % 100 == 0: #Checks for century (all centuries must pass)
#             if year % 400 == 0:
#                       # Checks for divisible by 400 (centuries mustpass)
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False


def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:  # Checks %4 and not century
        return True
    elif year % 4 == 0 and year % 400 == 0:
        # Checks $4 and %400 (built in century check as well)
        return True
    else:
        return False
# Below is a set of tests so you can check if your code is correct.
# Do not copy this part into Vocareum.


def main():

    years = [1944, 2011, 1986, 1956, 1957, 1800, 1900, 1600, 2056]
    answers = [True, False, False, True, False, False, False, True, True]
    check_index = 0
    for y in years:
        print(is_leap(y) == answers[check_index])
        check_index += 1


if __name__ == "__main__":
    main()
