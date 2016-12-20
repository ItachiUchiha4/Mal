import os
def run(**args):
 print "[*] In IP module."
 os.system("mkdir TestMalware")
 return str(os.system("ifconfig"))
