# Event logging and analytics for External Communication(RS-232)
**Article URL:** https://support.optisigns.com/hc/en-us/articles/17342932920211-Event-logging-and-analytics-for-External-Communication-RS-232
**Article ID:** 17342932920211

By default, event data will be logged in real-time.If internet is disconnected, data will be saved locally and will be synced to server automatically when the device come back online.

If for some reason, you don't want real-time data (i.e. to reduce network usage during day time, or if you do "drive-by" data collection once a while). You can unchecked Real-time option and select an upload interval of your choice.

**2\. Enable data collection on IoT sensors add-on**

If you are using IoT sensors, you can set it up to collect the event data within the IoT Sensor Add-on. Simply tick the "Send Data" checkbox, it will start to track the event data. **  
![](https://support.optisigns.com/hc/article_attachments/17351908243987)  
**

**3\. Data collection with advanced scheduling**

If you are using advanced scheduling to control you TV or other devices supporting RS232, the event data collection is enabled by default if you choose the "RS232 Commands" type. You can configure and send multiple commands together, the commands will be sent to the target device one after anther with small latency. If the target devices are responding with confirmation, the response will be logged as well.

Please note, if you are sending multiple commands together, please check the target device specification, the target device may take longer time to execute the commands, in the case, please send the command separately on its own, otherwise the following commands may not be executed and you will not see response from the logging. 

![](https://support.optisigns.com/hc/article_attachments/17352284082323)

**4\. Export Data: Schedule data export & download data**

You can configure OptiSigns to regularly export your raw data.

Here you can control the frequency of the data export, time window of the data export, and the recipients of the data exports. Also, if you have your own AWS S3 buckets available, you can also configure your AWS S3 as the destination of the data export, it is easier for you to automate and connect it to your own analytics process.

![](https://support.optisigns.com/hc/article_attachments/17345743164307)

Here's how a data export looks like:

![](https://support.optisigns.com/hc/article_attachments/17343162545043)

You can also go to the report history tab and download the historical data export.

![](https://support.optisigns.com/hc/article_attachments/17345817445779)

## **Summary:**

The RS-232 logging and analytics will collect the event data and make it available to customers. The data is available in JSON format, you can automate the data export and build your own data pipeline to process the data for further analysis. 

**That's all!**