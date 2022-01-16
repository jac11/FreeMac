# FreeMac
*****************************
### Network script Change mac address 
* A media access control address (MAC address) is a unique identifier assigned to a network interface controller (NIC) for use as a network address in       communications within a network segment. This use is common in most IEEE 802 networking technologies, including Ethernet, Wi-Fi, and Bluetooth. Within the Open Systems Interconnection (OSI) network model, MAC addresses are used in the medium access control protocol sublayer of the data link layer. As typically represented, MAC addresses are recognizable as six groups of two hexadecimal digits, separated by hyphens, colons, or without a separator. 

## how to use 
-----------------------------------------------

1.  https://github.com/jac11/FreeMac.git
2.  cd FreeMac
3.  chmod +x FreeMac.py
4.  show help message ./FreeMac -h 
-----------------------------------------------
 ### * -C/--Company  
-------------------------------------------

#### * To  Use Company mac use -C/--Company  < xxxx/Xxxxx > 
   * available company is [ Sony , Dell , Samsung , Cisco , Apple]
   * ./FreeMac.py -I eth0 -C Sony [ or any company name form the list avelable ]
```
./FreeMac.py -I eth0 -C Sony
````
#### * random Mac
* to use random mac use -r and set argument to true
```
   ./FreeMac.py -I eth0 -r true
   ```
#### * Cook Mac/spoofing Mac
     *  is options use to write your own mac 
     *  this options can use to spoofing mac address with the anther device on same network 
```
    ./freeMac.py -W 00:AA:BB:CC:DD:EE 
```    

###  Note :-
--------------------------------------
###  InterFace options is required  
###  to use -I or --Interface  use ifconfig to make sure that any of the interface are available
-----------------------------------------
## connect :
- administartor@jacstory.toch
-  thank you 
 
