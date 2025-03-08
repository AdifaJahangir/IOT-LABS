#RGB controling using Blynk cloude text input
#rgb text device
import BlynkLib as blynklib
import network
import uos
import utime as time
from machine import Pin, I2C, Timer
from neopixel import NeoPixel
#from machine import Pin, I2C, Timer
import ssd1306

WIFI_SSID = 'Ptcl FF'
WIFI_PASS = '19681968'
BLYNK_AUTH = "C947garnaNQNAW9_62AsKYA9_d8HJ94i"

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

# Define the pin connected to the NeoPixel
pin = Pin(48, Pin.OUT)
np = NeoPixel(pin, 1)

i2c = I2C(1, scl=Pin(9), sda=Pin(8), freq= 200000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def set_color(r, g, b):
    np[0] = (r, g, b)
    np.write()

# RGB Values
r = 0
g = 0
b = 0

# Blynk Handlers for Virtual Pins
@blynk.on("V0")  # RGB Text Input
def v0_handler(value):
    try:
        print("Received value:", value)  # Debugging step
        
        # Ensure value is a list with at least one element
        if not value or not isinstance(value[0], str):
            raise ValueError("Invalid format received from Blynk")

        # Remove spaces and split by comma
        parts = [x.strip() for x in value[0].split(',')]

        # Check if we have exactly 3 values
        if len(parts) != 3:
            raise ValueError(f"Expected 3 values, got {len(parts)}: {parts}")

        # Convert to integers and validate range (0-255)
        r, g, b = map(int, parts)
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise ValueError(f"RGB values out of range: {r}, {g}, {b}")

        set_color(r, g, b)
        oled.fill(0)
        oled.text("RGB Value", 18, 16)
        oled.text(f"{r},{g},{b}", 23, 32)
        oled.show()
    except ValueError as e:
        print("Invalid input format:", e)
    except Exception as e:
        print("Unexpected error:", e)



@blynk.on("connected")
def blynk_connected():
    print("Blynk Connected!")
    blynk.sync_virtual(0, 1, 2)  # Sync RGB sliders from the app

@blynk.on("disconnected")
def blynk_disconnected():
    print("Blynk Disconnected!")

# Main Loop
while True:
    blynk.run()
    

