# How to use the Web Scripting App
**Article URL:** https://support.optisigns.com/hc/en-us/articles/1500012522362-How-to-use-the-Web-Scripting-App
**Article ID:** 1500012522362

  * **_Name_ :** Name of your asset your asset list. It will _**not**_ be displayed on your screens.
  * **Master Password: **By default, OptiSigns will encrypt the whole script with OptiSigns private key to protect your script, especially username, password in the script. You can add another protection layer by entering a Master Password. If you enter Master Password here, at each device, you will need to enter that Master Password one time in OptiSigns app so it can decrypt the content. 
  * **_Recorded Script:_** Paste the script recorded by the Navigation Recorder here. You can take notice to the script, it's actually not very complicated, you can make some minor changes if you need to.



**Here's how the encryption flow works:**

![mceclip12.png](https://support.optisigns.com/hc/article_attachments/1500019937601)

If you want to add additional security by utilizing a Master Password and our Zero Knowledge Encryption framework you will have to enter your Master Password when:

  * Creating/editing assets
  * One time at each devices, so it will know how to decrypt



Your script is encrypted at your browser, and transfer securely using HTTPS/SSL during transits and stored on our servers.  
It then sends securely to devices, and decrypted at device level right before executing on the target website.

## **Using It on Your Screens**

Once created, the Web Scripting asset can be used in by itself or in Playlists, Schedules, or SplitScreen zones just like any other assets.

If you don't use Master Password, device will use OptiSigns private key to decrypt and execute, so no additional action is needed on the devices.

If you choose to use Master Password and our Zero Knowledge Encryption framework, you will have to enter your Master Password at each device

  * This only needs to be done once on each device and can be used to decrypt all Scripting Assets. (Of course, you have to use the same Master Password to encrypt them).



## **That's all!**

Congratulation, you have created Web Scripting assets, now you can automatically log in to gated websites, navigate to pages as needed.

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
