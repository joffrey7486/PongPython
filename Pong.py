import turtle

# Plateau de jeu
window = turtle.Screen()
window.title = ("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
score1 = 0
score2 = 0

# Joueur 1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("green")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.penup()
player1.goto(-350, 0)

# Joueur 2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("red")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.penup()
player2.goto(350, 0)

# Balle
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .1
ball.dy = .1

# Affichage 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Joueur1: 0  Joueur2: 0", align="center", font=("Courier", 24, "normal"))

# Fonctions
def player1_up():
    y = player1.ycor()
    y += 20
    player1.sety(y)

def player1_down():
    y = player1.ycor()
    y -= 20
    player1.sety(y)

def player2_up():
    y = player2.ycor()
    y += 20
    player2.sety(y)

def player2_down():
    y = player2.ycor()
    y -= 20
    player2.sety(y)

# Commandes
window.listen()
window.onkeypress(player1_up, "z")
window.onkeypress(player1_down, "s")
window.onkeypress(player2_up, "Up")
window.onkeypress(player2_down, "Down")

while True:
    window.update()

    # Mouvement de la balle
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Collision bord
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Joueur1: {}  Joueur2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("Joueur1: {}  Joueur2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))


    # Collision joueurs
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player2.ycor() + 45 and ball.ycor() > player2.ycor() -45):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < player1.ycor() + 45 and ball.ycor() > player1.ycor() -45):
        ball.setx(-340)
        ball.dx *= -1

    # IA Joueur
    if (player2.ycor() < ball.ycor()) and abs(player2.ycor() - ball.ycor()) > 10:
        player2_up()
    elif (player2.ycor() > ball.ycor()) and abs(player2.ycor() - ball.ycor()) > 10:
        player2_down()