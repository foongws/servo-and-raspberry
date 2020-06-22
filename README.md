# My raspberry and servo motor.

This repo mainly to keep a record of what I had done. 

If you are a beginner like me, you might find the information here is helpful for you.

I am trying to drive a 2 servo motors using a raspberry pi 4.

This is just a POC setup. It is a good for start but far from production usage.

In future, if I have any further modification of the script or setup , I will update here.

### Hardware List :

1. Raspberry PI (I am using Raspberry PI version 4 8GB RAM. GPIO layout for all raspberry PI version 4 are the same. Other version of Raspberry PI, the GPIO layout might be different. Please check the GPIO layout if your Raspberry PI is not version 4.)
https://my.cytron.io/p-raspberry-pi-4-model-b-8gb-latest

2. Servo Motor x 2 (At least 2 to make sure you are able to control more than 1 servo motor.)
https://my.cytron.io/p-sg90-micro-servo

If this is your first project, it is good to have all kind of jumper wire with you.

3. 40 Ways Male to Male Jumper Wire x 1
https://my.cytron.io/p-40-ways-male-to-male-jumper-wire

4. 40 Ways Male to Female Jumper Wire x 1
https://my.cytron.io/p-40-ways-male-to-female-jumper-wire

5. 40 Ways Female to Female Jumper Wire
https://my.cytron.io/p-40-ways-female-to-female-jumper-wire

These items is for the PWM servo driver. If you just want to start with 2 servo motor and don't want to spend much. You don't need this.

6. PCA9685 16 Channel 12 bit I2C PWM Servo Driver 
https://www.lelong.com.my/pca9685-16-channel-12-bit-i2c-pwm-servo-driver-arduino-sainapse-io-F1277883-2007-01-Sale-I.htm

7. Adapter 5V 4A R/Angle DC Jack 2.1mm - UK Plug
https://my.cytron.io/p-adapter-5v-4a-r-angle-dc-jack-2.1mm-uk-plug

8. DC Jack(Female) to Screw Terminal Adapter
https://my.cytron.io/p-dc-jack-female-to-screw-terminal-adapter

### Hock Up :
[Hooking-it-Up.md](Hooking-it-Up.md)

### Raspberry setup and configuration :

### Python Code :

Code for burn test: \
[simpletest-counting.py](simpletest-counting.py)

Code with web api:\
[web-api.py](web-api.py)

### Troubleshooting :

Remember to turn on the power of PCA9685.

To test out the servo motor: \
[servo-test.md](servo-test.md)
