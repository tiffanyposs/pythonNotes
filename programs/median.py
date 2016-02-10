def median(num):
    sort = sorted(num)
    if len(sort) % 2 == 0:
        index = (len(sort) / 2) - 1
        return (sort[index] + sort[(index+1)]) / float(2)
    else:
        index = (len(sort) / 2)
        return sort[index]


print(median([4, 5, 5, 4]))