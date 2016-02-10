def remove_duplicates(num):
    duplicates = []
    counter = {}
    for x in num:
        counter[x]=1
    for key in counter:
        duplicates.append(key)
    return duplicates

print remove_duplicates([1, 1, 1, 4, 5, 3])