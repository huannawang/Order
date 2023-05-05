# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 11:48:25 2022

@author: 王
"""

def order_appetizer():
    choose = int(input("(1)凱薩莎拉 (2)鮮蝦蘆筍 (3)水果沙拉, 請選一道開胃菜 : "))
    if(choose == 1):
        print("你點的開胃菜是凱薩莎拉")
        return "凱薩莎拉"
    elif(choose == 2):
        print("你點的開胃菜是鮮蝦蘆筍")
        return "鮮蝦蘆筍"
    elif(choose == 3):
        print("你點的開胃菜是水果沙拉")
        return "水果沙拉"

def order_soup():
    choose = int(input("(1)香菇雞肉湯 (2)鮮魚湯 (3)牛肉湯, 請選一道湯品: "))
    if(choose == 1):
        print("你點的湯品是香菇雞肉湯")
        return "香菇雞肉湯"
    elif(choose == 2):
        print("你點的湯品是鮮魚湯")
        return "鮮魚湯"
    elif(choose == 3):
        print("你點的湯品是牛肉湯")
        return "牛肉湯"

def order_main():
    choose = int(input("(1)超級厚黑牛排 (2)夭壽鮮嫩魚排 (3)不好吃砍頭雞排, 請選一道主菜: "))
    if(choose == 1):
        print("你點的主菜是超級厚黑牛排")
        return "超級厚黑牛排"
    elif(choose == 2):
        print("你點的主菜是夭壽鮮嫩魚排")
        return "夭壽鮮嫩魚排"
    elif(choose == 3):
        print("你點的主菜是不好吃砍頭雞排")
        return "不好吃砍頭雞排"

def order_dessert():
    choose = int(input("(1)法式布蕾 (2)炭烤布丁 (3)橙汁奶酪, 請選一道甜點: "))
    if(choose == 1):
        print("你點的甜點是法式布蕾")
        return "法式布蕾"
    elif(choose == 2):
        print("你點的甜點是炭烤布丁")
        return "炭烤布丁"
    elif(choose == 3):
        print("你點的甜點是橙汁奶酪")
        return "橙汁奶酪"
