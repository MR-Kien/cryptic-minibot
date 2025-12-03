# How to Set Up SAML 2.0 with OptiSigns and MS Entra ID (formerly Azure AD)
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4407252213395-How-to-Set-Up-SAML-2-0-with-OptiSigns-and-MS-Entra-ID-formerly-Azure-AD
**Article ID:** 4407252213395

Now enable **Enable SAML SSO**. There should be a green checkmark next to the option. This will expand the options available to you.

![saml sso settings checklist](https://support.optisigns.com/hc/article_attachments/37186682762387)

The other settings are:

  * **Enable Username & Password Login - **Allow users to also log in with username/password. We recommend disabling this once integration is finished. As Admin/Owner, it’s recommended to keep at least 1 account with a password login in case there are issues. You can use this account to login directly to the app to reconfigure if necessary.
  * **Enable User Creation -** If users are authenticated but do not exist in OptiSigns, they will be created in the OptiSigns app. We recommend enabling this unless you wish to be extremely strict and want to review the roles of users before they can start using OptiSigns.
  * **Enable User Override -** Every time a user logs in, OptiSigns will check their group assignment. If it has changed on SAML, OptiSigns will update their permissions within the app.



Next, note your **Single Sign On URL** and **Audience URI (SP Entity ID) URL**. You will need to use these later.

![](https://support.optisigns.com/hc/article_attachments/37186635040403)

* * *

## Add OptiSigns as an App in Microsoft Entra ID Portal

Log in to your Microsoft Azure portal as an administrator, then navigate to **Enterprise Applications**.

Click **New Application**.

![creating new enterprise application ms azure](https://support.optisigns.com/hc/article_attachments/37186682790803)

Select **Create your application**. This pops up a sidebar on the right. Inside, input “OptiSigns” as the name of the app, and choose **Integrate any other application you don’t find in the gallery (Non-gallery)**. Finally, hit **Create**.

![create own application ms azure](https://support.optisigns.com/hc/article_attachments/37186682801427)

This will take a moment, but you’ll eventually be brought to an Overview screen.

Click **Set up single sign on.**

![setting up single sign on ms azure](https://support.optisigns.com/hc/article_attachments/37186682808851)

Click **SAML**. This will begin the setup of SAML-based Sign-on.

![saml ms azure](https://support.optisigns.com/hc/article_attachments/37186635065235)

Here, click **Edit** in the Basic SAML Configuration section. This is where you should provide the Single Sign On URL and SP Entity ID you got in the last step.

![basic saml configuration](https://support.optisigns.com/hc/article_attachments/37186635074707)