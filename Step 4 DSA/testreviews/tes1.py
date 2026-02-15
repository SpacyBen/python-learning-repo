def checkdupe(dups):
    n = len(dups)
    seen = set()
    dupes = []
    for i in range(n):
        if dups[i] in seen:
            dupes.append(dups[i])
            dups.remove(dups[i])
        else:
            seen.add(dups[i])
    return ("No Duplicate" if not dupes else dupes)
        
        



nums = [1, 2, 3, 3]
print(checkdupe(nums))
print(nums)
