line1 = input().strip().lower()
line2 = input().strip().lower()

words1 = set(line1.split())
words2 = set(line2.split())

union = sorted(words1.union(words2))
intersection = sorted(words1.intersection(words2))

print(*union)
print(*intersection)
