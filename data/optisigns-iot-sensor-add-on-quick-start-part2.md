# OptiSigns IoT Sensor Add-on - Quick Start
**Article URL:** https://support.optisigns.com/hc/en-us/articles/13097501958291-OptiSigns-IoT-Sensor-Add-on-Quick-Start
**Article ID:** 13097501958291

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/13110350933139)

Click **"Add New"** in the **Connections** tab to bring up the **Create New Connection** page, where you can define the parameters for the serial communication.![firefox_KBKtcrjYw5.png](https://support.optisigns.com/hc/article_attachments/32208926832787)

**NOTE:** Most of the required settings will depend on your device. Please see your device's documentation for specific information.  
---  
  
We are only going to cover three main settings off this screen: **Name, COM Port,** and **Baud Rate.**

  * **Name:** A quick name for your sensor. Enter whatever you'd like.
  * **COM port:** Designates which serial port the serial communication channel will enter from.  
Please note, different systems will organize the serial port differently. 
    * **Windows:** Normally represented as "COM#". This will depend on the port you've plugged the sensor into.
    * **Linux:** Normally represented as something like "/dev/ttyUSB0" or "/dev/ttyACM0".
    * **Brightsigns:** Normally represented as "1" or "2"
    * **OptiSigns Preconfigured Android Sticks:** Usually is "USB0"

**NOTE**  
---  
You can find your COM Port by navigating to the **Trigger Event Viewer** page on your screen and clicking on "Show": ![](https://support.optisigns.com/hc/article_attachments/42985157368979)  
  
  * **Baud Rate:** This is a device specific number. For this example, we're using a Baud rate of 9600 for the communication with Arduino board. When using Nexmosphere sensors, the baud rate is always 115200.



Also note, both Arduino board and Nexmosphere controller are using USB port, please make sure the media player you use comes with USB port.

The other options (Data Bits, Stop Bits, Parity, Flow Controls, Receive Line Ending (EOL), Receive Encoding) are highly advanced and **are best left at default** unless your device specifies otherwise.

**Save** the connection once the configuration is complete and then it is ready for use.

**NOTE:** If you wish to set up custom commands to send to your sensor now, see the **_Set Up Custom Sensor Commands_** section of this guide.  
---  
  
* * *

## **2\. Set Up IoT sensor via Lift and Learn  
**

The IoT sensor is configured through our **"Lift and Learn"** builder, found under the **Engage** tab.

![firefox_h7cyVMoyaT.png](https://support.optisigns.com/hc/article_attachments/32208926838675)

Once you've selected Lift and Learn, click **Build.**