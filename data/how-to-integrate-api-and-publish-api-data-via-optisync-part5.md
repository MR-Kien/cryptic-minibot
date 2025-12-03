# How to Integrate API and Publish API Data via OptiSync
**Article URL:** https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync
**Article ID:** 22875592994195

![](https://support.optisigns.com/hc/article_attachments/32427362130195)

For this common example, this piece of JavaScript code should solve your issue. We can also set up the ability to map product availability at the same time.

This will fix the returned data, allowing it to display properly:

![](https://support.optisigns.com/hc/article_attachments/32427362133523)

This can also be used to make data appear as "SOLD OUT," to strike through an item if it's unavailable, or to display warnings in an inventory management system. For more on this example, see our article on [Digital Menu Boards.](https://support.optisigns.com/hc/en-us/articles/31860170199955-Integrating-Point-of-Sale-POS-Systems-to-Build-Digital-Menu-Boards-with-OptiSync)

* * *

### Step 3 (Optional): Use Substitution Parameters from Device Attributes.

Many point-of-sale (POS) systems are licensed by store/location. It's possible to configure a single API Request with OptiSync and have it work with different locations using **substitution parameters**. Inputting these allows your screen to communicate its store or location identification information. This means a single API request can communicate different data to different stores or locations, rather than needing to make individual API requests per screen.

To get started, find the screen you wish to edit.

![](https://support.optisigns.com/hc/article_attachments/32427362139411)

Click **Advanced** **→** **More** **→** **Device Additional Attributes.**

![](https://support.optisigns.com/hc/article_attachments/32427378848019)

Two fields will show up, **Key** and **Value**.  
![firefox_KkCBvxsPKU.png](https://support.optisigns.com/hc/article_attachments/32427362146707)

  * **Key** \- A parameter that will be used during the API call to substitute for your store's value. This will replace part of your API URL endpoint.
  * **Value** \- Represents the unique code associated with the store or location you wish to pass through to your API.



In this example, we are maintaining the Clover merchantID here. The value inputted will need to be obtained on your end as it will be unique.

Now, go back to the API request config page. Substitute the merchantID in the API endpoint with the Key name you previously defined.

#### **![](https://support.optisigns.com/hc/article_attachments/22917801932051)**