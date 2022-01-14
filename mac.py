#!/usr/bin/env python3

import random
import argparse
import subprocess
import sys
import re 
import os 

class Mac_Free:
      
      def __init__(self):

         self.parese_args()
         self.Main_run()

      def Sony_Mac(self):
          sony = ['FC:0F:E6:','00:12:EE:','00:1E:DC:','78:84:3C:']
          sony = random.choice(sony)          
          Mac_Cook  ="".join( f'{random.randrange(16**8):x}')      
          Mac_Host = ':'.join(Mac_Cook[i:i+2] for i in range(0,6,2)).upper()
          self.Mac_addr =  sony + Mac_Host      
      def Dell_Mac(self):
          dell = ['00:26:B9:','14:FE:B5:','BC:30:5B:','D0:67:E5:']
          dell= random.choice(dell)
          Mac_Cook  ="".join( f'{random.randrange(16**8):x}') 
          Mac_Host = ':'.join(Mac_Cook[i:i+2] for i in range(0,6,2)).upper()
          self.Mac_addr =  dell + Mac_Host 
      def Samsung_Mac(self):
          Samsung = ['10:1D:C0:','78:25:AD:','A0:0B:BA:','E8:11:32:']
          Samsung = random.choice(Samsung)
          Mac_Cook  ="".join( f'{random.randrange(16**8):x}')
          Mac_Host = ':'.join(Mac_Cook[i:i+2] for i in range(0,6,2)).upper()
          self.Mac_addr =  Samsung + Mac_Host 
      def Cisco_Mac(self):
          cisco= ['00:0A:F3:','00:0C:86:','B4:A4:E3:','FC:FB:FB:']
          cisco= random.choice(cisco)
          Mac_Cook  ="".join( f'{random.randrange(16**8):x}')
          Mac_Host = ':'.join(Mac_Cook[i:i+2] for i in range(0,6,2)).upper()
          self.Mac_addr =  cisco + Mac_Host 
      def Apple_Mac(self):
          apple = ['F8:1E:DF:','E0:F8:47:','A4:B1:97:','7C:6D:62:']
          apple = random.choice(apple)
          Mac_Cook  ="".join( f'{random.randrange(16**8):x}')
          Mac_Host = ':'.join(Mac_Cook[i:i+2] for i in range(0,6,2)).upper()
          self.Mac_addr =  apple + Mac_Host 
      def Random_Mac(self):
          Mac_Cook  ="".join( f'{random.randrange(16**16):x}')
          self.Mac_addr = ':'.join(Mac_Cook[i:i+2] for i in range(0,12,2)).upper()
      def Wrire_Mac(self):
          self.Mac_addr = self.args.write
      def mac_change(self):
          command  = "ifconfig  "+self.args.Interface + " | grep ether"
          Current_Mac_P = subprocess.check_output (command,shell=True).decode('utf-8')
          Current_Mac_C = re.compile(r'(?:[0-9a-fA-F]:?){12}')
          Current_Mac_F = re.findall(Current_Mac_C , Current_Mac_P)
          self.Current_Mac_G = str("".join(Current_Mac_F[0]))
          ifconfig_down = "sudo ifconfig "+self.args.Interface+" down"
          ifconfig_mac_change = "sudo ifconfig "+self.args.Interface+ " hw ether "+self.Mac_addr
          ifconfig_up = "sudo ifconfig "+self.args.Interface+" up"
          os.system(ifconfig_down)
          os.system(ifconfig_mac_change)
          os.system(ifconfig_up) 
      def parese_args(self):
          parser = argparse.ArgumentParser( description="Usage: <OPtion> <arguments> ")
          parser.add_argument( '-I',"--Interface"  ,dest = "Interface"   ,required=True   , action=None )
          parser.add_argument( '-C',"--Company"    ,dest = "Company"     ,required=False  , action=None )
          parser.add_argument( '-r',"--random"     ,dest = "random"      ,required=False  , action=None )
          parser.add_argument( '-W',"--write"      ,dest = "write"       ,required=False  , action=None )
          parser.add_argument( '-R',"--Reboot"     ,dest = "Wireshark"   ,required=False  , action=None )
          parser.add_argument( '-T',"--Time  "     ,dest = "Wireshark"   ,required=False  , action=None )
          self.args = parser.parse_args()
          if len(sys.argv)> 1 :
             pass
          else:
             parser.print_help()
             exit()  

      def Main_run(self):
          if self.args.Company:
             if "Sony" in  self.args.Company\
             and len(self.args.Company)==4:
                  self.Sony_Mac() 
                  self.mac_change()
                  print("[+] Current Mac ------------| ",self.Current_Mac_G)
                  print ("[+] New Mac     ------------| ", self.Mac_addr +" [ Sony Mac ]")
             elif "Dell" in  self.args.Company\
             and len(self.args.Company)==4:
                  self.Dell_Mac() 
                  self.mac_change()
                  print("[+] Current Mac ------------| ",self.Current_Mac_G)
                  print ("[+] New Mac     ------------| ", self.Mac_addr +" [ Dell Mac ]")
             elif "Samsung" in  self.args.Company\
             and len(self.args.Company)==7:
                  self.Samsung_Mac() 
                  self.mac_change()
                  print("[+] Current Mac ------------| ",self.Current_Mac_G)
                  print ("[+] New Mac     ------------| ", self.Mac_addr +" [ Samsung Mac ]")
             elif "Cisco" in  self.args.Company\
             and len(self.args.Company)==5:
                  self.Cisco_Mac()
                  self.mac_change() 
                  print("[+] Current Mac ------------| ",self.Current_Mac_G)
                  print ("[+] New Mac     ------------| ", self.Mac_addr +" [ Cisco Mac ]")
             elif "Apple" in  self.args.Company\
             and len(self.args.Company)==5:
                  self.Apple_Mac()
                  self.mac_change()
                  print("[+] Current Mac ------------| ",self.Current_Mac_G)
                  print ("[+] New Mac     ------------| ", self.Mac_addr +" [ Apple Mac ]")
             else:
                 print("[Sony,Dell,Sumsung,Cisco,Apple]"\
                       +'\n'+"the OPtion aveblio")
                 exit() 
          if self.args.random:
             self.Random_Mac()
             self.mac_change()  
          if self.args.write:
             self.Write_Mac()
             self.mac_change()
             
       
if __name__=='__main__':
   Mac_Free()



