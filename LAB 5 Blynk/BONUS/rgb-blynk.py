import BlynkLib as blynklib
import network
import utime as time
from machine import Pin
from neopixel import NeoPixel

WIFI_SSID = 'Ptcl FF'
WIFI_PASS = '19681968'
BLYNK_AUTH = "xlKMMD_1XMWzIM0EEuAtJMX-EsBqelQL"

print("Connecting to WiFi network '{}'".format(WIFI_SSID))
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)
while not wifi.isconnected():
    time.sleep(1)
    print('WiFi connect retry ...')
print('WiFi IP:', wifi.ifconfig()[0])

print("Connecting to Blynk server...")
blynk = blynklib.Blynk(BLYNK_AUTH)

# Define the pin connected to the NeoPixel (Try GPIO 5 or 18)
pin = Pin(48, Pin.OUT)  # Changed from 48 to 5
np = NeoPixel(pin, 1)

def set_color(r, g, b):
    print(f"Setting color: R={r}, G={g}, B={b}")  # Debugging print
    np[0] = (r, g, b)
    np.write()

# Initialize LED with white light
set_color(255, 255, 255)

# RGB Values
r, g, b = 0, 0, 0

# Blynk Handlers for Virtual Pins
@blynk.on("V0")  # Red Slider
def v0_handler(value):
    global r
    r = int(value[0])
    set_color(r, g, b)

@blynk.on("V1")  # Green Slider
def v1_handler(value):
    global g
    g = int(value[0])
    set_color(r, g, b)

@blynk.on("V2")  # Blue Slider
def v2_handler(value):
    global b
    b = int(value[0])
    set_color(r, g, b)

@blynk.on("connected")
def blynk_connected():
    print("Blynk Connected!")
    blynk.sync_virtual(0, 1, 2)  # Sync RGB sliders from the app
    set_color(r, g, b)  # Ensure last known values are applied

@blynk.on("disconnected")
def blynk_disconnected():
    print("Blynk Disconnected!")

# Main Loop
while True:
    blynk.run()
