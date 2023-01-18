import random

def make_question():
    a = random.randint(1,10)
    b = random.randint(1,10)
    c = random.randint(1,3)

    question_num = c
    
    if question_num == 1:
        return f"{a}+{b}"
    elif question_num == 2:
        return f"{a}-{b}"
    elif question_num == 3:
        return f"{a}*{b}"


sc1 = 0
sc2 = 0

print("계산 맞히기 게임을 시작합니다")

for x in range(5):
    question = make_question()
    print(question)
    answer = input("=")
    d = int(answer)

    if eval(question) == d:
        print("정답입니다")
        sc1 = sc1 + 1
    else:
        print("오답입니다")
        sc2 = sc2+1

print("정답 횟수 : ",sc1, "오답 횟수: ", sc2)
if sc2 == 0:
    print("당신은 천재입니다!")

        
        
