import wget, sys, time, zipfile, shutil, os, distutils, subprocess
from msvcrt import getch

def installSDLM():
	if not os.path.isfile("Car_SDLM.zip"):
		SDLMurl = 'https://www.dropbox.com/s/0kg69x93fvxiryw/Car_SDLM.zip?dl=1'
		SDLMname = wget.download(SDLMurl)
		print("")
	with zipfile.ZipFile('Car_SDLM.zip', "r") as sdlmZ:
		sdlmZ.extractall()
		sdlmZ.close()
		os.remove("Car_SDLM.zip")
	os.system("xcopy /s /y /q \"SDLM\cars\" \"C:\Games\Infogrames\Dirt Track Racing 2\data\cars\"")
	os.system("xcopy /s /y /q \"SDLM\skins\" \"C:\Games\Infogrames\Dirt Track Racing 2\data\skins\"")
	shutil.rmtree("SDLM")

def installBLSLM():
	if not os.path.isfile("Car_BLSLM.zip"):
		BLSLMurl = 'https://www.dropbox.com/s/2mmwx5hw9p7r1tm/Car_BLSLM.zip?dl=1'
		BLSLMname = wget.download(BLSLMurl)
		print("")
	with zipfile.ZipFile('Car_BLSLM.zip', "r") as blslmZ:
		blslmZ.extractall()
		blslmZ.close()
		os.remove("Car_BLSLM.zip")
	os.system("xcopy /s /y /q \"BLSLM\cars\" \"C:\Games\Infogrames\Dirt Track Racing 2\data\cars\"")
	os.system("xcopy /s /y /q \"BLSLM\skins\" \"C:\Games\Infogrames\Dirt Track Racing 2\data\skins\"")
	shutil.rmtree("BLSLM")

def main():
	print("Welcome to DTR2Sync\nPlease Choose an Option (press number corresponding to option):\n")
	print("[1] Install SDLM (Car)")
	print("[2] Install BLS LM (Car)")
	print("[3] Quit")
	
	key = ord(getch())
	
	if key == 49:
		installSDLM()
	if key == 50:
		installBLSLM()
	elif key == 51:
		print("Goodbye")
		time.sleep(1.5)
		sys.exit()

main()