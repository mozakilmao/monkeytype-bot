from PIL import Image
import pytesseract
import pyautogui
import keyboard

#vars
typeSpeed = 0.06 #lower number = more speed

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

print("Start key: F2")
keyboard.wait('f2')
logolocation = pyautogui.locateOnScreen('logo.png')
top = logolocation.top
left = logolocation.left

img1 = pyautogui.screenshot('screenshot1.png', region=(left+1.3,top+265, 1800, 66.6))
txt1 = pytesseract.image_to_string('screenshot1.png')
txt1split = " ".join(line.strip() for line in txt1.splitlines())
result1 = txt1split.replace("|", "")
pyautogui.write(result1+" ", interval=typeSpeed)

img2 = pyautogui.screenshot('screenshot2.png', region=(left+1.3,top+325, 1800, 66.6))
txt2 = pytesseract.image_to_string('screenshot2.png')
txt2split = " ".join(line.strip() for line in txt2.splitlines())
result2 = txt2split.replace("|", "")
pyautogui.write(result2+" ", interval=typeSpeed)

img3 = pyautogui.screenshot('screenshot3.png', region=(left+1.3,top+325, 1800, 66.6))
txt3 = pytesseract.image_to_string('screenshot3.png')
txt3split = " ".join(line.strip() for line in txt3.splitlines())
result3 = txt3split.replace("|", "")
pyautogui.write(result3+" ", interval=typeSpeed)

img4 = pyautogui.screenshot('screenshot4.png', region=(left+1.3,top+325, 1800, 66.6))
txt4 = pytesseract.image_to_string('screenshot4.png')
txt4split = " ".join(line.strip() for line in txt4.splitlines())
result4 = txt4split.replace("|", "")
pyautogui.write(result4+" ", interval=typeSpeed)

img5 = pyautogui.screenshot('screenshot5.png', region=(left+1.3,top+325, 1800, 66.6))
txt5 = pytesseract.image_to_string('screenshot5.png')
txt5split = " ".join(line.strip() for line in txt5.splitlines())
result5 = txt5split.replace("|", "")
pyautogui.write(result5+" ", interval=typeSpeed)

img6 = pyautogui.screenshot('screenshot6.png', region=(left+1.3,top+325, 1800, 66.6))
txt6 = pytesseract.image_to_string('screenshot6.png')
txt6split = " ".join(line.strip() for line in txt6.splitlines())
result6 = txt6split.replace("|", "")
pyautogui.write(result6+" ", interval=typeSpeed)

img7 = pyautogui.screenshot('screenshot7.png', region=(left+1.3,top+325, 1800, 66.6))
txt7 = pytesseract.image_to_string('screenshot7.png')
txt7split = " ".join(line.strip() for line in txt7.splitlines())
result7 = txt7split.replace("|", "")
pyautogui.write(result7+" ", interval=typeSpeed)