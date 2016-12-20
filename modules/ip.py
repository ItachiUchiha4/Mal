import os
def run(**args):
 print "[*] In IP module."
 p = os.system("ifconfig")
 return str(p)
