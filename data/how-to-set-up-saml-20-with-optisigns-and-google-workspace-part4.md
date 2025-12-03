# How to set up SAML 2.0 with OptiSigns and Google Workspace
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4407493404307-How-to-set-up-SAML-2-0-with-OptiSigns-and-Google-Workspace
**Article ID:** 4407493404307

You'll first need to find your OptiSigns Account ID. To do this, simply find a paired screen, and hit **Edit → Advanced → More**.

![edit screen advanced more](https://support.optisigns.com/hc/article_attachments/38962512579219)

Click **Device Info:**

![info button edit screen](https://support.optisigns.com/hc/article_attachments/38962512582675)

Find the **"accountId"** number, then write it down somewhere. You'll be needing it soon.

![](https://support.optisigns.com/hc/article_attachments/38962490259731)

Now copy the following URL, being sure to substitute your account ID where appropriate:
    
    
    https://app.optisigns.com/signIn/<accountId>

Then put this URL in your Google Workspace under SSO URL.

### **That's it!**

You have configured SAML 2.0 for OptiSigns with Google Workspace.

Now your users can log in using the subdomain that you configured (in this case it was <https://advanced.optisigns.net/signIn>).

You can share the URL with your users and they can log in with their SSO credentials.

If you have any additional questions or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
