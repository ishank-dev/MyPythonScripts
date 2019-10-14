import pyautogui
pyautogui.size() # to get the dimensions of the screen
width,height = pyautogui.size() # store height and width in respective variables
pyautogui.position() # returns the current mouse pointer locaton
pyautogui.moveTo(10,10,duration = 1.5)# move the pointer to the provided coordinates
pyautogui.moveRel(200,0,duration = 1.5)# move the pointer to the provided coordinates( in pixels)
pyautogui.click(339,38) # click on a specific coordinate
pyautogui.doubleClick()
pyautogui.middleClick()
pyautogui.rightClick()
pyautogui.dragTo(10,10,duration = 1.5)# drag the pointer to the provided coordinates

pyautogui.displayMousePosition() #real time mouse pointer location 
