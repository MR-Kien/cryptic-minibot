# OptiSigns IoT Sensor Add-on - Quick Start
**Article URL:** https://support.optisigns.com/hc/en-us/articles/13097501958291-OptiSigns-IoT-Sensor-Add-on-Quick-Start
**Article ID:** 13097501958291

### Option 2: Through the Edit Screen Menu

You can also assign your completed Sensor app to a screen through the [Edit Screen Menu.](https://support.optisigns.com/hc/en-us/articles/360048914673-Edit-Screen-What-does-each-option-do)

To get there, go to Screen Management and click Edit the screen you want to add this Add-on to.

Click **Advanced** **→** **More** **→** **Sensor Add-on → Activate** to open up more options.

![mceclip7.png](https://support.optisigns.com/hc/article_attachments/13110881710611)

![mceclip6.png](https://support.optisigns.com/hc/article_attachments/13110883397907)

  * **Sensor Add-on -** This is the IoT Sensor Add-on we created earlier. You can cycle through your created apps here.
  * **Sensor COM Connection** \- This is the serial communication channel we created in the first step. Select it here!
  * **Sensor Commands Template -** This sets an external command template. If you're using an IoT sensor, you **should not need to use this device**.
  * **External COM -** This for when you need to send a command out. Most users will want to leave this unchecked.



On the screen, you should also select the standard content that should be played on the screen in the normal, in this case we use the "Heat Sensor - Normal" asset that display the standard content and also data from temperature sensor in real time.

Once IoT Sensor Addon is activated, you can assign the IoT sensor Add-on app that was created earlier, in this case it is called "Sensor". And also select the sensor connection that was created in the first step, in this case it is "Arduino - Win". Since we are only receiving commands from sensors, we will leave the sensor commands template as "None"

* * *

## **Advanced Settings**

**Use Case**  
---  
In special cases when you need to send commands back to external devices, such as a light source or speaker, these options are for you. These options are not needed for those using ordinary IoT sensor devices.  
  
First, navigate to **External Communications (RS232) →****Add New**

![firefox_Ormk62EJMc.png](https://support.optisigns.com/hc/article_attachments/32208910780051)

This screen will come up:

![firefox_tdPfmJaP56.png](https://support.optisigns.com/hc/article_attachments/32208910797715)

Here you'll see four options: