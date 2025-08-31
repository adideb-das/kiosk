import time, board, busio
import adafruit_vl53l0x

installation_height=2134 # height of the sensor in mm(2.1m)

i2c = busio.I2C(board.SCL, board.SDA)
tof = adafruit_vl53l0x.VL53L0X(i2c)     # i2c address of lidar is  0x29


while True:
    # Distance is in centimeters
    distance = tof.range
    height_mm=installation_height-distance
    height_cm=height_mm/10
    print(f"Distance : {distance} cm")
    print(f"Height: {height_cm} cm")
    time.sleep(0.1)
