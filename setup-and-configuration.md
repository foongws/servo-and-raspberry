```
sudo apt update
sudo raspi-config

# Interfacing Options -> P2 SSH -> Enable
# Interfacing Options -> P4 SPI -> Enable
# Interfacing Options -> P5 I2C -> Enable

sudo apt-get install python-smbus
sudo apt-get install i2c-tools
sudo i2cdetect -y 1

sudo pip3 install adafruit-circuitpython-servokit
sudo pip3 install adafruit-pca9685

```
