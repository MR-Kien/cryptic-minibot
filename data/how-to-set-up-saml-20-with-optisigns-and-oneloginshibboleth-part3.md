# How to set up SAML 2.0 with OptiSigns and OneLogin(Shibboleth)
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4407476403859-How-to-set-up-SAML-2-0-with-OptiSigns-and-OneLogin-Shibboleth
**Article ID:** 4407476403859

Scroll to Advanced Settings and create a mapping.  
Group Name (roles assigned to the user from OneLogin), Role (role in OptiSigns) mapping.   
![mceclip9.png](https://support.optisigns.com/hc/article_attachments/21286528943635)

It's best practice to create a group specifically for OptiSigns with name prefix with optisigns- and map to OptiSigns like below:

  * optisigns-admins (SAML group) -> OptiSigns role: Admin
  * optisigns-users (SAML group) -> OptiSigns role: Users
  * optisigns-custom-role (SAML group) -> OptiSigns custom role that you create



**How to handle Unmapped users/groups:**

You can map the "Unmapped users/group" to No Team (Disabled)

This way they will receive an error when trying to log in and will have to reach out to Admins to get correct teams, and roles assigned. This can be used as a safeguard, in case some users accidentally got assigned OptiSigns app but not the right groups.

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/26504504778259)

Note that if you map a SAML group to a Team and then delete the team, it will result in the new user being mapped to No Team and will have to contact you to be assigned to a team to use the app.

Next, go to your OneLogin portal. Go to the parameters page of the OptiSigns application. This is where you maintain the mapping of the attributes.

Create new custom parameters here by clicking the + icon. Currently, OptiSigns support attributes mapping of first name, last name, and group. You can set the customer parameter name to the same default attribute name used on OptiSigns, and then assign it to the corresponding values from OneLogin.

Shibboleth has many predefined standard attributes. In this case, the givenName can be mapped to firstName on OptiSigns, and the surname can be mapped to lastName on OptiSigns.

These mappings will pass information to OptiSigns on the user's Name and Group.

![mceclip4.png](https://support.optisigns.com/hc/article_attachments/4407468380563)

The parameter names are corresponding to OptiSigns

<https://app.optisigns.com/app/s/saml-settings>

OptiSigns accept firstName, lastName, and group by default. Instead of setting the parameter names to the default attribute name used on OptiSigns, you can also change the attribute name on OptiSigns to match the parameter names you defined on OneLogin as well. 

Shibboleth uses standard namespace and id for the predefined standard attributes. In the case of names, the id should be used in the attributes mapping on OptiSigns.