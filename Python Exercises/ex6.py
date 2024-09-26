# Exercise for transforming loops into single-line loops.

text = [ 'Promising', 'yves', 'that', 'home', 'on', 'nobb' ]

for word in text:
    print(word[0])

print("------Solution------")

python = [print(word[0]) for word in text]

# Another way. In one row.
python = [word[0] for word in text]
print(python)
