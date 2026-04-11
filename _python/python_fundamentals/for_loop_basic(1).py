#1.basic
for i in range(1,151):
    print(i)

#2. Multiples of 5
for i in range(5,1001,5):
    print(i)

#3. the Dojo Way
for i in range(1, 101):
    if i % 5 == 0:
        print("Coding")
    elif i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)

#4. Whoa. That Sucker's Huge
sum = 0

for i in range(0, 500001):
    if i % 2 != 0:
        sum += i
print(sum)

#5. Countdown by Four
for i in range(2018, 0, -4):
    print(i)

#6. Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)