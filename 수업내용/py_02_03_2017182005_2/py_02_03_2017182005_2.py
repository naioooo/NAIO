def tgoto(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

import turtle as t

for i in range(0,6):
    tgoto(-300, 300 - (i * 100))
    t.fd(500)

t.rt(90)
for i in range(0,6):    
    tgoto(-300 + (i * 100), 300)
    t.fd(500)
    
t.exitonclick()
