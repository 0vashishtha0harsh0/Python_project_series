import socket
from urllib.parse import urlparse
import subprocess

URL = input("Enter the URL for which you want to find the IP and host : ")


def clean(Host_Name):
    
        parsed = urlparse(Host_Name)
        return parsed.netloc if parsed.netloc else Host_Name 
def Host_IP(Host_Name):
    
    try:
        Host = clean(Host_Name)

        print("Host Name : ", Host)
        print(f"IP : {socket.gethostbyname(Host)}")
    except socket.gaierror as e:
        print(f"Invalid Host name !!!! showing error : {e}")


def Find_all_IP(Host_Name):
    try:
        Host = clean(Host_Name)
        name, aliases, IPs = socket.gethostbyname_ex(Host)
        print("Host Name : ",name)
        print("Aliases : ",aliases if aliases else "None")
        print("All IPs : ",IPs if IPs else "None")
    except Exception as e:
        print("Error in fetching all IPs")


Host_IP(URL)
Find_all_IP(URL)
