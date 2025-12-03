# How to use Toast API data with OptiSigns
**Article URL:** https://support.optisigns.com/hc/en-us/articles/31113088917907-How-to-use-Toast-API-data-with-OptiSigns
**Article ID:** 31113088917907

### Toast is one of the most common Point-of-Sale systems in North America. In this article, we'll explain how to set up API integration between your Toast system and OptiSigns.

  * Step 1: Preparation
  * Step 2: Authentication to Toast API
  * Step 3: Call the API to Get the Required Data from Toast
  * Step 4: Build the DMB Designer with OptiSync



Toast provides an API for users to integrate POS data with other systems. With OptiSync, building auto-updating digital menu boards from your Toast API's data is simple.

Toast API requires a dynamically generated authentication token to be supplied with every API call, unlike many other POS systems that use a static API key. This adds some complexity to the integration that other POS systems don't have. However, using OptiSigns' API request and OptiSync, these added complexities are no trouble at all.

In this article, we'll provide a step-by-step guide on how to integrate your Toast API using OptiSigns API request, and how to create a DMB using OptiSync. Below are the high level steps we will follow:

1\. Get required information from Toast portal

2\. Get the Authentication Token from Toast (Inside Pre-Request step)

3\. Call the API to get the required data from Toast

4\. Use Toast API data to build DMB in designer with OptiSync

* * *

## Step 1: Preparation

To get started with integrating a Toast API with OptiSigns, we need the following information from the Toast system:

  * _toast-api-hostname_
  * clientId
  * clientSecret
  * userAccessType



Refer to Toast's Documentation [here](https://doc.toasttab.com/doc/devguide/portalHowToBuildAToastIntegration.html) for further details.

**NOTE**  
---  
In order to use Toast's API to read data, this requires **[Toast Standard API access](https://doc.toasttab.com/doc/devguide/devApiAccessUserGuide.html). **This usually comes with an additional charge (to Toast) of $25/month per location.   
  
* * *

## Step 2: Authentication for Toast API

For Toast API authentication, we will first need to pass the POST request to get the authentication token. The authentication token is then used to pass in the API request to get the data from Toast menus, orders etc. 

This authentication process will be handled using Pre-request processing with OptiSigns' API request. For more information about Pre-request processing and API requests in general, please check [here](https://support.optisigns.com/hc/en-us/articles/22875592994195).

In the Pre-request processing stage, the OptiSigns API calls the authentication API to get the necessary token, and sets it to the context of the API request.