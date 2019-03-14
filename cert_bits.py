from __future__ import print_function
import sys
import os
import ssl
import socket
from pprint import pprint as pp

# calling underscore prefixed functions is generally a no-no, they're 
# intended for internal use only, and there aren't the same guarantees 
# that the function signature will stay the same from version to same version

# https://stackoverflow.com/questions/16899247/how-can-i-decode-a-ssl-certificate-using-python 
# https://www.geeksforgeeks.org/count-total-bits-number/ 
# https://crt.sh 

def countBits(n):
    count = 0
    while (n):
        count += 1
        n >>= 1
    return count

def cert_file(cert):
    cert_file_name = os.path.join(os.path.dirname(__file__), cert)
    try:
        cert_dict = ssl._ssl._test_decode_cert(cert_file_name)
        pp(cert_dict)
        print("\nNumber of bits in serialnumber of cert " + cert + " : " + str(countBits(int(cert_dict['serialNumber'], 16))))
    except Exception as e:
        print("Error decoding certificate: {:}".format(e))

def cert_url(url):
    url = url.split(':')
    host = url[0]
    port = int(url[1])
    try:
        context = ssl.create_default_context()
    except AttributeError:
        print("\nMinimal python version is 2.7.16")
        sys.exit(1)
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host)
    try:
        conn.connect((host, port))
        cert_dict = conn.getpeercert()
        pp(cert_dict)
        print("\nNumber of bits in serialnumber of cert " + cert + " : " + str(countBits(int(cert_dict['serialNumber'], 16))))
    except Exception as e:
        print("Error decoding certificate: {:}".format(e))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('cert_bits.py file <certificate file> / cert_bits.py url <fqdn:port>')
        sys.exit(2)
    
    file_url = sys.argv[1]
    cert = sys.argv[2]

    print("Start analyze of " + cert)

    if file_url.lower() == 'file':
        cert_file(cert)
    elif file_url.lower() == 'url':
        cert_url(cert)
