# How to Integrate API and Publish API Data via OptiSync
**Article URL:** https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync
**Article ID:** 22875592994195

Now, we're ready to set up your API request.

* * *

### Step 2: Set Up and Test the API Request

Before moving forward in OptiSigns, we recommend [**testing your API**](https://www.postman.com/api-platform/api-testing/) connection using a free tool, such as [**Postman**](https://www.postman.com/). This provides several advantages, including:

  * Checking your data formatting
  * Ensuring the correct data is being provided
  * Verifying your authentication
  * Identifying integration problems or connection errors



The test parameters, endpoints, and authenticators can then be used in OptiSigns to set up your API request. Here's how to do that.

![firefox_orSTybxxGU.png](https://support.optisigns.com/hc/article_attachments/32427362124563)

Click the **Add Request** button, it will launch the window for you to configure and test the API request.

![firefox_owER9ex9xQ.png](https://support.optisigns.com/hc/article_attachments/32427362128147)

  * **Display Name -** This will be shown under the API gateway list, mainly to help users identify the API request.
  * **Name -** This is used as a reference to the API request, it is a technical name that will be used later in the path to refer to the API request data. 
  * **URL -** This is the API endpoint, you can use the GET or POST method depending on the API request, for example, if you are using GraphQL, then all requests will be using POST.
  * **Params -** Allows you to define the parameters in your API request. You may see parameters in your API endpoint URL, these will be preceded by a "?" mark. These can be used in pre and post processing request code to further automate your API request.
  * **Headers -** The header(s) of the API request. You will want to input your API Authentication token here.
  * **Pre-request -** An optional piece of code which prepares the context before the API request. For example, you may need to call another API to get a short-lived authentication token before calling the API, or you need to calculate some variables to be used in the API request.
  * **Post-request -** An optional piece of code which modifies the data received from the request. For example, if the data you receive is not exactly how you want it displayed, you can write a bit of code to modify it according to your digital display needs.
  * **Enable Webhook -** Generates a webhook link and an associated token. This webhook can be used to notify us of a change in the data, which will refresh the API request and update your screens automatically.
  * **Enable this Request** \- Set the status of the API request.

