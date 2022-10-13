lst = [1, 2, [5, [9, 10, 11, 12], 6, 7, 8], 4]

print(f"\nFirst two elements of the within the original list: {lst[2][:2]}\n")

print(f"Last three elements of the list within a list whithin a list: {lst[2][1][1:5]}\n")

print(f"List backwards: {lst[::-1]}\n")