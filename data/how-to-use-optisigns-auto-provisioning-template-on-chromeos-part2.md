# How to use OptiSigns Auto Provisioning Template on ChromeOS
**Article URL:** https://support.optisigns.com/hc/en-us/articles/17353256033811-How-to-use-OptiSigns-Auto-Provisioning-Template-on-ChromeOS
**Article ID:** 17353256033811

  * _Template Name_ : Name of your template, this is for you to distinguish it when you have multiple provisioning templates.
  * _Device Name Prefix_ : This is used to generate the device name during provisioning.
  * _Device Name Suffix_ : This is used to generate the device name during provisioning, the default setting will add timestamps as a suffix.
  * _Folder:_ The folder you want to have the provisioned devices to be created.
  * _WIFI:_ Select from the stored WIFI, need to be created first. Only required if you want to setup WIFI during provisioning. WIFI setup is normally not needed for ChromeOS deployment. Because the deployment will be managed through Chrome Device Management.
  * _Time Zone:_ Specify the time zone of the device.
  * _Tags:_ Specify the tags you want to associate to the devices.
  * Initial Default Content Type: Used to set the initial content on the device after provisioning.
  * _Orientation:_ Set the orientation, landscape is the default.
  * _Sync Play:_ Used to set the turn on/off of the sync play feature. For more details of Sync Play feature, please click [here](https://support.optisigns.com/hc/en-us/articles/4412065189267-Synchronized-playback-Sync-Play-feature).
  * _Location:_ Set the location of the device.



Once the template is created, it will be available under the list of provisioning templates, you can download the config file and it will be used later during deployment. Please make sure to select "ChromeOS" when you click the download button. The configuration file's name is "provisionting-template-<Your Template Name>.txt"

![](https://support.optisigns.com/hc/article_attachments/17359692661139)

The file will contain a JSON object, this is what is needed later when setting up auto provisioning on Google Chrome Device Management.

![](https://support.optisigns.com/hc/article_attachments/17359871365139)

**2) Create mass provisioning template for your Chrome deployment**

OptiSigns uses policy extensions on ChromeOS to provision the device into your account.

Please follow section 1 of this document([how to deploy OptiSigns on ChromeOS with Chrome Device Management](https://support.optisigns.com/hc/en-us/articles/360054033374)) to complete the auto provisioning of the OptiSigns application on your ChromeOS device.

Then go to "Apps&extensions" from Chrome Device Management, find the OptiSigns app from the Kiosks setting.

Find the "Policy for extensions", this is where you put the JSON object from the auto provisioning template file generated above.

![](https://support.optisigns.com/hc/article_attachments/17360066112659)

Save it, then you are ready to start your deployment.