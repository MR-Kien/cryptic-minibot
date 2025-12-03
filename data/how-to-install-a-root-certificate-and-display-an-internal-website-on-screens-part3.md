# How to Install a Root Certificate and Display an Internal Website on Screens
**Article URL:** https://support.optisigns.com/hc/en-us/articles/35184720136595-How-to-Install-a-Root-Certificate-and-Display-an-Internal-Website-on-Screens
**Article ID:** 35184720136595

  1. Open the Microsoft Management Console (MMC)
  2. Add the Certificates Snap-In
  3. Import the Certificate
  4. Verify the Installation



These same steps can be performed quickly using the Windows Terminal, if you’re so inclined.

Be cautious when installing root certificates, especially self-signed ones. Only install certificates from sources you trust completely.

**NOTE**  
---  
You need administrator privileges to install certificates in the Trusted Root Certification Authorities store.  
  
### Open the Microsoft Management Console (MMC)

The first step is opening the Microsoft Management Console (MMC), which is a framework for managing Windows components.

To do this, click **Start,** type **mmc** into the Search bar, then press **Enter**.

![](https://support.optisigns.com/hc/article_attachments/35184705345939)

### Add the Certificates Snap-In

With the MMC open, go to **File → Add/Remove Snap-In**.

![](https://support.optisigns.com/hc/article_attachments/35184705348371)

In the “Available snap-ins” list, select **Certificates** and click **Add.**

![](https://support.optisigns.com/hc/article_attachments/35184720078227)

Choose **Computer account** to manage certificates for the local computer. Click **Next**.

![](https://support.optisigns.com/hc/article_attachments/35184705352851)

Next, click **Local computer** and click **Finish**.

![](https://support.optisigns.com/hc/article_attachments/35184705355155)

Click **OK** to close the “Add or Remove Snap-ins” dialog.

### Import the Certificate

Now **Certificates (Local Computer)** will appear as an option in your MMC. To continue, exp[and the **Certificates (Local Computer)** option within the right pane of the console. Then, expand **Trusted Root Certification Authorities**.

![](https://support.optisigns.com/hc/article_attachments/35184720086931)

Right-click on the **Certificates** folder and select **All Tasks → Import**.

**![](https://support.optisigns.com/hc/article_attachments/35184720091795)**

This will open the Certificate Import Wizard. Click **Next** to get started.

Now, click **Browse.** Locate your self-signed certificate and select it. This should be a .pem file. You may need to expand the file name options to **All Files** to see it.

![](https://support.optisigns.com/hc/article_attachments/35184705362323)

Select the file and click **Open → Next.**

Select **Place all certificates in the following store.** Ensure that **Trusted Root Certification Authorities** is selected, then click **Next.**