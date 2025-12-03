# Integrating Point-of-Sale (POS) Systems to Build Digital Menu Boards with OptiSync
**Article URL:** https://support.optisigns.com/hc/en-us/articles/31860170199955-Integrating-Point-of-Sale-POS-Systems-to-Build-Digital-Menu-Boards-with-OptiSync
**Article ID:** 31860170199955

### OptiSync allows you to create dynamic digital menus through API integration. Your POS systems can interface directly with OptiSigns to automatically update prices, track inventory, and more.

  * How to Integrate POS Systems Through API Requests  

    * Get API URL Endpoint and Set Up API Request DataSource
    * Additional Information on API Authentication
    * Handling Multiple Stores or POS Locations
    * How to Use Post-Request Processing to Convert API Data
  * How to Build Digital Menu Boards in Designer with OptiSync  

    * Using DataSources and Repeaters
    * Element Mapping  

      * Adding Text Elements to Your Menu
      * Creating Strike Throughs and Sold Out Warnings
  * Pushing a Digital Menu Board to a Screen



In this article, we will create a real Digital Menu Board (DMB) integrated with a Clover POS system. The DMB pulls product info from Clover and display it onscreen. When an item is not available, it will display as "SOLD OUT."

**NOTE**  
---  
  
#### API Integration is only available with a **Pro Plus** plan or higher.  
  
* * *

## How to Integrate POS Systems Through API Requests

Most POS systems have an API library which OptiSigns can use to get the relevant data from the system programmatically. This API can return menu items, item price, availability, and more.

With OptiSync, we can link APIs to the OptiSigns portal and push the data to screens as a Digital Menu Board (DMB) or any other type of screen you'd like without the need of human intervention.

![api optisigns integration diagram](https://support.optisigns.com/hc/article_attachments/31860108901523)

This article will focus on these POS specific wrinkles, and the process of mapping POS data to assets and pushing them to screens.

**IMPORTANT**  
---  
In order to integrate a POS system, you'll need to first set up an API Gateway request. A complete guide for how to do that can be found [here](https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync).  
  
* * *

### Get API Endpoint URL and Set Up API Request DataSource

We have a [comprehensive guide](https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync) on how to set up your API gateway request. We recommend following this guide until your initial request is set up.

Bare minimum, you'll need an API endpoint URL and an API Authentication token.

### Additional Information on API Authentication