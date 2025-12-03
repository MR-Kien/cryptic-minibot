# How to Set Up a PowerBI Service Principal for Use in OptiSigns
**Article URL:** https://support.optisigns.com/hc/en-us/articles/32860569148819-How-to-Set-Up-a-PowerBI-Service-Principal-for-Use-in-OptiSigns
**Article ID:** 32860569148819

### In this article, we will walk you through the process of setting up a service principal for PowerBI in Microsoft Azure, and connecting it to OptiSigns.

  * Creating an Entra App in Microsoft Azure
  * Enable PowerBI Service Admin Settings
    * Add the Service Principal to a Workspace
  * Authenticating OptiSigns via Service Principal
  * Getting PowerBI onto a Screen



Using a PowerBI service principal with app registration is a preferred option for companies with strict information security rules that don't want to use individual user accounts for PowerBI integration. 

This reduces headaches in situations when:

  * There is a position or permission change of a user and authentication needs to be performed again by a different user.
  * A prolonged authentication token period cannot be set for individual users, and you will need to reauthorize and refresh the token every couple of months.



Using a PowerBI service principal, the authentication tokens are associated with a registered app instead of a user. This allows you to set a longer validity time for the authentication token and avoids more frequent re-authorization. Using service principal with App registration for Power BI integration is supported well with OptiSigns.

**NOTE:** This feature is only available to customers on an **Enterprise** plan.  
---  
  
* * *

## Create an Entra App in Microsoft Azure

An Entra app will be responsible for handling identity and access management for your service principal. In order to create one, you’ll need to login to Microsoft Azure with a viable Microsoft account.

Once at the Azure portal, search for **“app registrations,”** then select **App Registrations** from the list that appears:

![app registration instructions in microsoft azure](https://support.optisigns.com/hc/article_attachments/32860610406547)

Create a **New Registration**.

![how to create a new registration in microsoft azure](https://support.optisigns.com/hc/article_attachments/32860569069459)

On this screen, type a name for the app, then leave the other settings as default. These can be changed or altered at any time.

![instructions on registering an application in microsoft azure](https://support.optisigns.com/hc/article_attachments/32860610418707)

Once done, hit **Register.**

* * *

## Enable PowerBI Service Admin Settings

Follow this link to the [PowerBI Admin Portal](https://app.powerbi.com/admin-portal/capacities?experience=power-bi).

Once there, click **Tenant Settings**. Then, scroll down to **Developer Settings**.

![finding developer settings in tenant settings within powerbi admin portal](https://support.optisigns.com/hc/article_attachments/32860610420627)

Enable the **Embed Content in Apps Settings** , as below:

![how to enable embed content in apps](https://support.optisigns.com/hc/article_attachments/32860610421779)