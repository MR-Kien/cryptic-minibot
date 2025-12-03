# SAML Integration Strategies & Best Practices
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4407128433299-SAML-Integration-Strategies-Best-Practices
**Article ID:** 4407128433299

There are many ways to implement SAML to manage users and access OptiSigns with your IDP.

Here are some high-level best practices with OptiSigns that will help to plan your integration and reduce overhead and manual work later.

This article focuses on integration strategies and approaches. For detailed step-by-step configurations by platform, see one of our guides:

  * [SAML SSO with Okta](https://support.optisigns.com/hc/en-us/articles/4404590815635-How-to-set-up-SAML-2-0-with-OptiSigns-and-Okta)
  * [SAML SSO with MS Entra ID](https://support.optisigns.com/hc/en-us/articles/4407252213395-How-to-Set-Up-SAML-2-0-with-OptiSigns-and-MS-Entra-ID-formerly-Azure-AD)
  * [SAML SSO with OneLogin](https://support.optisigns.com/hc/en-us/articles/4407386819731-How-to-set-up-SAML-2-0-with-OptiSigns-and-OneLogin)
  * [SAML SSO with OneLogin (Shibboleth)](https://support.optisigns.com/hc/en-us/articles/4407476403859-How-to-set-up-SAML-2-0-with-OptiSigns-and-OneLogin-Shibboleth)
  * [SAML SSO with Google Workspace](https://support.optisigns.com/hc/en-us/articles/4407493404307-How-to-set-up-SAML-2-0-with-OptiSigns-and-Google-Workspace)



## **Create a backup Admin account during set up:**

During set up, we recommend leaving Enable Username & Password login, and creating an Admin account with username/password to log back in and config, in case you accidentally lock yourself out by missing assignments of roles or groups.

You can disable this account later once your implementation is completed.

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/4407128153235)

In this case, you are planning not to use email as the unique identifier for the user, and use a username or employee ID instead. We recommend having this on, so the account owner and admin account will be able to manage the account without interruption, e.g. forgetting the password, or an issue with identifying the provider. 

## **Strategies for using SAML:**

#### **1) As an Authentication & Authorization Service (RECOMMENDED)**

SAML can be used to enforce identity verification, but also to enforce user, team, and role mapping in OptiSigns.