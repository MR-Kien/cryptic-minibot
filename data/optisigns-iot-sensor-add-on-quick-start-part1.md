# OptiSigns IoT Sensor Add-on - Quick Start
**Article URL:** https://support.optisigns.com/hc/en-us/articles/13097501958291-OptiSigns-IoT-Sensor-Add-on-Quick-Start
**Article ID:** 13097501958291

### How to quickly get your IoT sensors up and running on any screens you wish.

In this article:

  * Set Up Serial Communication Channel
  * Set Up IoT Sensor via Lift and Learn
  * Assign the IoT Sensor to a Screen
    * Option 1: Through Lift and Learn
    * Option 2: Through Edit Screen Menu
  * Advanced Settings

**NOTE:** This feature requires the **Engage plan** or higher.  
---  
  
* * *

The OptiSigns IoT Sensor Add-on allows you to use any IoT sensors that work with serial communication to interact with your screens. You'll be able to:

  1. Detect and monitor sensor data about the surroundings, such as motion, temperature and humidity, object liftup/placedown. 
  2. Responsively display different content based on the sensor event that was received by the player connected to the screen.
  3. Send command to other IoT devices to control its behavior, e.g. turn on the atmosphere light, turn on/off the screen monitor.



Our YouTube video shows how it supports the lift and learn use cases using a Nexmosphere brand sensor.

_This feature supports Windows, Linux , MacOS, BrightSigns Player, and our pre-configured Android Stick._

* * *

## **Quick Start Guide for OptiSigns IoT Sensor Add-on**

For the following example, we will use a temperature sensor with an **Arduino** board to demonstrate how it works. ** _Your board may have slightly different connection options - we will note instances where this may be the case._**

The temperature sensor will send data in its own format to the OptiSigns player through serial communication. The temperature data can be displayed on the screen in realtime, and when the defined condition met, the screen content will change to show overheat status. 

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/13110301584531)

Setting up the IoT sensor add-on will take three steps:

  1. Set up the serial communication channel.
  2. Set up IoT sensor via Lift and Learn
  3. Activate the IoT sensor on the screen and assign the IoT sensor addon app to it.



From there you can modify the set up to fit your need.

* * *

## **1\. Set Up Serial Communication Channel**

In the top right corner, click on the account name.

Then, click **Personal Profile →** Look to the left hand column.

Expand **"Advanced" →** **"External Communications (RS232)"**.

![firefox_kDKZkQZT6x.png](https://support.optisigns.com/hc/article_attachments/32208926824211)

_You can also go the the page using this link:**<https://app.optisigns.com/app/s/external-coms>**_