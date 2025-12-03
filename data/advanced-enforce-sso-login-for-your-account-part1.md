# Advanced: Enforce SSO login for your account
**Article URL:** https://support.optisigns.com/hc/en-us/articles/360061576673-Advanced-Enforce-SSO-login-for-your-account
**Article ID:** 360061576673

### In this article, we'll explain how to enforce SSO logins for your OptiSigns account.

  * Setting Up Basic SSO Enforcement (Microsoft, Facebook, Google)
  * Setting Up SAML SSO Enforcement (MS Entra ID, Okta, OneLogin, Google Workspace)



By default, OptiSigns allows the use of Google, Facebook, or Microsoft accounts to access the OptiSigns portal:

![optisigns sso options](https://support.optisigns.com/hc/article_attachments/37792885011987)

However, some organizations have requirements to enforce SSO login for two-factor authentication and password protection purposes. OptiSigns supports this through Microsoft Entra ID and Google GSuite, as well as various SAML options requiring custom branding.

* * *

## Setting Up Basic SSO Enforcement

To set up basic SSO enforcement, go to the **Preferences** page in your OptiSigns portal:

![optisigns preferences tab](https://support.optisigns.com/hc/article_attachments/37792885015699)

You'll find the **Enforce Account SSO** option under the "General" section, right at the top of the page.

![optisigns enforce sso option](https://support.optisigns.com/hc/article_attachments/37792931285523)

Clicking on this will display several drop down options:

![optisigns enforce sso dropdown options](https://support.optisigns.com/hc/article_attachments/37792931288339)

Selecting either option will require any users logging on to OptiSigns to do so with their Google or Microsoft account. If a user tries to log in in any other way, they'll receive this error:

![optisigns failed login error example](https://support.optisigns.com/hc/article_attachments/1500001233801)

For more information, see our guide on **[User Management](https://support.optisigns.com/hc/en-us/articles/360046356113-Advanced-Security-Managing-User-Roles#AddingorInviting)**.

**Notes:** You will have to use the official <https://app.optisigns.com/> to log in to enforce SSO. You cannot use a custom domain with Enforce SSO, as the custom domain URL does not have an SSO login.

* * *

## Setting Up SAML SSO Enforcement (MS Entra ID, Okta, OneLogin, Google Workspace)

**NOTE:** This feature is available to **Pro Plus** , **Engage** , and **Enterprise** plan users.  
---  
  
Setting up SAML SSO enforcement requires setting up a subdomain, then configuring your settings on your client of choice.

We have numerous articles covering this process, as well as general best practices: