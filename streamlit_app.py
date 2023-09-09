#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[1]:


import streamlit as st
import turtle
import pandas as pd
st.title("US State Game")

screen = turtle.Screen()
screen.title("US State Game")
img = "blank_states_img.gif"
screen.addshape(img)
game = turtle.Turtle()
game.shape(img)
score = 0
guessed = []

data = pd.read_csv("50_states.csv")
state_list = data.state.to_list()

while len(guessed) < 50:
    answer = screen.textinput(title=f"{score}/{len(data.state)} States Correct", prompt="What's another state").title()
    if answer in data.values:
        guessed.append(answer)
        state_list.remove(answer)
        score += 1
        ans = turtle.Turtle()
        ans.hideturtle()
        ans.penup()
        correct_st = data[data.state == answer]
        ans.goto(float(correct_st.x), float(correct_st.y))
        ans.write(answer, align="center", font= ("Arial", 8, "normal"))
        
    if answer == "Exit":
        break


# Close the Turtle graphics window if it's open
df = pd.DataFrame(state_list)
df.to_csv("remaining states.csv")

turtle.bye()


# In[3]:


get_ipython().system('jupyter nbconvert --to script streamlit_app.ipynb')

