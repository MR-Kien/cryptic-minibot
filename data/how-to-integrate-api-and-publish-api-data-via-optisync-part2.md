# How to Integrate API and Publish API Data via OptiSync
**Article URL:** https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync
**Article ID:** 22875592994195

  1. Use the OptiSigns API Keystore to securely store and use API keys from other systems.
  2. Test the API endpoints, with the capability to modify headers and parameters.
  3. Use substitution parameters and pre-processing and post-processing rules to handle complex integration. Pre-processing rules can help you handle those API integration situations that require an additional call to get an authentication token before making the API call. Post-processing will allow you to process the returned data and tailor it to fit your use better. 



To get started, open your OptiSigns Web Portal.

Once there, navigate to the upper right corner of the screen, and hover over your account name.

Hover over **More → ****DataSources**

**![](https://support.optisigns.com/hc/article_attachments/32427378791315)**

You'll see the screen below.

![](https://support.optisigns.com/hc/article_attachments/32427378806803)

Now you're ready to get started.

* * *

### Step 1: Store Your API Authorization Token in the OptiSigns API Keystore

The first step is to take your API Authorization Token and store it in the OptiSigns API Keystore.

This step is technically optional: you can input your API Authorization token into an individual API request. However, the Keystore has a few major advantages:

  * Allows your API Authorization token to be sent to multiple API requests, without the need to manually input it each time
  * Provides superior security for your API Authorization token, making it much harder for outside actors to discover it



Therefore, we **_highly recommend_** this step.

To enter the Keystore, find the **Lock Icon** and click it.

![firefox_YNrLQDITUl.png](https://support.optisigns.com/hc/article_attachments/32427362113683)

This will open the **API Keystore.**

![](https://support.optisigns.com/hc/article_attachments/32427378817171)

Click **Add Key**.

![firefox_Af1bBuAYxy.png](https://support.optisigns.com/hc/article_attachments/32427378823187)

There are two fields here.

  * **First Field -** Enter the name of the key here. We recommend something that will help you remember it. You'll be using this to set up an API request.
  * **Second Field -** The actual unique passcode for your API communications.



Once you've input your API Authorization token, hit **Save**. When you want to run a request using this API Key, you'll use the term: **{{apiKeystore. <<key>>}}** where "<<key>>" is replaced by the name you inserted earlier. In this example, we'll name our request "clover".

![](https://support.optisigns.com/hc/article_attachments/32427378828051)