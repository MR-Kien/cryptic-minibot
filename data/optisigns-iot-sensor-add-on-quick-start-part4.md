# OptiSigns IoT Sensor Add-on - Quick Start
**Article URL:** https://support.optisigns.com/hc/en-us/articles/13097501958291-OptiSigns-IoT-Sensor-Add-on-Quick-Start
**Article ID:** 13097501958291

  *     * **Play Content:** Determines what content plays (or stops) when trigger conditions are met. Options are "Asset," "Playlist," or "Stop Playing."
    * **Commands:** Allows you to send out commands to sensors instead of just receiving them. If you're using a typical IoT sensor, **you most likely won't need to use this**. These are typically used for other types of devices, such as atmospheric lighting or speakers. These commands are created in the "Commands" section of the "External Communications (RS232)" section from before. We will be returning to this later in the article.
    * **Action:** Allows you to move a Rule's place in the list, or delete them.
  * **Add Rule:** Allows the creation of more rules, with no maximum. These can be deleted or organized via the Action setting.



We  _**strongly recommend**_ obtaining a string command and inputting it into the **Play Rules** section. This will reduce or eliminate any potential issues.

To do this, boot up your screen and navigate to the OptiSigns main menu. Scroll down until you see **Trigger Event Viewer**.

![firefox_VujXdIW6kJ\(1\).jpg](https://support.optisigns.com/hc/article_attachments/42985157371027)

When your sensor is properly configured, you will be able to see it mapped to a COM port. This information can be By placing pressure on the sensor, a **string** will appear on the right side of your screen. By typing this **case-sensitive** string into your **If Detected** area, your issues will likely resolve.

![firefox_ISUylb5Aq5.png](https://support.optisigns.com/hc/article_attachments/32208926880915)

This is the easiest way to get these command strings for non-Nexmosphere brand sensors. You can also find these command strings by looking at your manufacturer's website.

  
Once you've got everything set up to your liking, hit **Assign** to move to the next step.

* * *

## **3\. Assign the IoT Sensor Add-on app to a Screen**

There are two options for assigning your Sensor Add-On to a screen.

### Option 1: Through Lift and Learn

![firefox_vDbwOLdUam.png](https://support.optisigns.com/hc/article_attachments/32208926865683)

Once you've created the parameters for your IoT sensor, you can assign it directly to one of your screens. There are two options:

  * **Target -** Select between Screens and Tags. Selecting one or the other will change the next option to either Screens or Tags, depending on which you select here.
  * **Screens / Tags** \- Select which screen or tag will be associated with the sensor. This determines where your content will appear.

