# How to Set Up SAML 2.0 with OptiSigns and MS Entra ID (formerly Azure AD)
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4407252213395-How-to-Set-Up-SAML-2-0-with-OptiSigns-and-MS-Entra-ID-formerly-Azure-AD
**Article ID:** 4407252213395

  1. Select **Groups assigned to the application** under “Which groups associated with the user should be returned in the claim?”
  2. (Optional) Input the name “groups” in the “Customize the name of the group claim” and leave the Namespace section blank.



![group claim settings ms azure](https://support.optisigns.com/hc/article_attachments/37186635155987)  
That’s all for creating Group claims.

#### Customizing User Claims for Use with OptiSigns

These mappings will pass information to OptiSigns on the user’s Name and Group:

![managing user claims ms azure](https://support.optisigns.com/hc/article_attachments/37186635162003)

The Claim names are, by default, represented by a URL. The Type will be given as SAML, with the Value corresponding to identifying information about the user, including:

  * user.givenname
  * user.groups (only if setup - see above section)
  * user.mail
  * user.userprincipalname
  * user.surname



These Claim names correspond to this section under **Advanced Settings** on the SAML SSO Settings page:

![advanced settings optisigns saml sso settings page](https://support.optisigns.com/hc/article_attachments/37186635168659)

OptiSigns accepts First Names, Last Names, and Groups by default.

These values correspond to the **Namespace** of the claim. So, in other words, if the Value corresponding to the firstName (user.givenname) is a URL, you will have to paste the entire URL into OptiSigns. It is possible, however, to change the Namespace to something more manageable.

In Azure, click on any of these claims to Manage them.

![ms azure manage claims](https://support.optisigns.com/hc/article_attachments/37186635174931)

To eliminate the URL, simply delete it from the Namespace field, then hit **Save**.

![eliminate URL ms azure claim](https://support.optisigns.com/hc/article_attachments/37186635182483)

This will replace the URL in the Namespace with the Name. This is a much easier piece of information to manage.

![claims after removing url ms azure](https://support.optisigns.com/hc/article_attachments/37186635189523)

These can now be mapped, like so:

![proper user mapping in optisigns example](https://support.optisigns.com/hc/article_attachments/37186635199123)

Finally, go to the **Users and groups** section within Azure and assign your groups to the OptiSigns Enterprise app.

![add user/group](https://support.optisigns.com/hc/article_attachments/37186682960019)

* * *

## Setting Up OptiSigns Login to Appear in Office.com