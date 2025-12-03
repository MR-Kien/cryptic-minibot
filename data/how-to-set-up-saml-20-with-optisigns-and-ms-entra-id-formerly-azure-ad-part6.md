# How to Set Up SAML 2.0 with OptiSigns and MS Entra ID (formerly Azure AD)
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4407252213395-How-to-Set-Up-SAML-2-0-with-OptiSigns-and-MS-Entra-ID-formerly-Azure-AD
**Article ID:** 4407252213395

It’s often convenient to have the OptiSigns app appear as a clickable option on your company’s Office.com portal.

To set this up, you'll first need to find your OptiSigns Account ID. To do this, simply find a paired screen, and hit **Edit → Advanced → More**.

![edit screen advanced more](https://support.optisigns.com/hc/article_attachments/38825933298579)

Click **Device Info:**

![info button edit screen](https://support.optisigns.com/hc/article_attachments/38825917033875)

Find the **"accountId"** number, then write it down somewhere. You'll be needing it soon.

![](https://support.optisigns.com/hc/article_attachments/38825917043475)

Now copy the following URL, being sure to substitute your account ID where appropriate:
    
    
    https://app.optisigns.com/signIn/<accountId>

Next, head back to your Azure portal, and go to **SAML-based Sign-on**. Once there, find **Basic SAML Configuration** and hit **Edit.** This will open up a sidebar. Simply paste/type your URL into the **Sign on URL (Optional)** and **Relay State**(Optional) fields.

![](https://support.optisigns.com/hc/article_attachments/38838224681235)

This will allow the OptiSigns app to appear in your Microsoft Office portal. This will also provide the full range of options for your side menu.

![optisigns app in ms office portal](https://support.optisigns.com/hc/article_attachments/37186635219219)

* * *

## Frequently Asked Questions

Here, we’ll answer some of the most common questions we get around this topic.

#### **I Got this Error Message. Help?**

Unable to process request due to missing initial state. This may happen if browser sessionStorage is inaccessible or accidentally cleared. Some specific scenarios are - 1) Using IDP-Initiated SAML SSO. 2) Using signInWithRedirect in a storage-partitioned browser environment.

![optisigns common error message](https://support.optisigns.com/hc/article_attachments/37186635223443)

This error appears for one of two reasons:

  1. The wrong URL was input. This is frequently (https://auth.optisigns.com/__/auth/handler)
  2. The user has tried to access the OptiSigns portal from Office.com without setting up SAML SSO in Microsoft Azure correctly.



The easiest way to solve this problem is to login through your branded URL.

![branded url example](https://support.optisigns.com/hc/article_attachments/37186682989075)

This will be unique to your organization. For more information, follow the steps outlined in the “Add OptiSigns as an App in Microsoft Entra ID Portal” section.