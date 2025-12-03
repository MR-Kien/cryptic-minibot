# How to set up SAML 2.0 with OptiSigns and Google Workspace
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4407493404307-How-to-set-up-SAML-2-0-with-OptiSigns-and-Google-Workspace
**Article ID:** 4407493404307

With Pro Plus and Enterprise plan, you can configure SAML 2.0 with OptiSigns via Google Workspace. The Google Workspace will be acting as the IDP (Identify Provider), and OptiSigns will be working as the SP(Service Provider).

### **Set up OptiSigns & Google Workspace:**

**First you need to do some set up in OptiSigns:**

If you don't have a sub domain yet, you can set up one by going to:  
<https://app.optisigns.com/app/s/branding-settings>

Fill in subdomain field and click Activate. After that you can use this sub domain for "  
You can also map your own domain like digitalsigns.yourcompany.com by following this [article](https://support.optisigns.com/hc/en-us/articles/1500000480302).

This will be the URL that you can share with your users so they can log in to use the app, once integration has set up. In our example we will use <https://advanced.optisigns.net/>

![mceclip13.png](https://support.optisigns.com/hc/article_attachments/21287201525907)

Next, go to the SAML Single Sign On setting page:

<https://app.optisigns.com/app/s/saml-settings>

Click Enable SAML SSO.

The settings are:

  * Enable Username & Password login: Allow users to also log in with username/password. It’s recommended to disable it once the integration is all done. As Admin/Owner, it's recommended that you keep at least 1 account with a password log in, in case there are issues, you can always log back in from app.optisigns.com to reconfigure.
  * Enable User Creation: If users are authenticated, but do not exist in OptiSigns, they will be created in OptiSigns. You should enable this, because you likely already assign/approve users/groups to use OptiSigns, unless for some reason you want to be very strict and want to review roles of users before they can start using OptiSigns.
  * Enable User Override: Every time a user logs in, if their group assignment have changed on SAML, OptiSigns will update, override new profile settings.
  * Note the "Single Sign On URL" and "Audience URI (SP Entity ID) URL", you will need this to use in Google Workspace later.



![](https://support.optisigns.com/hc/article_attachments/21286640961939)

**Next, add OptiSigns as an App in your Google Workspace admin portal:**

Log in to your Google Workspace portal as admin -> Apps -> Web and mobile apps

Click Add app -> Add custom SAML app ![mceclip0.png](https://support.optisigns.com/hc/article_attachments/4407485683475)