line = [1, 2, 3, 'hello', ['test', 10], 'world', True]
# print(len(line))
names = ['Ivanov', 'Petrov', 'Sidorov']
# print(names[0])
# print(line[4][0])
# print(line[0:3])
# print(line[4][:])

line[2] = 'world'
print(line)
line[:2] = [10, 15]
print(line)

# line.append('new')
# line.extend(names)
# line.remove(True)
# line.pop(0)
# line.clear()
print(line)

line2 = ['Ivan', 'Denis', 'Masha', 'Aure']
# line2.sort()
line2 = sorted(line2)
print(line2)
