# строка это неизменяемая последовательность
s = 'hello'
print(len(s)) # 5
print(s.capitalize()) # Hello
print(s.center(20)) #       hello       
print(s.count('l')) # 2
print(s.replace('l', 't')) # hetto
s2 = 'hello, world'
print(s2.split(',')) # ['hello', 'world']
print(s2.split()) # ['hello,', 'world']

print(s2.isdigit()) # состоит ли из цифр false
print(s2.isalpha()) # состоит ли из букв false (space , )
print(s2.isalnum()) # состоит ли из цифр или слов false (space , )
print(s2.islower()) # rue
print(s2.isupper()) # false


