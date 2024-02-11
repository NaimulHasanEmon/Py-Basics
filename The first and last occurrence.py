name = input()

# finds the first appearance of 'f' in the string name
first_idx = name.find('f')


# finds the last appearance of 'f' in the string name
last_idx = name.rfind('f')


if first_idx != last_idx:
    print(first_idx, last_idx)
elif first_idx == -1:
    print()
else:
    print(first_idx)
