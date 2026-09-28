import random
import turtle

ventana = turtle.Screen()    
ventana.title("Carrrea de Caracoles")
ventana.bgcolor("orange")
ventana.setup(width=800, height=600)


caracol1 = turtle.Turtle()
caracol1.shape("turtle")
caracol1.color("red")     #Color tortuga
caracol1.penup()     
caracol1.goto(-350,-50)   #coordenadas



caracol2 = turtle.Turtle()
caracol2.shape("turtle")
caracol2.color("white")     #Color tortuga
caracol2.penup()     
caracol2.goto(-350,50)   #coordenadas

meta = 300

#Linea de meta
meta_linea = turtle.Turtle()
meta_linea.penup()
meta_linea.goto(meta, 150)
meta_linea.pendown()
meta_linea.goto(meta, -150)
meta_linea.hideturtle()





while True:
    avance_caracol_1 = random.randint(1,20)
    avance_caracol_2 = random.randint(1,20)


    if avance_caracol_1 % 2 == 0 and avance_caracol_2 % 2 == 0:
        continue 

    caracol1.forward(avance_caracol_1)    
    caracol2.forward(avance_caracol_2)

    print(f"El caracol 1 avanzo: {avance_caracol_1} , con total de avance {caracol1.xcor()} ")
    print(f"El caracol 2 avanzo: {avance_caracol_2} , con total de avance {caracol2.xcor()} ")
    print("--------------------------------------------------------------------------")
    if caracol1.xcor() >= meta or caracol2.xcor() >= meta:
        break


if caracol1.xcor() >= caracol2.xcor():
    print("Felicidades  Caracol 1 GANASTE")
elif caracol2.xcor() > caracol1.xcor():
    print("Felicidades Caracol 2 GANASTE")
else:
    print("Empate")


ventana.exitonclick()