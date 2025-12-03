# How to Integrate API and Publish API Data via OptiSync
**Article URL:** https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync
**Article ID:** 22875592994195

### Integrating your API with OptiSigns has many uses and allows easy display of auto-updating data on your screens. In this guide, we'll walk you through how to connect your API - no software engineering background required.

  * What API Integration Can Do
  * What You'll Need to Get Started
  * How to Set Up an API Request  

    * Step 1: Store Your API Authorization Token in the OptiSigns API Keystore
    * Step 2: Set Up and Test the API Request
      * How to Use Parameters
      * How to Use Pre- and Post-Request
    * Step 3 (Optional): Use Substitution Parameters from Device Attributes
  * How to Map API Data in Designer
    * Step 1: Creating an API DataSource
    * Step 2: Maintain the Element Mapping
  * More on OptiSync Use Cases

**NOTE:** API Integration is only available with a **Pro Plus** plan or higher.  
---  
  
* * *

## What API Integration Can Do

OptiSigns allows easy integration with user APIs. This allows data from a user's API to be shown on any of your digital signs. This allows dynamic updates for:

  * **Digital Menu Boards** \- Integrate with your POS systems and get the DMB updated automatically, and edit the format of your DMB using the designer app whenever needed. 
  * **Automated HR Update** \- Use the API from your HR systems to display birthdays or work anniversaries on the screens automatically.
  * **Warehouse Inventory Tracking** \- Use your Warehouse's API to display inventory levels with automatic updates throughout your organization
  * Any other information display use cases that you will need to consume API data and display the data on the screens.



This API integration can be achieved in OptiSigns with little to no coding, making it approachable for those without backgrounds in software engineering. In this guide, we will walk you through how to get it set up with the example below using an API from the Clover POS system.

* * *

## What You’ll Need to Get Started

You’ll need your:

  * **API Endpoint URL**
  * **API Authorization Token**



These are required for OptiSigns to connect with your desired API. Make sure you have them in an easily accessible place before you try to set up your API Request in the OptiSigns Web Portal. You should be able to obtain these from an IT professional in your organization, or through your POS system administrator.

* * *

## How to Set Up an API Request

The API gateway is a powerful tool that allows users to centrally manage the APIs, as well as configure and test the APIs. 

Now that you have everything you need, let's get started on setting up an API Request. With an API request, you can: