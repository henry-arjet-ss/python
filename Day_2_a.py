print("Hello World"[8])
print("thinker"[slice(2, 5)])
print("hello"[1])
print("Sammy"[2:])
miss = ""
for c in set("Mississippi"):
    miss += c
print(miss)

def checkPal(inString):
    inString = inString.lower()
    cleanString = list(filter(lambda c: c not in ('!', ' ', '?', '.', '"', "'", ',', ':', ';', '(', ')'), inString))
    for i in range(len(cleanString)//2):
        if cleanString[i] != cleanString [-1 - i]:
            return False
    return True

pals = []
n = int(input("Input data:\n"))
for i in range (n):
    pals.append(input())
results = ""
for s in pals:
    if checkPal(s):
        results += "Y "
    else:
         results += "N "

print(results)
