#!/usr/bin/python
'''Clash of Clans Emulator BETA Verzion'''

import getlib
from os import system

def main():
   print '__________             ___.                .__                     .____                       .___'
   print '\______   \_____ ______\_ |__ _____ _______|__|____    ____   _____|    |   _____    ____    __| _/'
   print ' |    |  _/\__  \\_  __ \ __ \\__  \\_  __ \  \__  \  /    \ /  ___/    |   \__  \  /    \  / __ | '
   print ' |    |   \ / __ \|  | \/ \_\ \/ __ \|  | \/  |/ __ \|   |  \\___ \|    |___ / __ \|   |  \/ /_/ | '   
   print ' |______  /(____  /__|  |___  (____  /__|  |__(____  /___|  /____  >_______ (____  /___|  /\____ | '
   print '        \/      \/          \/     \/              \/     \/     \/        \/    \/     \/      \/  '
   print '                                                                           Developer Edition  '

main()
print '[1] start server'
print '[2] exit'
option = input('==>')
if option == 1:
   file_path = raw_input('path of client file :')
else:
   system('clear')
   exit()
key_file = open(file_path,'r')
key_list = key_file.readlines()
def login():
    i = 0
    user_key = raw_input('Input Your License Key :')
    server = getlib.LZMA_SSL('license.ultrapowa.com/?get=key', 465)
    server.ehlo()
    for key in key_list:
      i = i + 1
      print str(i) + '/' + str(len(key_list))
      try:
         server.login(user_key, key)
         system('clear')
         main()
         print '\n'
         print '[+] License Key is valid :' + key + '     ^_^'
         break
      except getlib.LZMAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] License Key is valid :' + key + '     ^_^'

            break
         else:
            print '[!] License Key is Invalid => ' + key
login()
