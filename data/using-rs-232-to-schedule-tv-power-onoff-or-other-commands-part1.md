# Using RS-232 to Schedule TV Power On/Off or other commands
**Article URL:** https://support.optisigns.com/hc/en-us/articles/9061950942995-Using-RS-232-to-Schedule-TV-Power-On-Off-or-other-commands
**Article ID:** 9061950942995

With OptiSigns, you can schedule TV Power On/Off using the advanced schedule feature. There are 2 ways you can do it with OptiSigns depending on what devices you are using.

  * If you are using a consumer-grade TV and an OptiStick, the TV Power On/Off is achieved through HDMI-CEC. See our **[Operational Schedule](https://support.optisigns.com/hc/en-us/articles/28598173096723-How-To-Create-and-Use-Operational-Schedules-HDMI-CEC-RS-232) **article for more information.
  * If you are using a commercial-grade display, RS232 will be the option for you. 



In this article, we will walk through how to set up the external communication for RS-232 and use it to control your commercial display power on/off. It consists of 3 steps at a high level.

  1. Set up RS-232 connection for serial communication.
  2. Configure the RS-232 command for your display and set up the template
  3. Create the Power On/Off Schedule



The same procedures can be used to send other RS 232 compliant commands as well.

Supported devices/platforms: Windows, Linux, Raspberry Pi, OptiStick, and OptiSigns Pro/ProMax players.

**1\. Create RS-232 connection**

Go to the admin console and expand Advanced, click on the link for external communication. You can also use the link below.

<https://app.optisigns.com/app/s/external-coms>

Click "Add New" button, to create a new RS-232 connection. 

![chrome_ThjlLpoiH0.png](https://support.optisigns.com/hc/article_attachments/32323154940819)

In the connection creation window, you can give a name to the connection and define the serial port to use, Baud Rate, Data bits, Stop bits, and Parity. This info is determined by the commercial display used, you should be able to get it from your TV user manual. Flow control is normally not needed in this case, you can just leave it blank.

![chrome_972ixLupAY.png](https://support.optisigns.com/hc/article_attachments/32323154949651)

Click "Save", once the configuration is complete. 

To know which serial port is used, you will need to check it on your device. Using Windows as an example, you can find it in the device manager, it will list out the COM port available. On Linux/Raspberry Pi, the serial port is normally "/dev/ttyS0" or "/dev/ttyUSB0" if a USB serial adapter is used. On OptiSigns pre-configured Android Stick, you can use "USB0" as the serial port. 