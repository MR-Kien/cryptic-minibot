# How to Set Up SAML 2.0 with OptiSigns and MS Entra ID (formerly Azure AD)
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4407252213395-How-to-Set-Up-SAML-2-0-with-OptiSigns-and-MS-Entra-ID-formerly-Azure-AD
**Article ID:** 4407252213395

![groups with object id noted](https://support.optisigns.com/hc/article_attachments/37186635118611)

This Object ID should be input into the Group Name field within OptiSigns. However, we recommend creating a group specifically for OptiSigns with an OptiSigns- prefix and map these to OptiSigns like this:

  * optisigns-admins (SAML group) → OptiSigns role: Admin
  * optisigns-users (SAML group) → OptiSigns role: Users
  * optisigns-custom-role (SAML group) → OptiSigns custom role that you create



Once finished, it should resemble this:

![filled out group mapping optisigns](https://support.optisigns.com/hc/article_attachments/37186682886547)

You can create as many groups and roles as you like.

### How to Handle Unmapped Users and Groups

You may wish to map the “Unmapped users/groups” section to **No Team (Disable)**. This way, they will receive an error message when trying to login in and will have to reach out to Admins to get the correct team and role assigned. This is a useful safeguard in case certain users accidentally get assigned the OptiSigns app but not the correct group.

![unmapped users/groups with no team selected](https://support.optisigns.com/hc/article_attachments/37186635129363)

**NOTE:** If you map an SAML group to a Team, then delete the Team, it will result in new users being mapped to No Team. They will have to contact you to be assigned to a team in order to use the app.  
---  
  
### Managing Attributes & Claims in Microsoft Azure

Editing the Attributes & Claims in Microsoft Azure can give you even more control over the Users added to the group, and is a valuable tool.

To begin, go to the Azure portal. Click **Enterprise Applications** → **OptiSigns** → **Single sign-on**. Scroll down to Section 2: User Attributes & Claims. This is where you maintain the mapping of these attributes.

![user attributes and claims ms azure](https://support.optisigns.com/hc/article_attachments/37186682899603)

Within this section, there are two main things to customize:

  * Group Claims
  * User Attributes



We’ll walk you through each.

#### Creating Group Claims for Use with OptiSigns

To create a Group Claim, first hit **Add a group claim** :

![add group claim ms azure](https://support.optisigns.com/hc/article_attachments/37186682904595)

When you create a Group: