# How to set up SAML 2.0  with OptiSigns and Okta
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4404590815635-How-to-set-up-SAML-2-0-with-OptiSigns-and-Okta
**Article ID:** 4404590815635

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/4404598581779)

Select SAML 2.0

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/4404590829203)

Enter App name: OptiSigns

If you want to upload a logo, you can use our logo [here](https://download.optisignsapp.com/marketing/optisigns-logo.png).

Click Next

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/4404590844691)

In "Single sign-in URL" and "Audience URI (SP Entity ID)", these are the URL that you have in <https://app.optisigns.com/app/s/saml-settings>  
Check "Use this for Recipient URL and Destination URLs"

Click Next.

![mceclip5.png](https://support.optisigns.com/hc/article_attachments/4404608330003)

![](https://support.optisigns.com/hc/article_attachments/28207766417811)

The last step is just informational for Okta to know how you are using the app.

Select "I'm an Okta customer adding an internal app" as OptiSigns is now an internal app in your organization.

Click Next.

![mceclip8.png](https://support.optisigns.com/hc/article_attachments/4404615741075)

Then click "View Setup Instruction"

Copy these 3 fields and paste into OptiSigns' SAML config page:

  * Identity Provider Single Sign-On ULR -> OptiSigns: SAML 2.0 Endpoint (HTTP)
  * Identity Provider Issuer -> OptiSigns: Identity Provider Issuer
  * X.509 Certificate -> OptiSigns: Public Certificate



![okta-config.png](https://support.optisigns.com/hc/article_attachments/4404615786259)

Lastly, set the "Sign In Button label", this is the text of the button you want your users to see in their login portal. Use something descriptive like "Log in with Okta" "Sign in with SSO" or something your user is familiar with.

![okta-config-2.png](https://support.optisigns.com/hc/article_attachments/4404615885331)

Click Save

Now your login portal & integration are all setup.

Next, you need to assign users, and groups that can use OptiSigns.

#### **Assign & map users, and groups from Okta to OptiSigns**

It's not required, but recommended to create groups of users to be assigned, and map to OptiSigns Roles, and Teams so they will automatically have the right role & group.

**IMPORTANT NOTE: If you don't configure this, all users will be assigned User Role & Default Team (screenshot see below)**