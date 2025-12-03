# Integrating Point-of-Sale (POS) Systems to Build Digital Menu Boards with OptiSync
**Article URL:** https://support.optisigns.com/hc/en-us/articles/31860170199955-Integrating-Point-of-Sale-POS-Systems-to-Build-Digital-Menu-Boards-with-OptiSync
**Article ID:** 31860170199955

In order to create a DMB with data from your POS system, the API Request will need to be registered as a DataSource. This allows data elements to be added to [OptiSigns' Designer app](https://support.optisigns.com/hc/en-us/articles/4404151402899-How-to-use-OptiSigns-Template-Designer-app-to-make-your-Digital-Signs-in-minutes), where it can be formatted and incorporated into any visual design you'd like to display.

The Designer app and templates can be used to do the formatting, and mapping the element to the data from the API data source. Any text box or image element can be mapped in Designer. When you map an image element, the URL of the image will be replaced at run time.

* * *

### Using DataSources and Repeaters

To get started, find your design or create a new one in the **Files/Assets** tab.

With the design open, click **"DataSource"** in the left hand column. Then, click **"Add DataSource"** to add an API data source to the design.

![firefox_ebkICMVoVf.jpg](https://support.optisigns.com/hc/article_attachments/43051537966355)

Scroll down to where it says **"API Gateway Collection"** and click it.

![firefox_mCdtjleFse - Copy.png](https://support.optisigns.com/hc/article_attachments/31936613189523)

You can also set up a one-time Gateway with the _API Gateway_ command if you need a one-off design with no pre- or post-request processing. In our example, however, we are, so we'll use Gateway Collection.

You should see this screen:

![firefox_xXJk2r7wuv - Copy.png](https://support.optisigns.com/hc/article_attachments/31936613193747)

  * **Name -** The name of the DataSource. This is internally facing and will not be shown on your screens.
  * **Select APIs -** Here you'll select from the API Gateways you've already set up in earlier steps. You can select just one, or multiple. If multiple are selected, the API DataSource will automatically aggregate them.
  * **Update Interval -** How often to send requests back to the API for updates. Select from None (never call the API back), 30 minutes, 60 minutes, or every 6 hours. If you Enable WebHook on your API Request and input the provided URL in your API, this Update Interval will change to near real-time.



Hit **Save** , and the DataSource is created.

It should appear in the left column under **"Used in this design".** It will definitely appear in the **"Other DataSources"** section. You may need to refresh the page for it to appear.