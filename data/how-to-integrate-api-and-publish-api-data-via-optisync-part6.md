# How to Integrate API and Publish API Data via OptiSync
**Article URL:** https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync
**Article ID:** 22875592994195

When the API call is triggered on the device, it will take the value from the device and substitute it at runtime. For each screen, you'll want to perform these same steps, keeping the Key name the same while changing the Value. This will allow you to push different data to different screens.

* * *

## How to Map API Data in Designer

In order to push data from your API to a screen, it will need to be registered as a DataSource. This allows data elements to be added to OptiSigns' Designer app, where it can be formatted and incorporated into any visual design you'd like to display.

The Designer app and templates can be used to do the formatting, and the API data source will handle the data mapping. Any text box or image element can be mapped in Designer. When you map an image element, the URL of the image will be replaced at run time.

* * *

### Step 1: Creating an API DataSource

To get started, find your design or create a new one in the **Files/Assets** tab.

With the design open, click **"DataSource"** in the left hand column. Then, click **"Add DataSource"** to add an API data source to the design.

![](https://support.optisigns.com/hc/article_attachments/42850937896211)

Scroll down to where it says **"API Gateway"** and click it.

![](https://support.optisigns.com/hc/article_attachments/42850937907987)

You should see this screen:

![](https://support.optisigns.com/hc/article_attachments/42850937909523)

Select the API Request created above. You'll see a screen like the one below:

![](https://support.optisigns.com/hc/article_attachments/42850937911187)

Here, you can choose what data specifically you want to add to the Design. If you want all the options, hit **"Continue"**. This screen will appear.

![](https://support.optisigns.com/hc/article_attachments/42850937917715)

**DataSource Name** is how this DataSource will appear in Designer. Name it whatever helps you identify it.

**Synchronization** lets you choose how often to sync back to your API. _Only import once_ makes sense for one-time promos and the like. If this is for a longer-term asset, choose _Periodic direct access_ or _Periodic background sync_ depending if you need to use the data from specific device to set the context _._

Hit **Done** , and the DataSource is created.

It should appear in the left column under **"Used in this design".** It will definitely appear in the **"Other DataSources"** section. You may need to refresh the page for it to appear.

Now, we move to step 2.

* * *

### Step 2: Maintain the Element Mapping