from urllib.request import urlopen
import smtplib

with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)

server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
                """To: anhle1531994@gmail.com
                From: anhlvse00534x@funix.edu.vn
                
                Beware the Ides of March.
                """)
server.quit()
