# Advanced: Custom Domain mapping
**Article URL:** https://support.optisigns.com/hc/en-us/articles/1500000480302-Advanced-Custom-Domain-mapping
**Article ID:** 1500000480302

With OptiSigns Pro and Enterprise plan, you can enhance your branding by mapping your custom domain for OptiSigns Management Portal.

For example: you can map your sub-domain: **login.abcmedia.com** so that your users can log in and use the portal from **login.abcmedia.com** and use the app like the screenshot below.

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/1500000517302)

#### **Let's jump in and get started!**

**1) Activate your OptiSigns sub-domain (in this example: abcmedia.optisigns.net):**

Go to the Branding page of your Account Management Settings:

<https://app.optisigns.com/app/s/branding-settings>

Type in your desired sub-domain for optisigns.net. In this case, we type in "abcmedia".  
Don't worry about optisigns.net, you will map your domain in the next step.

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/360099399934)

**2) Map CNAME alias for your domain/sub-domain:**

In your Domain DNS management, map your desired domain/sub-domain to your OptiSigns sub-domain using CNAME Alias.  
In this example, we map: login.abcmedia.com -> abcmedia.optisigns.net

Refer to your domain host documentation for more specific details.

Here are the generic steps:

  1. Go to your domain’s DNS records.
  2. Add a record to your DNS settings, selecting **CNAME** as the record type.
  3. Return to the first window or tab and copy the contents of the **Label/Host** field.
  4. Paste the copied contents into the **Label** or **Host** field with your DNS records.
  5. Return to the first window or tab and copy the contents of the **Destination/Target** field.
  6. Paste the copied contents into the **Destination** or **Target** field with your DNS records. 

Your record should look similar to one of the tables below:

**CNAME Record**

Record type | Label/Host field | Time To Live (TTL) | Destination/Target field  
---|---|---|---  
CNAME | login | 3600 or leave the default | abcmedia.optisigns.net  
  7. Save your record.  
CNAME record changes can take up to 72 hours to go into effect, but typically they happen much sooner.



Here are links to documentation from some popular domain hosts: