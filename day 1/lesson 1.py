from turtle import *


#we want to painte a house
#step 1: draw e square

width(7)


color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#and of spuare

#drawing a door

forward(70) 
color("yellow")
left(90)        
forward(120)      #height of door       
right(90)  
forward(60)
right(90)
forward(120)

penup()
goto(200,200)
pendown()


color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()