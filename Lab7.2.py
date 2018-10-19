
str = input("Enter string: ")
str = ''.join(e for e in str if e.isalnum()).lower()

state = False
for i in range(0, len(str) // 2):
  if str[i]!=str[(len(str)-1) - i]:
    break
else:
  state = True

print(state)
