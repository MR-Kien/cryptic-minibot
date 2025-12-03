# Build Integration Using OptiSigns Enterprise App
**Article URL:** https://support.optisigns.com/hc/en-us/articles/13320135306515-Build-Integration-Using-OptiSigns-Enterprise-App
**Article ID:** 13320135306515

The template comes with sample code that you can use directly, all you need to do is to change how you would like the page to look like and how you want to handle the incoming data points from other systems. Once you are done with the changes, click "Save&Deploy" button, it will be ready for use.

![mceclip4.png](https://support.optisigns.com/hc/article_attachments/13320838658451)

#### **2\. Build the integration to your enterprise systems or custom applications.**

We will use the demo Control Center to show how you can send data and interact with the screens in this tutorial. In your cases, the demo Control Center will be your systems that you want to initiate the process to control the screen or a custom application that was specifically built for your need.

Click "Control Center" in the Enterprise App, it will launch the demo Control Center. 

![mceclip5.png](https://support.optisigns.com/hc/article_attachments/13320889712915)

The demo Control Center will launch with the logon page first. In this case, you just need to use your OptiSigns account. The framework supports authentication and authorization, when you build your integrations with other systems, you will have the capability to utilize the authorization you defined with in OptiSigns. 

After logon, the demo Control Center will list all the screens that you have access to. You can also search the screens that you want to control. In this case, we will try to control the Enterprise App Demo Screen.

![mceclip7.png](https://support.optisigns.com/hc/article_attachments/13321031641363)

Click the "Edit" button will popup the Edit Device page. This is where we can control how to send data to the screen.

![mceclip8.png](https://support.optisigns.com/hc/article_attachments/13321033226131)

#### **3\. Send data from your system to the screen and get it published.**

Looking at this screen, we can have any asset/playlist/schedule assigned to the screen. The screen will just play the assigned content as normal. When we initiate the integration from the demo Control Center, we can send the freeform JSON data to the screen, and assign the Enterprise App asset ID to take over the screen immediately and display the data.

Now, the screen is assigned an asset other than the Enterprise App.

![mceclip9.png](https://support.optisigns.com/hc/article_attachments/13321076982035)