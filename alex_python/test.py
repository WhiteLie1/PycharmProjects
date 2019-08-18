#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/6/16 19:45
# @Author : chenxin
# @Site : 
# @File : test.txt.py
# @Software: PyCharm
import pygame,random,time,turtle,multiprocessing

'''def music_play():
    pygame.mixer.init()
    music_name=str(random.randint(1,3))+'.mp3'
    pygame.mixer.music.load(''% music_name)
    pygame.mixer.music.play(start=1.0)
    time.sleep(120)
    pygame.mixer.music.stop()
'''
def draw_arc(lv):
    for i in range(20):
        lv.right(10)
        lv.forward(2)

def draw_love(x,y):
    love = turtle.Turtle()
    love.hideturtle()
    love.up()
    love.goto(x,y)
    love.color('red','pink')
    love.speed(100000000)
    love.pensize()
    love.pensize(2)
    # 开始画爱心lalala
    love.down()
    love.begin_fill()
    love.left(140)
    love.forward(22)
    draw_arc(love)
    love.left(120)
    draw_arc(love)
    love.forward(22)
    love.write("Dad", font=("Arial", 12, "normal"), align="center")  # 写上表白的人的名字
    love.left(140)  # 画完复位
    love.end_fill()

def tree(branchLen, t):
    if branchLen > 5:  # 剩余树枝太少要结束递归
        if branchLen < 20:  # 如果树枝剩余长度较短则变绿
            t.color("green")
            t.pensize(random.uniform((branchLen + 5) / 4 - 2, (branchLen + 6) / 4 + 5))
            t.down()
            t.forward(branchLen)
            draw_love(t.xcor(), t.ycor())  # 传输现在turtle的坐标
            t.up()
            t.backward(branchLen)
            t.color("brown")
            return
        t.pensize(random.uniform((branchLen + 5) / 4 - 2, (branchLen + 6) / 4 + 5))
        t.down()
        t.forward(branchLen)
        # 以下递归
        ang = random.uniform(15, 45)
        t.right(ang)
        tree(branchLen - random.uniform(12, 16), t)  # 随机决定减小长度
        t.left(2 * ang)
        tree(branchLen - random.uniform(12, 16), t)  # 随机决定减小长度
        t.right(ang)
        t.up()
        t.backward(branchLen)
def draw_main():
    Win=turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(100000000)
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("brown")
    t.pensize(32)
    t.forward(60)
    tree(100, t)
    Win.exitonclick()

if __name__=='__main__':
    process1 = multiprocessing.Process(target=draw_main)
    #process2 = multiprocessing.Process(target=music_play())
    process1.start()
    #process2.start()