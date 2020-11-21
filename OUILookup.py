from getmac import get_mac_address as gma
import sys 
import os 
import getopt


#varibles 
mac = None
mac_vendor = "" 
#argv 
argv = sys.argv[1:]
opts, args = getopt.getopt(argv, "i:m:h", ["ip=", "mac=", "help"])

archivo = open("archivo.txt", "r")
def getmac(ipadress): 
    mac = gma(ip=ipadress)
    return mac

def Vendor_Check(mac):
    lista = mac.split(sep=":")
    mac_vendor = ""
    for x in range(4):
        mac_vendor = mac_vendor + lista[x] + ":"
    print(mac_vendor)     

for opt, arg in opts:
    if opt in ('-i', '--ip'):
        Vendor_Check(getmac(arg))

def vendors():
    lineas = archivo.read()
    for linea in lineas:
        print(linea)    
        

vendors()


