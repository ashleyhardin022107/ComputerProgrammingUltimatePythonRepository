def count_falling_grades(items):
    count = 0
    for number in items:
        if number < 60:
            count = count + 1

    return count

inputlist = [89, 54, 67, 49, 93]
returnvalue = count_falling_grades(inputlist)
print(returnvalue)


def count_act_scores(items):
    count = 0
    for number in items:
        if number >= 1 and number <= 36:
            count = count + 1
    
    return count

inputlist = [28, 17, 32, 48, 62, 22]
returnvalue = count_act_scores(inputlist)
print(returnvalue)


def number_sum(items):
    total = 0
    for number in items:
        total = total + number

    return total

inputlist = [3, 5, 5]
returnvalue = number_sum(inputlist)
print(returnvalue)


def average_act_score(items):
    total = 0
    for number in items:
        if number >= 1 and number <= 36:
            total = total + 1
        else:
