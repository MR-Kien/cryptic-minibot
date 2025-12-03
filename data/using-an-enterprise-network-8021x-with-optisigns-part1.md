# Using an Enterprise Network (802.1x) with OptiSigns
**Article URL:** https://support.optisigns.com/hc/en-us/articles/44890229616403-Using-an-Enterprise-Network-802-1x-with-OptiSigns
**Article ID:** 44890229616403

### In this article, we'll cover how to get OptiSigns working on an Enterprise-level security network, either over WiFi or Ethernet.

  * Supported Devices
  * Setting Up 802.1x Enterprise WiFi on a Pro or ProMax Player
    * On Initial Setup
    * Changing From Another Network Source
  * Setting Up a Wired Ethernet 802.1x Enterprise Network



If your organization uses an 802.1x Enterprise Network, many devices will not be compatible with OptiSigns. Here, we'll let you know which ones are, and how to connect to it on OptiSigns devices.

* * *

## Supported Devices

  * OptiSigns [Pro Player](https://www.optisigns.com/product/hardware/pro-digital-signage-player) or [ProMax Player](https://www.optisigns.com/product/hardware/promax-digital-signage-player)
  * Windows
  * Linux



Note that this does not include the OptiStick, nor other devices such as Raspberry Pi. These do not support Enterprise networks at this time.

The scope of this article will limit itself to getting OptiSigns to work on OptiSigns devices. For Windows and Linux, connect the device to your network as normal and be sure OptiSigns has been [**whitelisted through your organization's firewall**](https://support.optisigns.com/hc/en-us/articles/360047275934-Whitelist-OptiSigns-IP-addresses-ports)**.**

**IMPORTANT**  
---  
You'll need to know whether or not you're using **PEAP** or **EAP-TTLS** for your network security protocol. This will determine what sort of certificate to set up on the OptiSigns device.  
  
* * *

## Setting Up 802.1x Enterprise WiFi on a Pro or ProMax Player

Setting up Enterprise WiFi on a Pro or ProMax Player can be done during initial setup, or it can be switched to from a different WiFi source.

### On Initial Setup

You can set your Enterprise WiFi network as See our article on [Setting Up WiFi on the Pro or ProMax Player](https://support.optisigns.com/hc/en-us/articles/32272215514131-OptiSigns-Pro-Digital-Signage-Player#Configuring) for more information on that.

You'll be on the **Device Wi-Fi Settings** menu. Under **Security** , select **WPA2-Enterprise**.

![device wifi settings wpa2-enterprise](https://support.optisigns.com/hc/article_attachments/44890229610259)

Several more options will open up.

![wpa2-enterprise login options](https://support.optisigns.com/hc/article_attachments/44890235677203)