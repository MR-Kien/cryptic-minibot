# How to Perform Mass Provisioning with OptiSigns
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4416542923667-How-to-Perform-Mass-Provisioning-with-OptiSigns
**Article ID:** 4416542923667

### In this article, we explain how to Mass Provision your devices for easy digital signage setup across numerous devices.

  * How to Set Up Mass Provisioning in the OptiSigns Portal
    * Prerequisites
    * Step 1: Create a Provisioning Template
    * Step 2: (Optional) Generate Device List
  * Deployment by Device
    * OptiSigns Digital Signage Players & Windows/Linux Devices
    * Raspberry Pi Devices
    * Apple TV and ChromeOS



**NOTE:** Mass Provisioning is only available to **Enterprise** plan subscribers.  
---  
  
Customers on the Enterprise Plan can now perform mass provisioning with OptiSigns. It is supported on OptiSigns Android Player, Windows, Linux, Raspberry Pi, ChromeOS, or AppleTV.

If running a large deployment of digital signs, mass provisioning will save a lot of time and effort.

For example, when you use our RPI image or have MDM software to display the OptiSigns player on a device, the mass provisioning feature lets you set up the device and get it connected to your account without having to set up each device individually.

* * *

## How to Set Up Mass Provisioning in the OptiSigns Portal

The process of performing mass provisioning is simple and straightforward.

  1. Create a provisioning template in your account.
  2. (Optional) Generate a device list. Only needed if you wish to
  3. Deploy and run.



### Prerequisites:

  * The device needs to support using a USB drive or SD card. Or there is a way you can push the configuration file to a specific location in the OS.
  * The user using the OS has the privilege to run the installation and access the USB drive or SD card.



First time using OptiSigns? [Learn how to set up your digital signs](https://www.optisigns.com/blog/how-to-set-up-digital-signs-with-optisigns-and-amazon-fire-tv) to get a better understanding before deployment.

### Step 1: Create provisioning template

To create a provisioning template, access it from the admin menu or use this [provisioning templates link](https://app.optisigns.com/app/s/provisioning-templates).

![provisioning templates dropdown in optisigns app](https://support.optisigns.com/hc/article_attachments/34385117085715)

**NOTE:** This option will not be visible without an **Enterprise** level plan.  
---  
  
Create a new provisioning template by clicking the **Create templates** button.

![create templates button with arrow pointing at it in optisigns app](https://support.optisigns.com/hc/article_attachments/34385123847827)

If you want to auto-step up WiFi at provisioning, you will need to create a stored WiFi first. These steps are covered later.

For now, set up the template in this popup: