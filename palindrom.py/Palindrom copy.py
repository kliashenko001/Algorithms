import time
start = time.time()
def is_palindrome(text):
    l = []
    k = txt.lower()
    for i in range(len(k)):
        if k[i] not in (' , . ! ? -'):
            l.append(k[i])
    s = []
    for j in range(len(l) - 1, -1, -1):
        s.append(l[j])
    if l == s:
        return True
    else:
        return False
end = time.time() - start
print(end)



#txt = input()
txt = "Standart - smallest, sell Amstrad nats."

print(is_palindrome(txt))