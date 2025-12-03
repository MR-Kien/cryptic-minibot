# How to approve OptiSigns as Enterprise App on Microsoft Azure (for PowerBI, Calendar, etc. access)
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4403616315539-How-to-approve-OptiSigns-as-Enterprise-App-on-Microsoft-Azure-for-PowerBI-Calendar-etc-access
**Article ID:** 4403616315539

Review the permissions requested by OptiSigns. OptiSigns, as a digital signage application, only reads and displays assets. It will not modify, move, or delete objects. See our [Privacy Policy](https://www.optisigns.com/privacy-policy) for more information.

Click **Accept:**

![mceclip7.png](https://support.optisigns.com/hc/article_attachments/4403627456531)

**That's all!** You have reviewed and approve OptiSigns to be used as Enterprise App in your organization.

You can notify your users who made the request that they can start using the requested app (Power BI, OneDrive, or Calendar) with OptiSigns now.

If users want to use more than 1 app (i.e. Power BI and OneDrive, then you will need to approve more than 1 time).

### Why does using Office 365, PowerBI, or other Microsoft App require giving OptiSigns Admin permission to use?

OptiSigns uses Microsoft APIs for integration. In order for our integrations to work, the integration has to be approved by an administrator to be allowed in the Azure tenant. This is the same across all integrations using Microsoft APIs.

This administrator access is only needed for first time access. Once the OptiSigns app is approved for use in the Azure tenant, other users can use OptiSigns directly.

**References:**

[Configure the admin consent workflow - Azure Active Directory | Microsoft Docs](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/configure-admin-consent-workflow)

[Quickstart: Configure properties for an application in your Azure Active Directory (Azure AD) tenant | Microsoft Docs](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/add-application-portal-configure)

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
