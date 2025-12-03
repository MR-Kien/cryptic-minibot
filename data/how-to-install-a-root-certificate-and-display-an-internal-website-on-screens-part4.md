# How to Install a Root Certificate and Display an Internal Website on Screens
**Article URL:** https://support.optisigns.com/hc/en-us/articles/35184720136595-How-to-Install-a-Root-Certificate-and-Display-an-Internal-Website-on-Screens
**Article ID:** 35184720136595

**![](https://support.optisigns.com/hc/article_attachments/35184705364115)**

Now you’ll be asked to confirm whether you want to complete the import. As long as you trust the certificate, agree to it by hitting **Finish**.

**![](https://support.optisigns.com/hc/article_attachments/35184705368339)**

### Verify the Installation

Close the MMC.

Open a web browser and try accessing the local host domain. If the certificate is installed correctly, you should no longer see the security warning. However, because it's a self-signed root certificate, you might still see a warning indicating that the website's identity cannot be verified.

If you encounter any issues, double-check the file paths, file names, and the output of the Certificate Import Wizard for any error messages.

### Command Line Installation

You can also use the **Terminal** to directly install the certificate. Simply open up the Terminal app with Administrator privileges after searching for it on your Start bar, and input the following command:
    
    
    certutil –addstore –f "Root" “C:\path\to\your_certificate_file”

This will automatically install the certificate to the Trusted Root Certificates folder and you should be able to access the host domain in the same way as above.

* * *

## Installing a Root Certificate on a MacOS Device

To prepare for the installation, make sure your device is connected to the same network of host servers you plan to use. Also, make sure your certificate is in a folder (the Download folder will work) on the device installing the certificates.

### Install Certificate

To begin, open **Keychain Access**. This is normally located in the “Other” folder in the launchpad.

![](https://support.optisigns.com/hc/article_attachments/35184720101907)

Select the System tab within the menu on the left. If you see a padlock icon next to the System folder, right click to unlock and enter the system password. 

![](https://support.optisigns.com/hc/article_attachments/35184720103571)

![](https://support.optisigns.com/hc/article_attachments/35184720107027)

Open the folder where your certificate is stored. Drag and drop the certificate into the system folder in Keychain Access. If a red x is displayed next to the certificate like below, keep following along. Otherwise, you’re done.

![](https://support.optisigns.com/hc/article_attachments/35184705380883)

Right click the certificate and select “get info”

![](https://support.optisigns.com/hc/article_attachments/35184705382291)

Select “Trust”.

![](https://support.optisigns.com/hc/article_attachments/35184720114579)

Select “Always Trust”. This means your computer will always trust this certificate to keep your connection secure.