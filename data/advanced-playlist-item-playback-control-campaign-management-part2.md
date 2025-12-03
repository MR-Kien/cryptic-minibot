# Advanced Playlist Item Playback Control & Campaign Management
**Article URL:** https://support.optisigns.com/hc/en-us/articles/22474034993043-Advanced-Playlist-Item-Playback-Control-Campaign-Management
**Article ID:** 22474034993043

  * Rotate X items: This defines how many items will be played each round in the sub-playlist. For example, if you set 2 here, whenever it comes to this sub-playlist, it will play 2 items. When all items are played, it will start over.
  * Max duration per item: This provides a way to better control the time of the playback to avoid anomalies. For example, if you set the value to 120 seconds, any item in the sub-playlist cannot play more than 2 minutes, even if a long video is accidentally placed in the sub-playlist, it will be cut when it reaches 2 minutes. 



![](https://support.optisigns.com/hc/article_attachments/22476049744019)

**NOTE**  
---  
Enabling "Sync Play" on your Master Playlist will ignore Sub-playlist control.  
  
#### **2) How to use resume on the next play**

Using a resume on the next play is simple. Just open the playlist options and get it enabled, then the playlist will always resume from where it left off last time and start playback from that point. This can resume from the middle of the video files as well. For example, if there is a 5-minute video in the playlist, you set the duration to 1 minute in the playlist, if this setting is enabled, the next time when it loops back to the video, it will play the next 1 minute instead of starting from the beginning each time. 

![](https://support.optisigns.com/hc/article_attachments/22476080162067)![](https://support.optisigns.com/hc/article_attachments/22476080164755)

#### **3) How to use split-screen primary zone with playlist**

Using the primary zone in split-screen can help you get more smoother transition when the split-screen is used inside the playlist. A common use is to create a split-screen to organize similar contents together.

For instance, the main zone may play a work safety video, and you want the side zone to show some safety-related messages as well. 

When there are many split-screen assets inside a playlist, you would like it to transition to the next item when the primary zone's playlist item is complete rather than follow the duration setting of the split-screen asset. This is a great way to avoid videos being cut off early.

To use the primary zone setting, just open the configs popup of the split-screen asset, and then you can select which zone will be the primary zone. Once the primary zone is selected, 2 settings can help you to control it. 

  * Select zones that use primary zone timing: This will help match the duration of the contents from the selected zones to the Primary Zone.  