import os
def run(**args):
 print "[*] In dirlister module."
 files = os.listdir(".")
 p=os.system("ifconfig")
 return str(files)
