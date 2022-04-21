# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 10:04:34 2022

@author: Jaloliddin
"""
def son_topish_2(n):
    import random as r
    royxat = list(range(1, n+1))
    pc_guess = r.choice(royxat)
    tries = 0
    keyboard = ""
    keyboard = input(f"{royxat[0]} dan {royxat[-1]} gacha son o'ylang. Men topishga harakat qilaman.\nSon o'ylab bo'lgan bo'lsangiz xohlagan tugmani bosing>>>>")
    while True:
        a = input(f"\nSiz {pc_guess} sonini o'yladingiz. to'g'ri(T), men o'ylagan son bundan kattaroq (+), yoki kichikroq(-)?")
        tries += 1
        if a == '+':
            while True:
                if royxat[0] == pc_guess+1:
                    break
                else:
                    del royxat[0]               
            pc_guess = r.choice(royxat)
            # print(royxat)
        elif a == '-':
            while True:
                if royxat[-1] == pc_guess-1:
                    break
                else:
                    del royxat[-1]
            pc_guess = r.choice(royxat)
            # print(royxat)
        elif a == 'T' or a == 't':
            print(f"Siz o'ylagan son {pc_guess} edi. Uraa topdim")
            break
    print(f"Urinishlar soni {tries}")
    return tries
#print(son_topish_2(10))    
