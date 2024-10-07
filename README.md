# Mac_Free
 * Mac_Free is a Python tool designed to change the MAC address of a network interface. It provides various options to select a MAC address from specific companies like Sony, Dell, Samsung, Cisco, and Apple, generate a random MAC address, or input a   custom MAC address for spoofing.
----------------------------------------------------
## Features
  * Change MAC address to a randomly generated address from a specific company (Sony, Dell, Samsung, Cisco, or Apple). 
  * Generate a completely random MAC address.
  * Set a custom MAC address.
  * Restore the real MAC address if needed.

## Requirements
  * Python 3.x
  * Root privileges (to change MAC addresses)
--------------------------------------------------------------------------
## Imports:
  * random: Used to generate random MAC addresses.
  * argparse: Provides functionality for parsing command-line arguments.
  * subprocess: Enables executing shell commands from the Python script.
  * sys: Provides access to system parameters and functions.
  * re: Used for regular expressions (validating MAC address format).
  *os: Provides operating system interaction (checking for network interfaces).
### Banner:
  * Defines a variable Banner containing a decorative ASCII art string, likely displayed at the script's start.

### Mac_Free Class:
   * This class encapsulates functionalities for changing the MAC address.
     
## init Method:

  * Initializes the class instance.
  * Calls parese_args to parse command-line arguments.
  * Calls Check_InterFace to validate the provided interface name.
  * Executes a shell command (ip link show + self.args.Interface) to retrieve interface details using subprocess.
  * Extracts the current MAC address from the output and stores it in self.real_Mac.
  * Calls Main_run to execute the core functionality.

## Check_InterFace Method:

   * Checks if an interface name was provided using self.args.Interface.
   * If not, it attempts to find valid interfaces using os.listdir('/sys/class/net/').
   * If the provided interface doesn't exist, it prints an error message and exits.

### Sony_Mac, Dell_Mac, Samsung_Mac, Cisco_Mac, Apple_Mac Methods:
   * These methods define functions to generate MAC addresses specific to certain manufacturers.
   * They first create a list containing pre-defined prefixes for the respective brands.
   * They then randomly select a prefix from the list and concatenate it with a randomly generated hex string.
   * Finally, they format the generated string into a valid MAC address format (XX:XX:XX:XX:XX:XX).

## Random_Mac Method:
   * Generates a completely random MAC address.
   * It creates a random hex string and formats it into the standard MAC address format.

### Wrire_Mac Method:

   * Validates the user-provided MAC address using regular expressions (re.findall).
   * If the format is invalid, it prints an error message and exits.
   * Otherwise, it stores the validated MAC address in self.Mac_addr.

## mac_change Method:

  *  Executes a shell command (ifconfig + self.args.Interface + ' | grep ether') to retrieve the current MAC address using subprocess.
  *  Extracts the current MAC address from the output and stores it in self.Current_Mac_G.
  *  Disables the network interface using sudo ifconfig + self.args.Interface + ' down'.
  *  Attempts to change the MAC address using sudo ifconfig + self.args.Interface + ' hw ether ' + self.Mac_addr.
  *  If the command fails (config == 256), it prints an error message suggesting starting the MAC address with "00" and exits.
  *  Re-enables the network interface using sudo ifconfig + self.args.Interface + ' up'.

### parese_args Method:
*  Prints the Banner.
*  Creates an argparse parser object to define command-line arguments.
*  Defines arguments for:
*  Interface (required): The name of the network interface to modify.
*  Company (optional): Specifies a manufacturer for a more realistic MAC address (e.g., Sony, Dell).
*  random (optional): Sets a random MAC address (requires -r true).
*  write (optional): Allows specifying a custom MAC address.
*  Parses the arguments from the command line using parser.parse_args().
*  Checks if any arguments were provided. If not, it prints help information and exits.

### Main_run Method:
 *   Handles the main logic based on the provided arguments.
 *  If Company is specified:
 *  Validates the company name against predefined options (Sony, Dell, Samsung, Cisco, Apple).
 *  If valid, it calls the corresponding method (e.g., Sony_Mac) to generate a manufacturer-specific MAC address.
 *  It then calls mac_change to apply the new MAC address.
 *  Finally, it prints the current, real, and new MAC addresses.
 *  If random is specified and the second argument is true:
 *  It calls Random_Mac to generate a completely random MAC address.
 *  It then calls mac_change to apply the
   
## Usage

1.  https://github.com/jac11/FreeMac.git
2.  cd FreeMac
3.  chmod +x FreeMac.py
4.  show help message ./FreeMac -h 
-----------------------------------------------
 ### * -C/--Company  
-------------------------------------------

#### * To  Use Company mac use -C/--Company  < xxxx/Xxxxx > 
   * available company is [ Sony , Dell , Samsung , Cisco , Apple]
   * sudo ./FreeMac.py -I eth0 -C Sony [ or any company name form the list avelable ]
```
sudo ./FreeMac.py -I eth0 -C Sony
````
#### * random Mac
* to use random mac use -r and set argument to true
```
   sudo ./FreeMac.py -I eth0 -r true
```
#### * Cook Mac/spoofing Mac
 *  is options use to write your own mac 
 *  this options can use to spoofing mac address with  another device in same network 
```
    sudo ./freeMac.py -I etho -W 00:AA:BB:CC:DD:EE 
```    

###  Note :-
--------------------------------------
###  InterFace options is required  
###  to use -I or --Interface  use ifconfig to make sure that any of the interface are available
-----------------------------------------

### Output Example

The tool provides details of the MAC address change:

mathematica
```
[+] Current Mac ------------| 00:1A:2B:3C:4D:5E
[+] Real MAC    ------------| 00:0C:29:4F:8F:14
[+] New Mac     ------------| 00:1A:2B:3C:4D:5E [ Cook Mac ]
```
-------------------------------------------------------------------------------------------------------
### Notes
  * Ensure you have root privileges to change the MAC address.
  * This tool is designed for educational purposes or testing environments.
  *  Always check the legality of spoofing MAC addresses in your area or network.


## connect :
- administartor@jacstory.toch
-  thank you 
