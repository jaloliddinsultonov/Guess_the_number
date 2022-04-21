# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 09:41:24 2022

@author: Jaloliddin
"""
def son_topish_1(m):
    import random as r
    pc_oylagan_son = r.randint(1, m)
    imkoniyat = 0
    print(f"1 dan {m} gacha son o'yladim. Topa olasizmi?")
    while True:
      imkoniyat += 1
      son = int(input("Son kiriting:"))
      if son < pc_oylagan_son:
          print("Xato, men o'ylagan son bundan katta")
      elif son > pc_oylagan_son:
          print("Xato, men o'ylagan son bundan kichik")
      elif son == pc_oylagan_son:
          print(f"To'g'ri men o'ylagan son {pc_oylagan_son} edi")
          break
    print(f"Siz men o'ylagan sonni {imkoniyat} martada topdingiz")
    return imkoniyat
      
# print(son_topish_1(20))
 
