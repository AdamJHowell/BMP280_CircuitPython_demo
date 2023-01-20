# SPDX-FileCopyrightText: 2020 Bryan Siepert, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import time

import adafruit_bmp280
import board
import busio

scl_pin = board.GP3
sda_pin = board.GP2

i2c_bus = busio.I2C( scl_pin, sda_pin )
bmp280_sensor = adafruit_bmp280.Adafruit_BMP280_I2C( i2c_bus, address = 0x76 )


def c_to_f( value ):
  return value * 1.8 + 32


loop_count = 0

while True:
  loop_count += 1
  print( f"Temperature: {bmp280_sensor.temperature:.2f} degrees C, {c_to_f( bmp280_sensor.temperature ):.2f} degrees F" )
  print( f"Loop count: {loop_count}" )
  print( "" )
  time.sleep( 15 )
