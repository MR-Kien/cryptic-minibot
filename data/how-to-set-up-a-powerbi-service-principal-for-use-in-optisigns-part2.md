# How to Set Up a PowerBI Service Principal for Use in OptiSigns
**Article URL:** https://support.optisigns.com/hc/en-us/articles/32860569148819-How-to-Set-Up-a-PowerBI-Service-Principal-for-Use-in-OptiSigns
**Article ID:** 32860569148819

In this example, we’ve set this embed to apply permissions to the entire organization. However, you can restrict access to specific security groups based on your needs. These security settings can be changed as per your requirements.

Next, **Enable Service principals can create workspaces, connections, and deployment pipelines** and **Enable Service Principals can call Fabric public APIs** , as below:

![image \(28\)\(1\).png](https://support.optisigns.com/hc/article_attachments/42225175622675)

Like before, we’ve applied these to the entire organization. Just like the last step, you can restrict access to specific security groups based on your needs.

### Add the Service Principal to a Workspace

Now we need to assign service principal access to the workspaces you want to show in your PowerBI reports.

In the admin portal, click **Workspaces**. You’ll want to go to the workspace you want to assign service principal access to. Click the workspace, then hit **Access**.

![how to grant service principal access powerbi](https://support.optisigns.com/hc/article_attachments/32860610425107)

Add the service principal you created in the last step as a member of the workspace.

![how to add service principal as a member of powerbi workspace](https://support.optisigns.com/hc/article_attachments/32860569093139)

* * *

## Authenticating OptiSigns via Service Principal

In order to authenticate your PowerBI on OptiSigns via service principal, you’ll need four pieces of information:

  1. Name of the service principal
  2. Application (client) ID
  3. Directory (tenant) ID
  4. Application (client) secret



Since we’ve already created an Entra app in Azure, we already have access to the first three pieces of information. These can be found under **App Registrations** back in Azure.

![where to find app registration information in microsoft azure](https://support.optisigns.com/hc/article_attachments/32860569095571)

In this example, the values have been blurred, but on your Azure portal, these should be visible.

The only piece of information you won’t have is the client secret. To get that, click **Manage → Certificates & Secrets → Client Secrets → New Client Secret**

**![how to create new client secret in microsoft azure](https://support.optisigns.com/hc/article_attachments/32860569099411)**

Next, set the **Description** and **Expiry** , then click **Add**.

![how to add a client secret](https://support.optisigns.com/hc/article_attachments/32860569100947)

The **Value** present is the last piece of information you need.

Now, head into the OptiSigns app. Click your **Profile name → More → Integrations.**