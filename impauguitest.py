import pyautogui
im1 = pyautogui.screenshot()


for val in range(1,10):
    filename = str(val) + ".jpg"
    print(filename)
    im1.save("d:/"+filename)
