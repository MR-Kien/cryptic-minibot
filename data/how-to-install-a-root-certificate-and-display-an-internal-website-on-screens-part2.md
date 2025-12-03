# How to Install a Root Certificate and Display an Internal Website on Screens
**Article URL:** https://support.optisigns.com/hc/en-us/articles/35184720136595-How-to-Install-a-Root-Certificate-and-Display-an-Internal-Website-on-Screens
**Article ID:** 35184720136595

**IMPORTANT**  
---  
For installation on a Gen 3 Pro Player, your certificate must have a **.crt** extension. However, it is important that this certificate is signed and contains your public key. These are usually generated as **.pem** files. You’ll need to rename your certificate (.pem) file and change its extension to **.crt** for your internal website to properly display.  
  
Now, open your OptiSigns player menu. Go to **About → Advanced Settings**.

**![](https://support.optisigns.com/hc/article_attachments/35184705322515)**

Here, you’ll see a field called **Certificate File**. 

![](https://support.optisigns.com/hc/article_attachments/35184705339539)

Simply locate your certificate on your USB or MicroSD card and select it. The certificate will automatically be downloaded to the appropriate location. This will allow your OptiSigns player to display your internal website.

* * *

## Installing a Root Certificate on OptiSigns Gen 2 Pro Players and Linux/Ubuntu Devices

To install a root certificate on a Linux or Ubuntu device, you’ll need to make heavy use of the **Terminal.**

To begin, take your trusted, signed certificate (.pem file) and place it in the /usr/share/ca-certificates folder.

![](https://support.optisigns.com/hc/article_attachments/35184720058515)

**NOTE**  
---  
You will need to rename your **.pem** file to make it a **.crt** file, or else this will not work.  
  
After the certificate has been moved and renamed, you’ll need to refresh the installed certificates and hashes. Open your **Terminal** and type in this command:
    
    
    sudo update-ca-certificates

Once this command is executed, it should say that it has installed 1 (or more) new certificate.

![](https://support.optisigns.com/hc/article_attachments/35184720067475)

This means the certificate has been added to the operating system and signed certificates will be trusted.

Now, you’ll want to install the certificate in the Chromium store using this command:
    
    
    certutil -A -n "ROOT-CA" -t "TCu,Cu,Tu" -i /usr/share/ca-certificates/[name-of-cert].crt -d sql:/home/[user]/.pki/nssdb

The Linux-based OptiSigns app uses Chromium, so this will allow the certificate to pass through the OptiSigns app.

Now reboot your device.

Congratulations! You’ve successfully installed a root certificate on Ubuntu.

* * *

## Installing a Root Certificate on a Windows Device

Broadly, there are four major steps to installing a root certificate locally on a Windows device: