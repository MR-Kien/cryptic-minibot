# How to Set Up a PowerBI Service Principal for Use in OptiSigns
**Article URL:** https://support.optisigns.com/hc/en-us/articles/32860569148819-How-to-Set-Up-a-PowerBI-Service-Principal-for-Use-in-OptiSigns
**Article ID:** 32860569148819

![where to find integrations tab in optisigns](https://support.optisigns.com/hc/article_attachments/32860610434451)

A screen like the one below will appear. Click **Add Azure Service Principal.**

![how to add service principal in optisigns](https://support.optisigns.com/hc/article_attachments/32860569109011)

When the popup appears, collect the information mentioned above from Microsoft Azure and input it into OptiSigns. The values match up like this:

![inputting all the powerbi service principal information into optisigns](https://support.optisigns.com/hc/article_attachments/32860610442771)

Once all the information is input correctly, hit **Save**. Now your Service Principal is saved to the OptiSigns portal.

* * *

## Getting PowerBI onto a Screen

Now we’ll need to configure your PowerBI asset in OptiSigns for use with your screens.

In the OptiSigns portal, go to **Files/Assets → Apps → PowerBI**

**![how to find powerbi app in optisigns](https://support.optisigns.com/hc/article_attachments/32860569116691)**

Check **Use Service Principal** and select the service principal you set up in the last step, or whichever service principal you want to use. 

**NOTE:** Using a service principal, the Power BI Dashboard URL link needs to include the actual **workspace (group)** ID instead of me.  
---  
  
**![powerbi app information in optisigns](https://support.optisigns.com/hc/article_attachments/32860610472339)**

Finally, input the URL of whatever report you want to share. Name the app whatever you like, then hit **Preview** to view your report.

**![preview of powerbi app running in optisigns](https://support.optisigns.com/hc/article_attachments/32860610476307)**

Hit **Save** , then this PowerBI app will exist as an asset. It can be pushed to any of your screens individually, scheduled, or added to a Playlist.

### **That’s all!**

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
