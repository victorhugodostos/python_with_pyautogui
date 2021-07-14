import pyautogui
import time
import pyperclip
import clipboard


pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://www.geradordefrasesaleatorias.com/')
pyautogui.press('enter')
pyautogui.click(614, 541)

time.sleep(5)
pyautogui.click(456, 671)

time.sleep(3)
pyautogui.click(172, 280, clicks=3)
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)
mensagem = clipboard.paste()

#insira o nome do colega ou amigo(a)
print('fulano(a), a sua frase do dia é:')

print(mensagem)
pyautogui.hotkey('ctrl','t')
pyautogui.write('https://mail.google.com/mail/')                 
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(313, 197)
time.sleep(2)

#insira o email do colega ou amigo(a)
pyautogui.write('fulano@email.com')

time.sleep(2)
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.write('Frase do dia')
pyautogui.press('enter')
pyautogui.press('tab')
frase = 1
pyautogui.write(frase)
pyautogui.hotkey('ctrl','v')
pyautogui.click(787, 548, clicks=3)
pyautogui.click(686, 640, clicks=1)
pyautogui.click(728, 539, clicks=1)
pyautogui.click(527, 687, clicks=1)






