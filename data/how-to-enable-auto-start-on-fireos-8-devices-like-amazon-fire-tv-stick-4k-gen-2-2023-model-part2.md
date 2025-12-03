# How to enable auto-start on FireOS 8 devices like Amazon Fire TV Stick 4K Gen 2 (2023 model)
**Article URL:** https://support.optisigns.com/hc/en-us/articles/23274673797139-How-to-enable-auto-start-on-FireOS-8-devices-like-Amazon-Fire-TV-Stick-4K-Gen-2-2023-model
**Article ID:** 23274673797139

Then type “cd android”

![](https://support.optisigns.com/hc/article_attachments/23274680497299)

Then type “dir”:

![](https://support.optisigns.com/hc/article_attachments/23274643497875)

Type “adb connect <The Firestick IP Address from step 2>”

**NOTE: If you receive a message where it mentions “failed to authenticate to <ip address>” you will need to allow access from your Firestick. Check “always allow from this computer” and press “OK”. Then back on the command prompt, type “adb disconnect” and hit enter.**

**![](https://support.optisigns.com/hc/article_attachments/23274690270739)**

Type adb connect <Firestick’s IP address> once more. Once connected, it should look like this:

![](https://support.optisigns.com/hc/article_attachments/23274660262547)

After you’ve successfully connected, enter this command then hit enter:
    
    
    **adb shell pm grant com.optisigns.player android.permission.SYSTEM_ALERT_WINDOW**

This command will now be sent to your Firestick in order to allow OptiSigns to have its auto-start function enabled.

And that’s it! You’re all set!

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
