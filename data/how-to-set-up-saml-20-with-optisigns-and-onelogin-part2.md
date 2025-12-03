# How to set up SAML 2.0 with OptiSigns and OneLogin
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4407386819731-How-to-set-up-SAML-2-0-with-OptiSigns-and-OneLogin
**Article ID:** 4407386819731

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/4407387031315)

Enter "OptiSigns" in the display name, then click Save. You can also upload the OptiSigns logo here as well.

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/4407392839187)

After saving, go to the configuration page. This is where you should provide the Single Sign On URL, and SP Entity ID you get from your OptiSigns SAML SSO setting.

  * SP Entity ID from OptiSigns SAML SSO setting should be put under **Audience (EntityID)** and **Login URL**.
  * Single Sign On URL from OptiSigns SAML SSO setting should be put under **Recipient** , **ACS URL validator,** and **ACS URL**. 
  * Change the **SAML initiator** to the **Service Provider**



![](https://support.optisigns.com/hc/article_attachments/19053399114899)

Then go to the SSO page. Get these 3 highlighted information, these need to be maintained in the OptiSigns SAML SSO settings. After clicking View Details of the certificate, you can find the encoded content of the certificate, this will be needed in the next step.

![](https://support.optisigns.com/hc/article_attachments/19053348948883)

Go back to your OptiSigns account maintain above mentioned 3 fields, and save it.

Put the SAML 2.0 endpoint from OneLogin under the SAML 2.0 Endpoint.

Put the Issuer URL from OneLogin under Identity Provider Issuer.

Put the content from base64 encoded x509 certificate under Public Certificate.

![](https://support.optisigns.com/hc/article_attachments/19053330062483)

Now your login portal & integration are all setup.

#### **Assign & map users, and groups from OneLogin to OptiSigns**

It's not required, but recommended to create groups of users to be assigned, and map to OptiSigns Roles, and Teams so they will automatically have the right role & group.

**IMPORTANT NOTE: If you don't configure this, all users will be assigned User Role & Default Team (screenshot see below)**

To configure how OptiSigns should map the user groups to OptiSigns Roles by going to: <https://app.optisigns.com/app/s/saml-settings>

Scroll to Advanced Settings and create a mapping.  
Group Name (roles assigned to the user from OneLogin), Role (role in OptiSigns) mapping.   
![mceclip9.png](https://support.optisigns.com/hc/article_attachments/4407387515155)