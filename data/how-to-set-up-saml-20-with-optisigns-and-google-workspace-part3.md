# How to set up SAML 2.0 with OptiSigns and Google Workspace
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4407493404307-How-to-set-up-SAML-2-0-with-OptiSigns-and-Google-Workspace
**Article ID:** 4407493404307

Scroll to Advanced Settings and create a mapping.  
Group Name (can use department from Google Workspace), Role (role in OptiSigns) mapping.   
![mceclip8.png](https://support.optisigns.com/hc/article_attachments/4407485832851)

It's best practice to create a group specifically for OptiSigns with name prefix with optisigns- and map to OptiSigns like below:

  * optisigns-admins (SAML group) -> OptiSigns role: Admin
  * optisigns-users (SAML group) -> OptiSigns role: Users
  * optisigns-custom-role (SAML group) -> OptiSigns custom role that you create



**How to handle Unmapped users/groups:**

You can map the "Unmapped users/group" to No Team (Disabled)

This way they will receive an error when trying to log in and will have to reach out to Admins to get correct teams, and roles assigned. This can be used as a safe guard, in case some users accidentally got assigned OptiSigns app but not the right groups.

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/21287201539475)

Note that if you map a SAML group to a Team and then delete the team, it will result in new user being mapped to No Team and will have to contact you to be assigned to a team to use the app.

Next, it is time to talk about the attributes mapping. This is the last step when creating the app in Google Workspace.

Currently, OptiSigns support attributes mapping of first name, last name and group. You can define the attribute name in Google Workspace and set it to the same default attributes name used on OptiSigns.

These mappings will pass information to OptiSigns on what's user's Name and Groups.

![mceclip5.png](https://support.optisigns.com/hc/article_attachments/4407485726611)

The "App attributes" are corresponding to OptiSigns

<https://app.optisigns.com/app/s/saml-settings>

OptiSigns accept firstName, lastName, and group by default. Instead of setting the attribute names to the default attribute name used on OptiSigns, you can also change the attribute name on OptiSigns to match the attribute name you defined on Google Workspace as well.

![mceclip9.png](https://support.optisigns.com/hc/article_attachments/4407485875347)

#### **I've made it into my OptiSigns account, but don't seem to have all the side menu options I'm used to. What’s going on?**

It's likely you've signed on through your Branded Portal, using a URL similar to this one:
    
    
    https://app.optisigns.com/signIn/<accountId>