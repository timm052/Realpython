# lists of lists
def enrollment_stats(uni_list):
    # create temp lists to collect the enrollment and fees from
    # the university data set
    temp_enrol = []
    temp_fees = []

    # takes list of unis and sorts into indervidual lists for fees and students
    for uni in uni_list:
        temp_enrol.append(uni[1])
        temp_fees.append(uni[2])

    return temp_enrol, temp_fees


def mean(numbers):
    temp_mean = 0

    # sum of list contents
    for i in numbers:
        temp_mean += i

    # number of values
    num_value = len(numbers)

    # calculate averages
    return int(temp_mean / num_value)


def median(numbers):
    # find length of list
    length = len(numbers)

    # sort numbers highest to lowest
    numbers.sort()

    # takes the middle number in list of median
    # if no single middle number exists then averages the two middle values
    # to find median
    if length % 2 != 0:
        median = numbers[round((((length + 1) / 2) - 1))]
    else:
        t1 = numbers[(length / 2) - 0.5]
        t2 = numbers[length / 2 - 1.5]
        median = (t1 + t2) / 2

    return int(median)


def sum_num(lis):
    temp = 0

    for i in lis:
        temp += i

    return temp


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

totals = enrollment_stats(universities)
# print(totals)

print("*************************")
print(f"Total students:   {sum_num(totals[0])}")
print(f"Total tuition:  $ {sum_num(totals[1])}\n")
print(f"Student mean:     {mean(totals[0])}")
print(f"Student median:   {median(totals[0])}\n")
print(f"Tuition mean:     {mean(totals[1])}")
print(f"Tuition median:   {median(totals[1])}")
print("*************************")
