# How to Set Up an Outlook Calendar App with Shared Permissions
**Article URL:** https://support.optisigns.com/hc/en-us/articles/45619214182803-How-to-Set-Up-an-Outlook-Calendar-App-with-Shared-Permissions
**Article ID:** 45619214182803

### In this article, we'll go over how to set up Shared Permissions to show Room or Equipment Resources on an Outlook Calendar with OptiSigns.

  * What You'll Need
  * Step 1: Granting the Proper Resource Permissions to a User Account
  * Step 2: Displaying the Resource in the User's Outlook Calendar



When using Outlook calendar in an organization, you are often granted access to various calendars. These may be for other individuals, or they may show the availability of certain shared resources, such as Rooms or Equipment.

While OptiSigns currently does not support showing multiple user calendars at once (see our [**Calendar Mix**](https://support.optisigns.com/hc/en-us/articles/4408052949139-How-to-use-Calendar-Mix-app) app for doing that), it is possible to show those Resources. However, specific permissions will need to be granted via your Microsoft Admin account in order to do this.

Let's get started.

* * *

## What You'll Need

To set up Resource permissions and display them on OptiSigns, you'll need:

  * Administrator Access to a Microsoft Business Account
  * A Room or Equipment Resource to display
  * An OptiSigns****[**Standard Plan or higher**](https://www.optisigns.com/pricing)



* * *

## Step 1: Granting the Proper Resource Permissions to a User Account

To get started, we'll need to open up the [**Microsoft Exchange Admin center**](https://admin.exchange.microsoft.com/#/resources). This is where permissions of this type are handled.

Navigate through the sidebar to the **Resources** tab. Here, select either **Add a Room Resource, Add an Equipment Resource,** or an already made Resource.

![exchange admin center resource example](https://support.optisigns.com/hc/article_attachments/45619197975827)

You'll see that the **Type** displays what type of resource it is, whether Room or Equipment. These resources are distinct from Users, and have different permissions.

Click the Display Name of the resource you want to change the permissions of to continue:

![microsoft room 1](https://support.optisigns.com/hc/article_attachments/45619197976339)

Next, navigate to the **Delegation** tab, then hit **Edit** under the "Read and manage" section:

![microsoft room permissions delegation](https://support.optisigns.com/hc/article_attachments/45619197976723)

On the Manage delegates screen, click **Add Member:**

![](https://support.optisigns.com/hc/article_attachments/45619197981459)

This will open up the "Add read and manage permissions tab." Here, select the Display Name of the user you want to set up OptiSigns with.

![microsoft exchange admin read manage permissions](https://support.optisigns.com/hc/article_attachments/45619197986195)