# How to set up SAML 2.0  with OptiSigns and Okta
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4404590815635-How-to-set-up-SAML-2-0-with-OptiSigns-and-Okta
**Article ID:** 4404590815635

To configure how OptiSigns should map the user groups to OptiSigns Roles by going to: <https://app.optisigns.com/app/s/saml-settings>

Scroll to Advanced Settings and create a mapping.  
Group Name (group names in Okta), Role (role in OptiSigns) mapping.   
![mceclip1.png](https://support.optisigns.com/hc/article_attachments/4404820186003)

It's best practice to create a group name prefix with Optisigns- and map to OptiSigns like below:

  * optisigns-admins (SAML group) -> OptiSigns role: Admin
  * optisigns-users (SAML group) -> OptiSigns role: Users
  * optisigns-custom-role (SAML group) -> OptiSigns custom role that you create



**How to handle Unmapped users/groups:**

You can map the "Unmapped users/group" to No Team (Disabled)

This way they will receive an error when trying to log in and will have to reach out to Admins to get the correct teams, and roles assigned. This can be used as a safeguard, in case some users accidentally got assigned OptiSigns app but not the right groups.

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/4404812977171)

Note that if you map a SAML group to a Team and then delete the team, it will result in new user being mapped to No Team and will have to contact you to be assigned to a team to use the app.

Next, go to your Okta Admin portal. Click Applications -> OptiSigns.

![mceclip11.png](https://support.optisigns.com/hc/article_attachments/4404615820691)

Click Assign -> People or Groups to use this app. You can also configure your user to request to use the app, but that's beyond the scope of this article.

![mceclip12.png](https://support.optisigns.com/hc/article_attachments/4404615832339)

You can set up group mapping by going to General -> SAML settings

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/4404762241811)

Click Next:

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/4404767623827)

Creating these mappings will pass information to OptiSigns on the user's Name and Groups.

![mceclip4.png](https://support.optisigns.com/hc/article_attachments/4404762334611)

The "Attribute Statement" and "Group Attribute Statement" are corresponding to OptiSigns <https://app.optisigns.com/app/s/saml-settings>