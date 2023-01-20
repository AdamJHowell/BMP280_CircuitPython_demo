# SPDX-FileCopyrightText: 2020 Bryan Siepert, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import time
import board
import busio
import adafruit_bmp280

i2c = busio.I2C( board.GP1, board.GP0 )
bmp280_sensor = adafruit_bmp280.Adafruit_BMP280( i2c )


def c_to_f( value ):
  return value * 1.8 + 32


while True:
  print( f"Temperature: {bmp280_sensor.temperature:.2f} degrees C, {c_to_f( bmp280_sensor.temperature ):.2f} degrees F" )
  print( "" )
  time.sleep( 15 )
