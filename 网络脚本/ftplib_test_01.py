import os ,sys
from getpass import getpass
from ftplib import FTP

non_passive =False
filename = 'monkeys.jpg'
dirname = '.'
sitename='ftp.rmi.net'
userinfo = ('lutz',getpass("pswd?"))

if len(sys.argv) > 1:
    filename=sys.argv[1]

print("connecting")
conn = FTP(sitename)
conn.login(userinfo)
conn.cwd(dirname)
if non_passive:
    conn.set_pasv(False)

print("downing...")
localfile = open(filename,'wb')
conn.retrbinary('RETR ' +filename, localfile.write,1024)
conn.quit()
conn.close()