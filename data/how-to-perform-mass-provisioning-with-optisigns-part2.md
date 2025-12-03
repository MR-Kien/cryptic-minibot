# How to Perform Mass Provisioning with OptiSigns
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4416542923667-How-to-Perform-Mass-Provisioning-with-OptiSigns
**Article ID:** 4416542923667

![provisioning template options in optisigns](https://support.optisigns.com/hc/article_attachments/4416555482899)

  * _Template Name_ : Name of your template, this is for you to distinguish it when you have multiple provisioning templates.
  * _Device Name Prefix_ : This is used to generate the device name during provisioning.
  * _Device Name Suffix_ : This is used to generate the device name during provisioning, the default setting will add timestamps as a suffix.
  * _Folder:_ The folder you want to have the provisioned devices to be created.
  * _WiFi:_ Select from the stored WiFi, which needs to be created first. Only required if you want to set up WIFI during provisioning.
  * _Time Zone:_ Specify the time zone of the device.
  * _Tags:_ Specify the tags you want to associate with the devices.
  * Initial Default Content Type: Used to set the initial content on the device after provisioning.
  * _Orientation:_ Set the orientation, landscape is the default.
  * _Sync Play:_ Used to set the turn on/off of the sync play feature. For more details on the Sync Play feature, please click [here](https://support.optisigns.com/hc/en-us/articles/4412065189267-Synchronized-playback-Sync-Play-feature).
  * _Location:_ Set the location of the device.



Once the template is created, it will be available under the list of provisioning templates. Download the config file for use during deployment. The configuration file's name is "provisioning-template-<Your Template Name>.cfg"

![provisioning templates screen with arrow pointing at file name button](https://support.optisigns.com/hc/article_attachments/4416548298259)

If you want to set up WiFi at the same time as provisioning, click the **Manage Stored WiFi** button.

In the popup, click "Add New WiFi", then enter the WiFi SSID and password. The WiFi will be stored and available to use in the provisioning template.

![manage stored wifi screen with arrow pointing at add new wifi button](https://support.optisigns.com/hc/article_attachments/4416570772627)

### Step 2: Generate Device List

If you want the device name preassigned for each device, follow this step. Otherwise, proceed to the Deployment section below.

To preassign the device name, choose **Preconfigure Devices** feature on the **Screens** tab to create a device list with a pairing code:

![screens tab with arrows showing how to get to preconfigure devices option](https://support.optisigns.com/hc/article_attachments/4416556453779)

In the popup, specify how many screens you want to preconfigure.