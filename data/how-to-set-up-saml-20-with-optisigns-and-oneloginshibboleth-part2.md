# How to set up SAML 2.0 with OptiSigns and OneLogin(Shibboleth)
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4407476403859-How-to-set-up-SAML-2-0-with-OptiSigns-and-OneLogin-Shibboleth
**Article ID:** 4407476403859

![mceclip6.png](https://support.optisigns.com/hc/article_attachments/4407476998035)

On the next page, search for "SAML" in the search box, and then select the "SAML Custom Connector (SP Shibboleth)".

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/4407468255507)

Enter "OptiSigns" in the display name, then click Save. You can also upload the OptiSigns logo here as well.

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/4407476590867)

After saving, go to the configuration page. This is where you should provide the Single Sign On URL, and SP Entity ID you get from your OptiSigns SAML SSO setting.

SP Entity ID from OptiSigns SAML SSO setting should be put under the Login URL.

Single Sign On URL from OptiSigns SAML SSO setting should be put under ACS URL and ACS URL validator. Please remember to escape the special character in the ACS URL validator.

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/4407476626451)

Then go to the SSO page. Get these 3 highlighted information, these need to be maintained in the OptiSigns SAML SSO settings. After clicking View Details of the certificate, you can find the encoded content of the certificate, this will be needed in the next step.

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/4407476684179)

Go back to your OptiSigns account maintain above mentioned 3 fields, and save it.

Put the SAML 2.0 endpoint from OneLogin under the SAML 2.0 Endpoint.

Put the Issuer URL from OneLogin under Identity Provider Issuer.

Put the content from base64 encoded x509 certificate under Public Certificate.

![mceclip6.png](https://support.optisigns.com/hc/article_attachments/21286544110099)

Now your login portal & integration are all set up.

#### **Assign & map users, and groups from OneLogin to OptiSigns**

It's not required, but recommended to create groups of users to be assigned, and map to OptiSigns Roles, and Teams so they will automatically have the right role & group.

**IMPORTANT NOTE: If you don't configure this, all users will be assigned User Role & Default Team (screenshot see below)**

To configure how OptiSigns should map the user groups to OptiSigns Roles by going to: <https://app.optisigns.com/app/s/saml-settings>