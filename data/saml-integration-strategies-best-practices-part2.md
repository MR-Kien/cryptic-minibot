# SAML Integration Strategies & Best Practices
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4407128433299-SAML-Integration-Strategies-Best-Practices
**Article ID:** 4407128433299

With this approach you will map all users to groups in your IDP, and map the IDP groups to OptiSigns teams/roles. When there's a change in IDP (for example, a user is added or changes groups), it will automatically reflect in OptiSigns. 

To implement this, check **Enable User Override**. When checked, every time a user logs in using SAML, OptiSigns will check to see if their name or group assignment has changed. It will then enforce that accordingly. If their name or assignment has updated, it will also update OptiSigns.

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/4407135779603)

Map all your appropriate groups to roles & teams in OptiSigns.

For example we have 3 groups:

  * Marketing West Coast - users responsible for managing screens, content for West region
  * Marketing East Coast - user responsible for manage screens, content for East region
  * IT Support - Admin that can support both region and do other admin tasks



The mapping should be like below.

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/4407128634643)

With this set up, let's say a user belongs to Marketing West Coast. You want to move them to Marketing East Coast. Simply update your IDP and move them from West Coast to East Coast. The next time they log in to OptiSigns, that will be reflected and they will belong to the Marketing West Coast team and can only see that content in OptiSigns.

For more on User Management, see our article on **[Teams and Folder Security](https://support.optisigns.com/hc/en-us/articles/43657735780627-User-Management-Example-Chain-Restaurant-or-Retail-Store-with-Multiple-Locations) **in OptiSigns.

#### **2) As Authentication Service Only**

SAML can be used to enforce your MFA, Password policy, and remove users and revoke access to OptiSigns. You can still manage these users and assign them to Teams or Roles. This approach is quick to set up and flexible as you can quickly move users around in OptiSigns. However, when users move around in your IDP, you will have to remember to move them around in OptiSigns as well, if required.

To implement this, uncheck **Enable User Override.**

![mceclip4.png](https://support.optisigns.com/hc/article_attachments/4407136124435)

Going back to our earlier example: when a user moves from Marketing West Coast to Marketing East Coast, you will need to go to OptiSigns and move the user's team assignment, if necessary.

Also if when the user update, change their name, you will have to update OptiSigns as well to keep it in sync.

#### **Enable User Creation:**