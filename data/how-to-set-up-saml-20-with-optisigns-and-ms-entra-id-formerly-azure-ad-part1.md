# How to Set Up SAML 2.0 with OptiSigns and MS Entra ID (formerly Azure AD)
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4407252213395-How-to-Set-Up-SAML-2-0-with-OptiSigns-and-MS-Entra-ID-formerly-Azure-AD
**Article ID:** 4407252213395

### In this article, we will provide a step-by-step guide to setting up SAML 2.0 with Microsoft Entra ID for use with OptiSigns.

  * Set Up OptiSigns Subdomain and SAML SSO Settings
    * Setting up a Custom Subdomain
    * Setting up SAML SSO Settings
  * Add OptiSigns as an App in Azure Portal
  * Assign and Map Users and Groups from Azure to OptiSigns (OPTIONAL)
    * How to Handle Unmapped Users and Groups (OPTIONAL)
    * Managing Attributes & Claims in Microsoft Azure (OPTIONAL)
      * Creating Group Claims (OPTIONAL)
      * Customizing Claims for Use with OptiSigns (OPTIONAL)
  * Setting Up OptiSigns Login to Appear in Office.com (OPTIONAL)
  * Frequently Asked Questions



**NOTE:** This feature is available to **Pro Plus** , **Engage** , and **Enterprise** plan users.  
---  
  
SAML (Security Assertion Markup Language) 2.0 allows a single authorization to access multiple systems. This can be configured to allow easy access to OptiSigns digital signage through your Microsoft Entra ID. Entra ID will act as the IDP (Identity Provider), with OptiSigns will work as the SP (Service Provider). Here is a quick video showing how to set up SAML 2.0 with Entra ID (when it was known as Azure AD):

* * *

## Set Up OptiSigns Subdomain and SAML SSO Settings

To begin, you’ll need to perform some functions within the OptiSigns app, including:

  * Creating a Custom Subdomain
  * Setting up SAML SSO Settings



Now, let’s begin.

### Setting up a Custom Subdomain

First, ensure you have an OptiSigns subdomain. This can be obtained by going to the [Branding Settings](https://app.optisigns.com/app/s/branding-settings) page.

Fill in the subdomain field and click **Activate**. Now you can use this subdomain for a variety of functions, including SAML setup. You can also map your domain by following our article on [Custom Domain mapping](https://support.optisigns.com/hc/en-us/articles/1500000480302-Advanced-Custom-Domain-mapping).

This subdomain will be the URL to share with your users so they can log in to use the app after integration has been set up.

For this example, we will use [https://optisignsdemo-ad.optisigns.net/](https://optisignsdemo-ad.optisigns.net/) as our URL.

### Setting up SAML SSO Settings

Go to the SAML Single Sign-On Setting Page:

![go to saml single sign on page](https://support.optisigns.com/hc/article_attachments/37186635027731)