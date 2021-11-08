from PIL import Image
import os, random
import pathlib

#take one part of picture picked from random
#take another random pic
#combine

class NFT:
  def __init__(self,base):
    self.pic = base
    self.code = " "
  def stack(self,top):
    self.pic.paste(top.pic, (0, 0), top.pic.convert('RGBA'))
    x = top.code.split(".")
    self.code = self.code.strip(" ") + x[0].strip(" ")

def get_random_picture(folder):
  p = pathlib.Path().resolve()
  p = os.path.join(p, "assets")
  p = os.path.join(p, folder)

  #get path of where program is actually stored
  #random.choice(os.listdir(p))
  #build path
  
  fileNum = random.choice(os.listdir(p))
  p = os.path.join(p,fileNum)
  rdmPic = NFT(Image.open(p))
  rdmPic.code = rdmPic.code + fileNum
  return rdmPic

#main
def getDirlist():
  p = pathlib.Path().resolve()
  p = os.path.join(p, "assets")
  p = os.listdir(p)
  return p

def generateNFT(res):
  base = NFT(Image.new(mode="RGBA", size=(res,res)))#create new image
  folder_list = getDirlist()
  for folder in folder_list: #layer random from each directory
    base.stack(get_random_picture(folder))
  return base

def autoGen(num, resolution):
  serial_list = [None] * num
  i = 0
  j = 0
  p = pathlib.Path().resolve()
  p = os.path.join(p, "generated")
  if not os.path.exists(p):
      os.makedirs(p)
  while i < num:
    current = generateNFT(resolution)
    if(current.code not in serial_list):
      serial_list[i] = current.code
      i = i + 1
      np = os.path.join(p, current.code + ".png")
      current.pic.save(np)
      j = 0
    else:
      j = j + 1
      if(j > 500): #checks if all nfts have been generated
	      break
      print("duplicate of" + current.code)

num = input("Enter number of unique NFT's to generate:")
res = input("Enter resolution: ")
autoGen(int(num),int(res))
print("Generated " + num + " NFTs")
      

