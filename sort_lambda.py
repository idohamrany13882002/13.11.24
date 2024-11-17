l1: list[int] = [89, 91, 23, 34, 15, 98, 71, 99, 101]
l2: list[str] = ["a b c", "z b", "x y", "z" ]

print(sorted(l1, key=lambda x: (x%10, x)))
print(sorted(l2, key=lambda w: len(w)))