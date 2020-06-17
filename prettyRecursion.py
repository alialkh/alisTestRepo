
import turtle
# 30 -> 15 -> 0
# 100 -> 85 -> 70 -> 55 -> 40 -> 25 -> 10 -> -5
def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-5,t)
        t.left(40)
        tree(branchLen-5,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(100,t)
    t.speed(1000)
    myWin.exitonclick()
main()


# def alisFunction():
#     print(f"this is alis function")
#     alisFunction()
#
# alisFunction()
