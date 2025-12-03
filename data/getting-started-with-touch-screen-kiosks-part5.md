# Getting Started with Touch Screen Kiosks
**Article URL:** https://support.optisigns.com/hc/en-us/articles/31449657955347-Getting-Started-with-Touch-Screen-Kiosks
**Article ID:** 31449657955347

![firefox_8U32WAaexO.png](https://support.optisigns.com/hc/article_attachments/31449657942419)

Once there, you'll see these options:

![dnqFMu0Ry0.png](https://support.optisigns.com/hc/article_attachments/31449641356051)

  * **Asset** \- The name of your asset.
  * **Target -** Here, select between Screens, Tags, and Tag Rules. To better understand Tags and Tag Rules, read [this article.](https://support.optisigns.com/hc/en-us/articles/20879903340947-How-to-Use-Content-Tags-in-The-Playlist)
  * **Screens / Tags / Tag Rule** \- Select which screen, tag, or tag rule will be associated with the Kiosk. This determines where your content will appear.



Once these are input, you have a few other options:

  * **Temp Takeover** \- Allows the Kiosk interface to temporarily take over the selected screen. You can select from several predetermined time frames, or create your own.
  * **Schedule Changes** \- Allows you to schedule when the kiosk interface goes live and appears onscreen.
  * **Push** \- Immediately push your kiosk interface to the screen, for an indeterminate amount of time.



You'll also be able to Preview your screen before you push it live.

* * *

## FAQs

Below are some of the most common questions we get surrounding getting a kiosk set up.

### How can I lock down my kiosk on a Windows device?

Windows itself offers a built-in [Kiosk Mode (Assigned Access)](https://learn.microsoft.com/en-us/windows/configuration/assigned-access/), which can restrict a user account to run only a single app—such as OptiSigns. This prevents users from exiting the app or accessing the desktop.  
  


This approach works well for locking down the device. 

**IMPORTANT**  
---  
For Assigned Access, only Universal Windows Platform (UWP) apps from the Microsoft store will appear. OptiSigns is a Win32 app, meaning it will not be available in the Assigned Access list.   
You can use Shell Launcher to replace the user interface from the Windows shell (explorer.exe) to OptiSigns. Keep in mind that this is only available on Windows 10/11 Enterprise, Education, or IoT Enterprise. Shell Launcher is not available on Home or Pro editions.    
You can always keep keyboard shortcuts available if no keyboard is needed for the kiosk.  
  
Consider using Windows Group Policy or third-party tools to further restrict keyboard shortcuts, Task Manager access, or other escape routes.

* * *

## **That's it!**