# Using RS-232 to Schedule TV Power On/Off or other commands
**Article URL:** https://support.optisigns.com/hc/en-us/articles/9061950942995-Using-RS-232-to-Schedule-TV-Power-On-Off-or-other-commands
**Article ID:** 9061950942995

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/9062308259731)

**2\. Configure RS-232 command and set up the template**

Go to the "Commands" tab, and click the "Add New" button.

![chrome_kVTicFpYv5.png](https://support.optisigns.com/hc/article_attachments/32323154954003)

Set the RS-232 command of your commercial display in the pop-up window. You can choose "asc ii" or "hex" encoding depending on your TV, and the end of line value can be set here accordingly as well. 

You will need to create a command for Power On, and a command for Power Off.

![chrome_QGt8AmZbeI.png](https://support.optisigns.com/hc/article_attachments/32323291436947)

Once commands are created, go to the "Templates" tab, this is where you map the commands to the Power On/Off action. You only need to create a template if the commands are different. For example, if you are only using Samsung commercial TVs, which all have the same commands for power on/off, then you only need to create one template for it, it can be used on all the Samsung TVs you have deployed. 

![chrome_0RqFJkgyu4.png](https://support.optisigns.com/hc/article_attachments/32323151390739)

Map the command to the actions. The actions will be used in the advanced schedule. Save it after the mapping is complete, then the template is ready for use.

![mceclip7.png](https://support.optisigns.com/hc/article_attachments/9062485175059)

**3\. Set up Power On/Off schedule**

Once the RS-232 configuration is complete, you will need to set up an Operational Schedule.

Go to the Edit Screens, then go to the **Operational Schedule** section. Hit **New**.

![](https://support.optisigns.com/hc/article_attachments/40414890419859)

You'll see the Operational Schedule screen. Here, click anywhere you'd like to schedule a Power On/Off.

![](https://support.optisigns.com/hc/article_attachments/40414890422803)

Once you've done this, you'll see this menu pop up on the side:

![](https://support.optisigns.com/hc/article_attachments/40414884380947)

Here, the relevant piece is **Power**. Clicking this will show a drop-down:

![](https://support.optisigns.com/hc/article_attachments/40414890424723)

To power your screen on or off using RS-232, there are two relevant options: