import os

f=open("Python/sample.txt","wt")
f.write('''The sun dipped below the horizon, casting a warm golden glow across the tranquil meadows. 
        Birds sang their evening melodies as a gentle breeze rustled the leaves. 
        In that moment, all worries seemed to fade, replaced by the beauty of the natural world.''')
f.close()

f=open("Python/sample.txt","at")
f.write('''Birds sang their evening melodies as a gentle breeze rustled the leaves''')
f.close()


f=open("Python/sample.txt","rt")
print(f.read())
# print(f.read(20))
# print(f.readline())
# for i in f.readlines():
#     print(i)

f.close()

if os.path.exists("Python/text.txt"):
    os.remove("Python/text.txt")