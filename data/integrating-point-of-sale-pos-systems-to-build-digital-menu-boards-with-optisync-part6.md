# Integrating Point-of-Sale (POS) Systems to Build Digital Menu Boards with OptiSync
**Article URL:** https://support.optisigns.com/hc/en-us/articles/31860170199955-Integrating-Point-of-Sale-POS-Systems-to-Build-Digital-Menu-Boards-with-OptiSync
**Article ID:** 31860170199955

**![](https://support.optisigns.com/hc/article_attachments/32077278901139)**

Click **Advanced Options →** **"Display Format"** and choose **"Number,"** then click **"Number Format"** and select the formatting you'd like. This will allow you to add dollar signs to your prices, with other options.

![ShareX_q0ybaobi0E.png](https://support.optisigns.com/hc/article_attachments/32060268867859)

Make sure to hit **Update** to make your new number format display.

![mraS5gfp1n.png](https://support.optisigns.com/hc/article_attachments/32060273056019)

The value of a repeater is that it will copy the format of this one cell, then replace the data points with others from your API. Done correctly, your menu should look something like this:

![](https://support.optisigns.com/hc/article_attachments/32077278906643)

The Repeater will pull as many data points as you have set up on your API. In this example, we've made a menu with 9 items, but with proper design you can put as many items as you'd like, with dynamic descriptions as well. If you have more items than what you've set to show on your screen at any one time, the items on the menu will rotate through them until they have all displayed.

#### Creating Strike Throughs and Sold Out Warnings

In the above example, we show a Sold Out warning. However, we don't want to display that all the time - only when the item isn't available. With OptiSync, this can be accomplished thanks to the Post-request processing we did earlier. Our code created this **"soldout: 0"** data. This is tied to our **"available"** data:

![](https://support.optisigns.com/hc/article_attachments/32077278913043)

When the "available" data reads "true," the "soldout" data reads 0. When your POS system detects items are unavailable, the "available" data will read "false". This will make the "soldout" data read 1.

We can use this knowledge to set up our Sold Out warnings and strike throughs to only appear when items are not available.

Going back to our Repeater Editor, we can click on a piece of text we want to strike through and hit **Settings** :

![](https://support.optisigns.com/hc/article_attachments/32077293399315)

In the Settings tab, hit **Advanced Options**.

![](https://support.optisigns.com/hc/article_attachments/32077801189779)

Under Advanced Options, hit **Property Mapping**.

![](https://support.optisigns.com/hc/article_attachments/31968071408915)