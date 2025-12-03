# How to Integrate API and Publish API Data via OptiSync
**Article URL:** https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync
**Article ID:** 22875592994195

To test the request, we'll need to configure the header. This is where the Keystore comes in. In the second box, type **Bearer {{apiKeystore. <<key>>}}**, where _Bearer_ is the type of token and _{{apiKeystore. <<key>>}}_ pulls the token stored in the Keystore. In this example, we'll use the name "clover" as referenced above.

Once that's done, click **"Run Test"**. If the response code is 200, the API has returned data successfully. If there is any other code, there is an issue in the API Request.

![](https://support.optisigns.com/hc/article_attachments/22917836593171)

#### How to Use Parameters

Parameters are present in URLs of all types. There are two elements to a parameter:

  * They have to follow a '?' mark in the URL;
  * They have a value associated with them



The **Params** tab lets you specify the Parameters whose value you would like to change.

Usually, the **Params** tab is used in conjunction with the Pre-request and Post-request tabs to create automatically updating values.

#### How to Use Pre- and Post-Request Processing

To use pre- and post-request processing, some amount of Javascript knowledge is needed.

What is the Difference Between the Two?  
---  
**Pre-request:** This is a code snippet normally set the context _**before**_ the API request. This can be retrieving an authentication token from another API, or to change parameters to allow for more automation.  
**Post-request:** A piece of code to apply to the data _**received from**_ the API request. This code can be used to modify the received data to change how it is displayed on your screens.  
  
The **Pre-request** tab is where you'll input code for pre-request processing.

**Example:** For the systems that requires a dynamically generated authentication token like Toast, this can be used to call another API to retrieve the authentication token and set it to the context of the API.

For more on this example, see this article on [how to connect your Toast API](https://support.optisigns.com/hc/en-us/articles/31113088917907-How-to-use-Toast-API-data-with-OptiSigns).

The **Post-request** tab is where you'll input code for post-request processing.

**Example:** You are receiving data from your point-of-sale (POS) software API, but certain pieces of data aren't displaying the way you'd like.

Prices may display as whole numbers (i.e. 1299) instead of as a proper pricing (i.e. $12.99). For this, we'd need a piece of code to convert the whole number into a price, and have that code be extensible to any similar display errors (e.g. 1899 instead of $18.99).