# OptiKiosk 50 Setup and Troubleshooting Guide
**Article URL:** https://support.optisigns.com/hc/en-us/articles/46299245284243-OptiKiosk-50-Setup-and-Troubleshooting-Guide
**Article ID:** 46299245284243

  * **Check Internet Connection** : Verifies whether the device has an active internet connection.
  * **Check Connection to API Services** : Tests the device's connection to OptiSigns services.
    * Note: If this check fails, it may be due to a firewall blocking the connection. Refer to our[ Whitelist Article](https://support.optisigns.com/hc/en-us/articles/360047275934) for the required URLs and ports.
  * **Check File Downloading** : Confirms the status of downloadable files (e.g., images, videos) being downloaded to the device.
  * **Network Information** : Displays the current network the device is connected to.
    * WiFi/Ethernet Details: Includes IP Address, SSID, Signal Strength, Channel, Connection Type, and MAC Address.
  * **Device Information:**
    * Screen Name, Pairing Code, Screen Resolution, OptiSigns App Version, OptiSigns MDM App Version, OS Version, Manufacturer, Model, Serial Number
    * Heartbeat/Polling Interval: Indicates how frequently the device communicates with OptiSigns servers and the last received signal.
  * **Running Time:** Shows how long the OptiSigns app has been running on the device.
  * **Storage:** Displays used and total storage capacity.
  * **Memory:** Displays used and total memory capacity.
  * **System Time:** Shows the current system time on the device.
  * **System Time Zone:** Displays the time zone configured on the device.
  * **Assigned Content Type:** Indicates the type of content the device is playing (e.g., Asset, Playlist, Schedule).
  * **Assigned Content Name:** Provides the name of the content being displayed.
  * **Device Created Date:** Displays the date the device was activated.
  * **Operational Schedule Assigned:** Shows whether an operational schedule is assigned (Y/N).
  * **Mute Status:** Displays the current audio status of the device.
  * **Heavy Content Status:** Indicates whether the device is handling heavy content (e.g., 4+ zones or SplitScreen with 4K video) (Y/N). This will usually result in lag.



### **Hardware Troubleshooting**

Here, we will cover the most common hardware troubleshooting issues our support team encounters.

#### **Network Troubleshooting**

This is, by far, the most common issue people encounter. Devices experiencing network issues typically appear “Offline” in the OptiSigns portal, even when they are powered on and have content assigned to them.

![](https://support.optisigns.com/hc/article_attachments/46299811073427)

**To identify and resolve network issues:**