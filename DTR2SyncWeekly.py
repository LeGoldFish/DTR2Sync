import wget, sys, time, zipfile, shutil, os, distutils, subprocess
from msvcrt import getch

def installCarWeekly():
	print("*INSTALLING SDLM*")
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

	print("*INSTALLING BLS LM*")
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

	print("*INSTALLING BLS 410 SC*")
	if not os.path.isfile("Car_BLS410SC.zip"):
		BLS410SCurl = 'https://www.dropbox.com/s/h4z5w7d8f5qzizx/Car_BLS410SC.zip?dl=1'
		BLS410SCname = wget.download(BLS410SCurl)
		print("")
	with zipfile.ZipFile('Car_BLS410SC.zip', "r") as bls410scZ:
		bls410scZ.extractall()
		bls410scZ.close()
		os.remove("Car_BLS410SC.zip")
	os.system("xcopy /s /y /q \"BLS410SC\cars\" \"C:\Games\Infogrames\Dirt Track Racing 2\data\cars\"")
	os.system("xcopy /s /y /q \"BLS410SC\skins\" \"C:\Games\Infogrames\Dirt Track Racing 2\data\skins\"")
	shutil.rmtree("BLS410SC")

	print("*INSTALLING BLS MOD*")
	if not os.path.isfile("Car_BLSMOD.zip"):
		BLSMODurl = 'https://www.dropbox.com/s/hgughq0rpt3pqrd/Car_BLSMOD.zip?dl=1'
		BLSMODname = wget.download(BLSMODurl)
		print("")
	with zipfile.ZipFile('Car_BLSMOD.zip', "r") as blsmodZ:
		blsmodZ.extractall()
		blsmodZ.close()
		os.remove("Car_BLSMOD.zip")
	os.system("xcopy /s /y /q \"BLSMOD\cars\" \"C:\Games\Infogrames\Dirt Track Racing 2\data\cars\"")
	os.system("xcopy /s /y /q \"BLSMOD\skins\" \"C:\Games\Infogrames\Dirt Track Racing 2\data\skins\"")
	shutil.rmtree("BLSMOD")

	os.system("cls")	
def installTrackWeekly():
	
	print("*INSTALLING PPMS2014v2*")
	if not os.path.isfile("Track_PPMS2014V2.zip"):
		PPMSV2url = 'https://www.dropbox.com/s/wjn7w2vq893lkb6/Track_PPMS2014V2.zip?dl=1'
		PPMSV2name = wget.download(PPMSV2url)
		print("")
	with zipfile.ZipFile('Track_PPMS2014V2.zip', "r") as ppmsZ:
		ppmsZ.extractall()
		ppmsZ.close()
		os.remove("Track_PPMS2014V2.zip")
		os.system("xcopy /s /y /q \"PPMS2014V2\" \"C:\Games\Infogrames\Dirt Track Racing 2\data\\tracks\"")
		shutil.rmtree("PPMS2014V2")

	print("*INSTALLING LAWRENCEBURG 2013*")
	if not os.path.isfile("Track_LBURG2013.zip"):
		LBURGurl = 'https://www.dropbox.com/s/pzhfrxu2s49vxbf/Track_LBURG2013.zip?dl=1'
		LBURGname = wget.download(LBURGurl)
		print("")
	with zipfile.ZipFile('Track_LBURG2013.zip', "r") as lburgZ:
		lburgZ.extractall()
		lburgZ.close()
		os.remove("Track_LBURG2013.zip")
		os.system("xcopy /s /y /q \"LBURG2013\" \"C:\Games\Infogrames\Dirt Track Racing 2\data\\tracks\"")
		shutil.rmtree("LBURG2013")

	print("*INSTALLING OCFS SLICK 2K12*")
	if not os.path.isfile("Track_OCFSSLICK.zip"):
		OCFSurl = 'https://www.dropbox.com/s/b69gnelmylz8ci1/Track_OCFSSLICK.zip?dl=1'
		OCFSname = wget.download(OCFSurl)
		print("")
	with zipfile.ZipFile('Track_OCFSSLICK.zip', "r") as ocfsZ:
		ocfsZ.extractall()
		ocfsZ.close()
		os.remove("Track_OCFSSLICK.zip")
		os.system("xcopy /s /y /q \"OCFSSLICK\" \"C:\Games\Infogrames\Dirt Track Racing 2\data\\tracks\"")
		shutil.rmtree("OCFSSLICK")

	print("*INSTALLING LASALLE SPEEDWAY 2013 TACKY*")
	if not os.path.isfile("Track_LASALLETACKY.zip"):
		LASALLEurl = 'https://www.dropbox.com/s/jjmyfczw7snfx31/Track_LASALLETACKY.zip?dl=1'
		LASALLEname = wget.download(LASALLEurl)
		print("")
	with zipfile.ZipFile('Track_LASALLETACKY.zip', "r") as lasalleZ:
		lasalleZ.extractall()
		lasalleZ.close()
		os.remove("Track_LASALLETACKY.zip")
		os.system("xcopy /s /y /q \"LASALLETACKY\" \"C:\Games\Infogrames\Dirt Track Racing 2\data\\tracks\"")
		shutil.rmtree("LASALLETACKY")

	print("COULD NOT FIND TRACK 'BMS OSKALOOSA' ON VLR OR IFRT, SKIPPING.")
	
def quit():
	print("Finished Operations! Happy Racing!")
	time.sleep(1.5)
	sys.exit()

def main():
	print("Welcome to DTR2Sync\nPlease Choose an Option (press number corresponding to option):\n")
	print("[1] Install Car Package (Week of 10/18-10/24)")
	print("[2] Install Track Package (Week of 10/18-10/24)")
	print("[3] Install Car and Track Package (Week of 10/18-10/24)")
	print("[4] Quit")
	
	key = ord(getch())
	
	if key == 49:
		installCarWeekly()
		quit()
	if key == 50:
		installTrackWeekly()
		quit()
	if key == 51:
		installCarWeekly()
		installTrackWeekly()
		quit()
	if key == 52:
		quit()
main()