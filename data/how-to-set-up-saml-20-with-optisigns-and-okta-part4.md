# How to set up SAML 2.0  with OptiSigns and Okta
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4404590815635-How-to-set-up-SAML-2-0-with-OptiSigns-and-Okta
**Article ID:** 4404590815635

OptiSigns accept firstName, lastName, and group by default, but if you change these in Okta, you will need to match it here as well.

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/4404812916115)

**Additional Note:**

If you want your user to login to the OptiSigns portal via OKTA portal, Okta does not support the IDP that is initiated. It will use the Bookmark App on Okta, You can follow this article to set up the Bookmark app: <https://support.okta.com/help/s/article/How-do-you-create-a-bookmark-app?language=en_US>

#### **I've made it into my OptiSigns account, but don't seem to have all the side menu options I'm used to. What’s going on?**

It's likely you've signed on through your Branded Portal, using a URL similar to this one:
    
    
    https://app.optisigns.com/signIn/<accountId>

You'll first need to find your OptiSigns Account ID. To do this, simply find a paired screen, and hit **Edit → Advanced → More**.

![edit screen advanced more](https://support.optisigns.com/hc/article_attachments/38962229904659)

Click **Device Info:**

![info button edit screen](https://support.optisigns.com/hc/article_attachments/38962229906835)

Find the **"accountId"** number, then write it down somewhere. You'll be needing it soon.

![](https://support.optisigns.com/hc/article_attachments/38962235455635)

Now copy the following URL, being sure to substitute your account ID where appropriate:
    
    
    https://app.optisigns.com/signIn/<accountId>

Now you'll want to set this URL up as an Okta bookmark. You can follow this article to set up the Bookmark app: <https://support.okta.com/help/s/article/How-do-you-create-a-bookmark-app?language=en_US>

### **That's it!**

You have configured SAML 2.0 for OptiSigns with Okta.

Now your users can log in using the subdomain that you configured (in this case it was <https://advanced.optisigns.net/signIn>).

You can share the URL with your users and they can log in with their SSO credentials.

If you have any additional questions or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
