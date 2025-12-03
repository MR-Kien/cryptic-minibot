# How to set up Monitoring Alert feature 
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4403306341523-How-to-set-up-Monitoring-Alert-feature
**Article ID:** 4403306341523

  * Alert Policy Name: This is just a name to show in the list of policies since you can create more than one.
  * Alert Rule: how often do you want monitoring rules to run? Our suggestion is 60 minutes. While OptiSigns support monitoring at 15-minute intervals, 60min may help you avoid some false positives due to temporary network, or power issues
  * Send Reminder: how often do you want OptiSigns to send reminders when screens are down? Our suggestion is to send reminders once a day. While OptiSigns support sending reminders every hour, this may just clutter up your inbox if you are not going to take action on the screen within 1h of getting a notification.
  * Select Screens or Tags: select which group of screens you want to monitor, not all screens may be equally important to you. You can select group specifics screens or group of tags. In this example we select all screens tags as [Location-1] and [customer-facing]
  * Send alert to: list of email address alerts to be sent to
  * Time zone: which time zone you want to follow. In alert email will reference as of time, if device is in New York (EST), and you are in Houston (CST), the down time will be convert to Houston (CST) time. This is necessary and useful especially if you manage many devices across time zones.
  * Active: you can turn the rule on/off. Sometimes you may want to turn it off temporarily if you are doing changes like building renovation or network upgrade that you know devices will not be on, so you don't receive too many alerts.



**Here's an example of alert email:**

![mceclip4.png](https://support.optisigns.com/hc/article_attachments/4403306337299)

You can click "Manage Alert Rules" to go to manage alert rule pages and update your rules if needed.

#### **That's it!**

You have created Monitoring Alert rule to help you get notifications when your screens are down, so you can take actions.

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
