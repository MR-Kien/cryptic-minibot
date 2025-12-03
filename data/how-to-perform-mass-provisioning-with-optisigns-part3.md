# How to Perform Mass Provisioning with OptiSigns
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4416542923667-How-to-Perform-Mass-Provisioning-with-OptiSigns
**Article ID:** 4416542923667

![preconfigure devices options screen 1](https://support.optisigns.com/hc/article_attachments/4416556459923)

Enter a prefix to give to your device and assign some initial content to display onscreen. The device name will be generated based on the prefix with a sequence number added. This name can be changed later before deployment.

![preconfigure devices options screen 2](https://support.optisigns.com/hc/article_attachments/4416556506003)

Once done, the page will list all the devices preconfigured with the pairing code. Click **Done**. This generates a CSV file named "preconfigure-devices.csv". Download it to your computer. 

![preconfigure devices screen with two screens added](https://support.optisigns.com/hc/article_attachments/4416556695571)

Open the CSV file. It will contain the list of the preconfigured devices and their corresponding pairing code. To change the device name, simply update the CSV file. Then the file can be used in deployment if you want to have your screens using the exact pre-assigned name.

![preconfigure devices downloaded csv file](https://support.optisigns.com/hc/article_attachments/4416571675923)

* * *

## Deployment

Once you have the provisioning template config file ready, you can proceed to the deployment. If you would like to pre-assign the exact name on the screen, you will need to get the preconfigured device list from step 2 as well.

### OptiSigns Digital Signage Players and Windows/Linux Devices

For mass provisioning deployment on the [OptiSigns Android Player](https://shop.optisigns.com/products/optisigns-android-stick-player-2), the [OptiSigns Pro Player](https://shop.optisigns.com/products/optisigns-digital-signage-player), or any Windows or Linux device, get a MicroSD card or USB drive and create a folder named "autoconfig" under the root directory. Place the CSV and CFG files into this folder.

Next, attach the MicroSD card/USB drive to your player. Launch the player, and the player will automatically detect the config file and start the provisioning process. You will receive this message once the provisioning is complete (with your local timezone configured):

![mass provisioning success screen](https://support.optisigns.com/hc/article_attachments/4416680470163)

Alternatively, you can MDM the CSV file into:

  * C:/autoconfig or C:/ProgramData/autoconfig on a Windows device
  * ~\autoconfig\ on a Linux or Mac



Then, set up the OptiSigns **[Local Folder app](https://support.optisigns.com/hc/en-us/articles/1500001985341-How-to-Use-the-Local-Folder-App-in-OptiSigns) **to automatically boot it up.

### Raspberry Pi Devices