# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 14:15:46 2022

@author: Jaloliddin
"""

def son_topish_final():
    print("Keling o'ylagan sonni topish o'ynaymiz!")
    import son_top as s1
    import sonni_pc_topadi as s2
    
    while True:
        # print(s1.son_topish_1(10))
        # print(s2.son_topish_2(10))
        userning_urunishlari = s1.son_topish_1(10)
        kompyuterning_urunishlari = s2.son_topish_2(10)
        if userning_urunishlari == kompyuterning_urunishlari:
            print(f"Ikkalamiz bir xil urinishda {userning_urunishlari} da topibmiz. Durrang.")
        elif userning_urunishlari > kompyuterning_urunishlari:
            print(f"Siz {userning_urunishlari} ta urunishda, men esa {kompyuterning_urunishlari} tada topibman. Men g'olibman")
        elif userning_urunishlari < kompyuterning_urunishlari:
            print(f"Siz {userning_urunishlari} ta urunishda, men esa {kompyuterning_urunishlari} tada topibman. Siz g'olibsiz.")
        choice = input("Yana o'ynashni xohlaysizmi?(Yes/No)").lower()
        if choice == "no":
            break
        
print(son_topish_final())