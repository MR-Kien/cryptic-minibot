# How to Use the Tableau App
**Article URL:** https://support.optisigns.com/hc/en-us/articles/39250660729747-How-to-Use-the-Tableau-App
**Article ID:** 39250660729747

Once created, it will appear in a list of Connected Apps. Select the app.

On this screen, you'll want to **Enable** the OptiSigns app by hitting the **Three Dots**. Then, you'll want to hit **Generate New Secret** :

![Screenshot 2025-03-22 at 5.27.26 PM.jpg](https://support.optisigns.com/hc/article_attachments/39672709375507)

The blurred out values are your **Secret ID, Secret Value, and Client ID**. These values will be critical to setting up your integration with OptiSigns, so keep this tab open.

With this information and the app Enabled in Tableau, we can configure the integration in OptiSigns.

* * *

## Step 2: Set Up Tableau Integration in OptiSigns

Before starting this step, you should have:

  1. Your **Secret ID, Secret Value, and Client ID** from your Connected App in Tableau on hand
  2. Your Connected App set to Enable



When you’re ready to go, navigate to the **Integrations** tab within OptiSigns:

![integrations tab optisigns](https://support.optisigns.com/hc/article_attachments/39250660697107)

Under the Tableau section of the Integrations page, select **Add Connection**.

![](https://support.optisigns.com/hc/article_attachments/39597853563283)

The **Add** window will pop up:

![add integrations window optisigns](https://support.optisigns.com/hc/article_attachments/39250613933203)  
You’ll need to fill in 5 values:

  * **Name -** The name of the integration. Put whatever you want to help identify it.
  * **Email -** The email associated with your Tableau account. This **_has to match_**.
  * **Client ID -** The Client ID from the last step.
  * **Secret ID -** The Secret ID from the last step.
  * **Secret Value -** The Secret Value from the last step.



Last, make sure the **Active** box is checked. When unchecked, this saves the integration but does not activate it.

Once these values are filled in, hit **Add**. We are now ready to create a Tableau Asset.

* * *

## Step 3: Create a Tableau Asset and Assign it to a Screen

Now that we’ve got the Tableau integration set up, it’s time to create a Tableau asset. This asset determines how your report will show up on your screens.

**NOTE**  
---  
See **Note 2** if your workbook contains Broad Views.  
  
First, find the report you’d like to display. Hit **Share:**

![](https://support.optisigns.com/hc/article_attachments/39364492002579)

On the Share View window, hit **Copy Link** :