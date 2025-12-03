# How to Set Up SAML 2.0 with OptiSigns and MS Entra ID (formerly Azure AD)
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4407252213395-How-to-Set-Up-SAML-2-0-with-OptiSigns-and-MS-Entra-ID-formerly-Azure-AD
**Article ID:** 4407252213395

Place the Single Sign On URL under **Reply URL** and the SP Entity ID under **Identifier**.

![identifier and reply URL saml config ms azure](https://support.optisigns.com/hc/article_attachments/37186682845331)

Next, note the next two sections: **SAML Certificates** and **Set up OptiSigns**. You’ll need to obtain three key pieces of information:

  1. Certificate (Base64)
  2. Login URL
  3. Microsoft Entra Identifier



![three key pieces of information ms azure](https://support.optisigns.com/hc/article_attachments/37186682850067)

These will need to be maintained within the OptiSigns app, in the SAML SSO Settings page.

Now go back to your OptiSigns account and input these three pieces of information in the following places:

  1. **Login URL** should go under **SAML 2.0 Endpoint (HTTP)**
  2. **Microsoft Entra Identifier** should go under **Identity Provider Issuer**
  3. The content of the downloaded **Certificate (Base64)** should be pasted under **Public Certificate**.



![setup SAML authentication optisigns](https://support.optisigns.com/hc/article_attachments/37186682855955)

With this, your login portal and integration are all set up. If this is all you need, you’re done. If you’d like to manage users, groups, and teams, keep reading.

* * *

## Assign and Map Users and Groups from Azure to OptiSigns (OPTIONAL)

We highly recommend creating groups of users to be assigned within Azure to be automatically mapped to OptiSigns with the correct role and group.

**NOTE:** Without configuring this, all users will be assigned User Role and Default Team. You will have to manually change their roles and teams within the OptiSigns app.  
---  
  
Head back to the [SAML settings page](https://app.optisigns.com/app/s/saml-settings) within OptiSigns. Scroll to **Advanced Settings** and you should see this:

![group mapping optisigns](https://support.optisigns.com/hc/article_attachments/37186635103379)

By default, unmapped users/groups become Users within the Default Team in OptiSigns. To link OptiSigns to Azure, either create a new mapping by clicking **Add** or edit one of the existing Group mappings.

The “Group Name” within OptiSigns corresponds to the “Group ID” within Azure. To find this information, go to your Azure Portal and select **Groups**.

![groups tab ms azure](https://support.optisigns.com/hc/article_attachments/37186682869779)

Your Object ID can be found here for each group you’ve created.