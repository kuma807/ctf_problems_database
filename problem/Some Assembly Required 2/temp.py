text = "xakgKaNs9=8:9l1?im8i<89?00>88k09=nj9kimnu"
ans = ""
ans2 = ""
for i in range(len(text)):
  print(ord(text[i]) - ord("_"))
  if i % 2 == 0:
    ans += str(chr(ord(text[i]) ^ 8))
    ans2 += chr(ord(text[i]) + 8)
    # print(str(chr(ord(text[i]) - 8)))
  else:
    ans += chr(ord(text[i]) ^ 8)
    ans2 += chr(ord(text[i]) - 8)
print(ans)
print(ans2)
print(len(ans), len(ans2))
