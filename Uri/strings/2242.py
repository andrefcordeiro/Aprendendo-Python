# Huaauhahhuahau

def isPalindrome(string):
    i = 0
    tam = len(string)

    while i < tam/2:
        if string[i] != string[tam-i-1]:
            return 0
        i += 1
    return 1


vogais = "aeiou"
v = [] #vetor de vogais presentes a risada
s = input()

for i in range(0, len(s)):
    if s[i] in vogais:# se é vogal
        v.append(s[i])

if isPalindrome("".join(v)):
    print("S")
else:
    print("N")
