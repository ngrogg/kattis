#!/usr/bin/python3

stringVal         = str(input())
stringList        = stringVal.split('-')
conCatString      = ""

for it, word in enumerate(stringList):
    conCatString += word[0:1]

print(conCatString)
