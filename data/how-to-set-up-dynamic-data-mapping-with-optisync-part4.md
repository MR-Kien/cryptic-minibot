# How to Set Up Dynamic Data Mapping with OptiSync
**Article URL:** https://support.optisigns.com/hc/en-us/articles/29217646663187-How-to-Set-Up-Dynamic-Data-Mapping-with-OptiSync
**Article ID:** 29217646663187

  * **Replace DataSource:** Change your DataSource
  * **Manage:** Make changes to your DataSource's information.
  * **Filter:** Apply condition based filters on the DataSource. Filter conditions can be applied using fixed value or device attributes.
  * **Disconnect:** Disconnect your DataSource from the Repeater
  * **Empty Data Handling:** When there is no DataSource element, the default behavior is to use a blank value. You can adjust this with the following options: 
    * **Skip:** Skip it, or get rid of additional repeater items if there isn't enough data to reach the set "Total Items displayed per Page".
    * **Use Default Value:** Show default content, which is what your Repeater element looks like by itself.
    * **Use Blank:** The Repeater will show nothing.
  * **Spacing Betwee****n****Items: **Increase or decrease the space between the Repeater items.
  * **Item Display Direction:** Change the positioning of the rows from your DataSource within the Repeater items.   

    * **Left To Right** : It will display the rows going from left to right.
    * **Top To Bottom** : It will display the rows going top to bottom.
  * **Item Display Alignment:** Change the alignment of the remaining element items (less than the configured items) to be aligned left/center/right or top/center/bottom. 
  * **Total Items Displayed per Page:** Increase or decrease how many Repeater items you'd like to be shown.
  * **Maximum Items in Each Row/Column:** Increase or decrease how many Repeater items you'd like shown in each row/column.
  * **Additional Row/Column Spacing:** Increase or decrease the spacing between rows/columns.
  * **Duration (seconds):** Adjust the duration of time for how long each Repeater item is shown before.
  * **Shuffle:** Randomly shuffle the items in your DataSource to be displayed on the Repeater.



If you edit a Repeater, it will replicate your updates for each instance of data in the dataset.

  * This allows for a consistent look across similar elements without the need to design each one individually.



If you want to use a specific Repeater Template or Component, and would like to update the sample DataSource to one of your DataSources, please follow the steps shown below:

### How to use the Property Mapping Feature

This advanced feature allows you to change the appearance of specific data in your repeater based on conditions set by the user. These conditions, defined in the data source, are mapped to the corresponding values or elements in the repeater, and the specified formatting is then applied.

![](https://support.optisigns.com/hc/article_attachments/42705284279187)