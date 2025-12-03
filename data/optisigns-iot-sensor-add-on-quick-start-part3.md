# OptiSigns IoT Sensor Add-on - Quick Start
**Article URL:** https://support.optisigns.com/hc/en-us/articles/13097501958291-OptiSigns-IoT-Sensor-Add-on-Quick-Start
**Article ID:** 13097501958291

![ZgbrWWmul3.png](https://support.optisigns.com/hc/article_attachments/32208910745747)

![S0kR2qEg9y.png](https://support.optisigns.com/hc/article_attachments/32208910750355)

**NOTE:** In the case of custom commands, these are often device specific. Your user manual may have several basic commands. More commands can be determined through OptiSigns; however, the rest of the setup process will need to be completed first.  
---  
  
  * **Name:** This is an internally facing name that will help you organize your IoT devices. Type whatever you wish.
  * **Change Content:** Switch between "Immediately" and a "Delay" of your choice in milliseconds.
  * **Play for at least:** When triggered, the app will play the content corresponding to the play rule for as many seconds as you select here. We recommend keeping this at 3 seconds to give a smoother experience, just in case the triggering events are met frequently.
  * **Rest for:** When the triggering condition is not met, the device will resume playing the content assigned to it for this number of seconds. We recommend keeping this at 3 seconds to give a smoother experience, just in case the triggering events are met frequently.
  * **Play Rules:** Set content you want to play when the corresponding trigger event fires.  

    * **Effective Time:** Determines the time at which the IoT sensor is active. You can select times and days of the week, or a customized schedule.
    * **If Detected:** Sets the command trigger for the rule. This can be one of two preset options, or a custom command. This is a command _received_ from the sensor.  

      * **Tag picked up:** If something is placed on the sensor and then picked up, this will trigger the rule. This gives a Default value specifically for Nexmosphere sensors. Please see the below section __ to get the exact command for your sensor.
      * **Tag put down:** If something is put down on the sensor, this will trigger the rule. This gives a Default value made for Nexmosphere sensors. Please see the below section to get the exact command for your sensor.
      * **Full Command:** A custom command can be input below.
    * **" </>": **A Javascript-based function where you can apply the needed logic to process the incoming command and derive the needed result. In the below example, the Ardunio board will send the temperature data from the sensor in a string, the processing rule extracts the temperature value and determine when the "TOOHOT30" custom command triggers the event.



![mceclip5.png](https://support.optisigns.com/hc/article_attachments/13110786060691)