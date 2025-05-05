# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
# setup static ip for esp32

# import network
# import utime as time
# 
# WIFI_SSID = "TampleDiago"
# WIFI_PASS = "12345689"
# 
# # Static IP configuration
# STATIC_IP = "192.168.145.75"  # Replace with your desired static IP/
# SUBNET_MASK = "255.255.255.0"
# GATEWAY = "192.168.145.56"  # Replace with your router's IP/hotspot
# DNS_SERVER = "8.8.8.8"  # Google DNS
# 
# 
# 
# print("Connecting to WiFi network '{}'".format(WIFI_SSID))
# wifi = network.WLAN(network.STA_IF)
# wifi.active(True)
# 
# wifi.ifconfig((STATIC_IP, SUBNET_MASK, GATEWAY, DNS_SERVER))
# 
# wifi.connect(WIFI_SSID, WIFI_PASS)
# while not wifi.isconnected():
#     time.sleep(1)
#     print('WiFi connect retry ...')
# print('WiFi IP:', wifi.ifconfig()[0])



import network
import utime as time

WIFI_SSID = 'TampleDiago'
WIFI_PASS = '12345699'

# Static IP configuration
STATIC_IP = "192.168.5.14"  # Replace with your desired static IP
SUBNET_MASK = "255.255.255.0"
GATEWAY = "192.168.5.78"  # Replace with your router's IP
DNS_SERVER = "8.8.8.8"  # Google DNS



print("Connecting to WiFi network '{}'".format(WIFI_SSID))
wifi = network.WLAN(network.STA_IF)
wifi.active(False)
wifi.active(True)

#wifi.ifconfig((STATIC_IP, SUBNET_MASK, GATEWAY, DNS_SERVER))

wifi.connect(WIFI_SSID, WIFI_PASS)
while not wifi.isconnected():
    time.sleep(1)
    print('WiFi connect retry ...')
print('WiFi IP:', wifi.ifconfig()[0])


