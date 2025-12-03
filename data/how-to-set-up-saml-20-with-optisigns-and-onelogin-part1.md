# How to set up SAML 2.0 with OptiSigns and OneLogin
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4407386819731-How-to-set-up-SAML-2-0-with-OptiSigns-and-OneLogin
**Article ID:** 4407386819731

With Pro Plus and Enterprise plan, you can configure SAML 2.0 with OptiSigns via OneLogin.

OneLogin will be acting as the IDP (Identify Provider), and OptiSigns will be working as the SP(Service Provider).

### **Set up OptiSigns & OneLogin:**

**First you need to do some set up in OptiSigns:**

If you don't have a sub domain yet, you can set up one by going to:  
<https://app.optisigns.com/app/s/branding-settings>

Fill in subdomain field and click Activate. After that you can use this sub domain for "  
You can also map your own domain like digitalsigns.yourcompany.com by following this [article](https://support.optisigns.com/hc/en-us/articles/1500000480302).

This will be the URL that you can share with your users so they can log in to use the app, once integration has set up. In our example we will use <https://advanced.optisigns.net/>

![mceclip13.png](https://support.optisigns.com/hc/article_attachments/19053401939731)

Next go to SAML Single Sign On setting page:

<https://app.optisigns.com/app/s/saml-settings>

Click Enable SAML SSO.

The settings are:

  * Enable Username & Password login: Allow users to also log in with username/password. It’s recommended to disable once integration is all done. As Admin/Owner, it's recommended that you keep at least 1 account with password log in, in case there's issues, you can always log back in from app.optisigns.com to reconfigure.
  * Enable User Creation: If users are authenticated, but do not exist in OptiSigns, they will be created in OptiSigns. You should enable this, because you likely already assign/approve users/groups to use OptiSigns, unless for some reason you want to be very strict and want to review roles of users before they can start using OptiSigns.
  * Enable User Override: Every time a user logs in, if their group assignment have changed on SAML, OptiSigns will update, override new profile settings.
  * Note the "Single Sign On URL" and "Audience URI (SP Entity ID) URL", you will need this to use in OneLogin later.



![](https://support.optisigns.com/hc/article_attachments/19053301304083)

**Next, add OptiSigns as an App in your OneLogin admin portal:**

Log in to your OneLogin portal as admin -> Applications

Click Add app

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/4407386965907)

On the next page, search for "SAML" in the search box, and then select the "SAML Custom Connector (Advanced)".