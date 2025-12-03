# How to use Toast API data with OptiSigns
**Article URL:** https://support.optisigns.com/hc/en-us/articles/31113088917907-How-to-use-Toast-API-data-with-OptiSigns
**Article ID:** 31113088917907

In this example, the token is set to the context variable "authorization". When the API request is made, it will be able to use the authentication token. Below is a screenshot of this example in practice.

![](https://support.optisigns.com/hc/article_attachments/31870675893011)

Use this code snippet (with the data obtained earlier filling in the "xxx"s) to
    
    
    const body = {  
    "clientId": "xxx",  
    "clientSecret": "xxx",  
    "userAccessType": "xxx"  
    };  
    const {data, headers} = await os.postRequest("https://[toast-api-hostname]/authentication/v1/authentication/login", body );  
    const token = os.getValue(data.token.accessToken);  
    os.context.set("authorization", os.getValue(token));

* * *

## Step 3: Call the API to get the required data from Toast

Now we'll use the authorization token we received in Pre-request processing and pass it to the actual API call header. 

In the Header tab, create two parameters with the following values:

**authorization** Bearer {{authorization}}

**Toast-Restaurant-External-ID**

You can get the **Toast-Restaurant-External-ID value** from Toast Portal. This is the specific restaurant Id you want to get data for.

![](https://support.optisigns.com/hc/article_attachments/31870675894035)

Now put the desired API URL from which you want to get data. In this example we have used the following API to get the menus

  *     * <https://ws-api.toasttab.com/menus/v2/menus>



The final request will look something like this:

![](https://support.optisigns.com/hc/article_attachments/31870675898515)

You can enable this request and save the API. Click **Run Test**.

You should receive a _(200 OK)_ response, with data returning from the API. This means the API request has successfully contacted Toast and is transferring data.

![](https://support.optisigns.com/hc/article_attachments/31870683910291)

* * *

## Step 4: Build Digital Menu Board in Designer with OptiSync 

Now that your API request data source is ready for use, you can build your DMB using Designer with OptiSync. OptiSync allows you to map the API data to an element in the designer, either text or images. Using Repeaters, this data can be used to build out multiple item menus, and you're also able to define how you'd like to handle sold-out items, specials, and more.