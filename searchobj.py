# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:24:37 2018

@author: WP OCT User
"""


class searchobj(searchstrs):
    def __init__(self,searchstrs):
        self.searchstrs = searchstrs
    def find(self,dotimeout=False):
        r =None
        while r is None:
            
                timeout = time.time() + 5
                
                x,y=np.random.randint(5,size=2)
                pyautogui.moveTo(684+x, 1076+y) 
                
                for item in searchstrs:
                    r = pyautogui.locateOnScreen(item,grayscale=False)
                    if r is not None:
                        homex,homey = pyautogui.center(r)
                        pyautogui.click(homex,homey)
                        break
                
                if time.time()>timeout:
                    print("Could not find setupwindow!")
                    break
            






