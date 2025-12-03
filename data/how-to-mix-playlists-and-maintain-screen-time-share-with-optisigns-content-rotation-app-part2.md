# How to mix playlists and maintain screen time share with OptiSigns Content Rotation App
**Article URL:** https://support.optisigns.com/hc/en-us/articles/1500001561861-How-to-mix-playlists-and-maintain-screen-time-share-with-OptiSigns-Content-Rotation-App
**Article ID:** 1500001561861

  * Enforce each item duration limit: Force each asset's playing time is same as Each Item Duration time. When this is checked, you will need to select how you want to handle when an item's duration is less than "Each item duration": 
    * Move to next: If an item's duration is less than "Each item duration", it will move to next
    * Repeat: If an item's duration is less than "Each item duration", it will repeat the same asset until the "Each item duration" is over.



Click Save.  
After Saving, you can Preview the Content Rotation to see how the system mix the playlist.

## **That's all! Congratulation!**

You have added a Content Rotation app.

You can assign the newly created Content Rotation asset to your screen by going to Screens, click Edit screens and assign the asset to screens that you want.

**If you really curious about how the system mix the playlist, you can check out these cases:**

**Case 1** \- Enforce each item duration limit = checked + Repeat (This is the default case)   
Playlist A -> 5 items: Rotate A: 1 item - 20s  
A1: 10s  
A2: 20s  
A3: 15s  
A4: 10s  
A5: 50s

Playlist B -> 3 items, Rotate B: 1 item - 20s  
B1: 10s  
B2: 40s  
B3: 5s

Result:  
A1: 20s  
B1: 20s

A2: 20s  
B2: 20s

A3: 20s  
B3: 20s

A4: 20s  
B1: 20s

A5: 20s  
B2 20s

**Case 2** \- Enforce each item duration limit = checked + Move to next

Playlist A -> 5 items: Rotate A: 1 item - 20s

A1: 10s  
A2: 20s  
A3: 15s  
A4: 10s  
A5: 50s

Playlist B -> 3 items, Rotate B: 1 item - 20s

B1: 10s  
B2: 40s  
B3: 5s

Result:

A1: 10s  
B1: 10s

A2: 20s  
B2: 20s

A3: 15s  
B3: 5s

A4: 10s  
B1: 10s

A5: 20s  
B2 20s

**Case 3** \- Enforce each item duration limit = checked + Repeat

Playlist A -> 5 items: Rotate A: 2 item - 20s