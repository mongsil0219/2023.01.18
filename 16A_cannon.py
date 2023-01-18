import turtle as t
import random

def turn_up():  #위에 키 눌렀을 때 호출되는 함수
    t.left(2) #거북이를 왼쪽으로 2도 돌림
    
def turn_down(): #아래 키 눌렀을 때 호출되는 함수
    t.right(2) #거북이를 오른쪽으로 2도 돌림

def fire():  #스페이스바 눌렀을 때 호출되는 함수
    ang = t.heading()  #현재 거북이가 바라보는 각도를 기억
    while t.ycor() > 0:  #거북이가 땅 위에 있는 동안 반복
        t.forward(15)  #15만큼 앞으로 이동
        t.right(5)  #오른쪽으로 5도 회전

    d = t.distance(target, 0)  #거북이와 목표 지점과의 거리를 구함
    t.sety(random.randint(10,100)) #성공 또는 실패를 표시할 위치를 지정
    if d < 25: #거리 차이가 25보다 작으면  명중한 것으로 처리
        t.color("blue")
        t.write("Good!", False, "center", ("",15))
    else:  #25보다 멀면 실패 처리
        t.color("red")
        t.write("Bad!", False, "center", ("",15))
    t.color("black") #거북이 색을 검은색으로 되돌림
    t.goto(-200, 10) #거북이 위치를 처음 발사했던 곳으로 되돌림
    t.setheading(ang) #각도돋 처음 기억해둔 각도로 되돌림

#땅 그리기
t.goto(-300,0)
t.down()
t.goto(300,0)

#목표지점을 설정하고 그림
target = random.randint(50,150) #목표 지점을 50~150 사이에 있는 임의의 수로 지정

t.pensize(3)
t.color("green")
t.up()
t.goto(target - 25,2)
t.down()
t.goto(target +25, 2)

#거북이 색을 검은색으로 지정하고 처음 발사했던 곳으로 되돌립니다.
t.color("black")
t.up()
t.goto(-200,10)
t.setheading(20)

#거북이가 동작하는 데 필요한 설정
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")

t.listen()
