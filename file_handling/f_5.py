f = open('abc.txt', mode='a+')
f.seek(0)
print(f.read())
f.write("ABC")

f.close()
