from ftplib import FTP
ftp = FTP('ftp.debian.org')     # connect to host, default port
ftp.login()                     # user anonymous, passwd anonymous@
ftp.cwd('debian')               # change into "debian" directory
ftp.retrlines('LIST')           # list directory contents
ftp.retrbinary('RETR README', open('README', 'wb').write)
ftp.quit()