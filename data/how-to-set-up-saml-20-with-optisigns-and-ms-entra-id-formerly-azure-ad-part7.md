# How to Set Up SAML 2.0 with OptiSigns and MS Entra ID (formerly Azure AD)
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4407252213395-How-to-Set-Up-SAML-2-0-with-OptiSigns-and-MS-Entra-ID-formerly-Azure-AD
**Article ID:** 4407252213395

#### **It’s Saying I Don’t Belong to a Team/Group. How Can I Fix This?**

This error has to do with group mapping. To start, follow all the steps outlined in the “Assign and Map Users and Groups” section above.

![team/group error message](https://support.optisigns.com/hc/article_attachments/37188678189203)

If you’re still having trouble, check your Group names. In Azure, that’s Object ID:

![ms azure groups tab object id](https://support.optisigns.com/hc/article_attachments/37186635239699)

Check the desired User’s Attributes & Claims and make sure their Group name is assigned as **Groups assigned to the application**.

**![group claims error fix](https://support.optisigns.com/hc/article_attachments/37186635254803)**

Next, check if the Claim has been set up properly:

![proper claims names ms azure](https://support.optisigns.com/hc/article_attachments/37186683011731)

The above values should match these within the OptiSigns portal:

![proper claims names optisigns](https://support.optisigns.com/hc/article_attachments/37186683017875)

Finally, make sure the user and group have been added to the application within MS Azure:

![user and group added to app within ms azure](https://support.optisigns.com/hc/article_attachments/37186635286419)

This should resolve the issue.

#### **I've made it into my OptiSigns account, but don't seem to have all the side menu options I'm used to. What’s going on?**

It's likely you've signed on through your Branded Portal, using a URL similar to this one:
    
    
    https://app.optisigns.com/signIn/<accountId>

Go ahead and follow the steps outlined **here** and this issue should resolve itself.

### **That's all!**

You have configured SAML 2.0 for OptiSigns with Microsoft Entra.

You can share the URL with your users and they can log in with their SSO credentials.

If you have any additional questions or any feedback about OptiSigns, feel free to reach out to our support team at support@optisigns.com
