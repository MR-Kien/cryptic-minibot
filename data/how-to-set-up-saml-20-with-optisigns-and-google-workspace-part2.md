# How to set up SAML 2.0 with OptiSigns and Google Workspace
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4407493404307-How-to-set-up-SAML-2-0-with-OptiSigns-and-Google-Workspace
**Article ID:** 4407493404307

In the popup window, enter OptiSigns as the name of the app, you can upload the app icon here as well. Then click continue.

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/4407485688467)

The next page will provide the IDP data. Get these 2 highlighted information then click continue, these need to be maintained in the OptiSigns SAML SSO settings later.

![](https://support.optisigns.com/hc/article_attachments/21287044557843)

Next page will be the SP information, this is where you should provide the Single Sign On URL, and SP Entity ID you get from your OptiSigns SAML SSO setting.

SP Entity ID from OptiSigns SAML SSO setting should be put under Entity ID.

Single Sign On URL from OptiSigns SAML SSO setting should be put under ACS URL.

Also, set the Name ID format to Email.

![](https://support.optisigns.com/hc/article_attachments/21286792807699)

The next page is where you maintain the attributes. This step will be explained later in this article. Click Finish, and the app is added to the Google Workspace.

![](https://support.optisigns.com/hc/article_attachments/21286840258963)

After completing the app creation on Google Workspace. You can select the OptiSigns app under the "Web and mobile apps". Click on the OptiSigns app, and note the ID in the URL, that is the SPID that will be needed.

![mceclip7.png](https://support.optisigns.com/hc/article_attachments/4407493347731)

Go back to your OptiSigns account maintain above mentioned 3 fields, and save it.

You can get SSO URL, Entity ID, and Certificate from your Google Workspace.

  * Put SSO URL from Google Workspace under SAML 2.0 Endpoint (HTTP).
  * Put Entity ID from Google Workspace under Identity Provider Issuer.
  * Put the content from the base64 encoded certificate under Public Certificate.



![](https://support.optisigns.com/hc/article_attachments/21287166076819)

Now your login portal & integration are all setup.

#### **Assign & map users, and groups from Google Workspace to OptiSigns**

It's not required, but recommended to create groups of users to be assigned, and map to OptiSigns Roles, and Teams so they will automatically have the right role & group.

**IMPORTANT NOTE: If you don't configure this, all users will be assigned User Role & Default Team (screenshot see below)**

To configure how OptiSigns should map the user groups to OptiSigns Roles by going to: <https://app.optisigns.com/app/s/saml-settings>