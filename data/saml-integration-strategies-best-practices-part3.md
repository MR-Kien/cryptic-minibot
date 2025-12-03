# SAML Integration Strategies & Best Practices
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4407128433299-SAML-Integration-Strategies-Best-Practices
**Article ID:** 4407128433299

We recommend keeping this option checked. When enabled, if users are authenticated and SAML maps the user to a team or role that can use OptiSigns, the user will be created automatically.

If disabled, you will have to create each user first in OptiSigns before they can log in with SAML SSO.

![mceclip5.png](https://support.optisigns.com/hc/article_attachments/4407136156819)

Going back to our old example. Let's say there are 20 users belong to Marketing West Coast group in your IDP, and Marketing West Coast is mapped to the Marketing West Coast team in OptiSigns.

If a user in Marketing West Coast group logs in to OptiSigns, they will be automatically created and can immediately access West Coast Team screens and content.

The other 19 users are not created in OptiSigns until they attempt to log in.

You can also map **Unmapped users/groups** to **No Team (Disable)**. This way, if a user belongs to some other group in your IDP and tries to log in, they will get an error and the user is not created in OptiSigns.

This way you can keep the system clean and only users needing access to the app are replicated.

![mceclip6.png](https://support.optisigns.com/hc/article_attachments/4407136240659)

If you have any questions or need help with SAML integration please feel free to reach out to us at [support@optisigns.com](mailto:support@optisigns.com)
