import random
import time

w = ["apple", "orange", "python", "pineapple", "blueberry"]
n = 1

print("준비가 되었다면 엔터를 누르세요")
input()
start = time.time()

q = random.choice(w)

while n <= 5:
    print("*문제", n)
    print(q)
    x = input()
    if q == x:
        print("통과!")
        n = n+1
        q = random.choice(w)
    else:
        print("오타! 다시 도전")

end = time.time()
et = end - start
et = format(et, ".2f")
print("타자 시간:", et, "초")

