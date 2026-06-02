str = input()
answer = ""
for c in str:
    if ord(c)<90:
        answer+=c.lower()
    else: answer += c.upper()
print(answer)