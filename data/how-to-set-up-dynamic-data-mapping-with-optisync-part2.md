# How to Set Up Dynamic Data Mapping with OptiSync
**Article URL:** https://support.optisigns.com/hc/en-us/articles/29217646663187-How-to-Set-Up-Dynamic-Data-Mapping-with-OptiSync
**Article ID:** 29217646663187

  * [How to add Google Sheets as a DataSource for OptiSync](https://support.optisigns.com/hc/en-us/articles/29838866920211)
  * [How to add a Microsoft 365 Excel Spreadsheet as a DataSource for OptiSync](https://support.optisigns.com/hc/en-us/articles/29863080711059)



In addition, you can integrate and test API requests, and execute any necessary pre- or post-request coding.

![](https://support.optisigns.com/hc/article_attachments/29217646654099)

Once your data source is set up, you can see **Where Used,****Edit** the data source, and/or **Duplicate** it.

![](https://support.optisigns.com/hc/article_attachments/29689445946003)

  * **Where Used: **This will show you which of your designs are using this Data Source. This is useful to track the use of this data source across different assets.
  * **Edit Data: **Go into your data source and make any updates/changes.
  * **Duplicate: **This will create a copy of your data source.



![](https://support.optisigns.com/hc/article_attachments/29689413996947)

## Inputting Your Data Source in Designer

Once your Data Source is set up, you can connect it to the Designer app.

Go to **DataSource** on the left side of the Side Menu.

![datasource location designer](https://support.optisigns.com/hc/article_attachments/42703178733715)

As previously mentioned, you can add your DataSource here. Or, if you have already created it in the Data Source section of **Advanced** , then it should show up under **Other DataSources**.

**Select** your data source.

**Drag and drop** the data source elements onto the Designer canvas. 

  * You can either drag and drop an entire Row or the individual aspects within the rows. 



A pop-up message will appear, asking "**Would you like to use this data in a Repeater or on its Own?** "

![on its own vs repeater gif](https://support.optisigns.com/hc/article_attachments/42703178736787)

  * **Use on its own:** It will be an element on its own and will update automatically based on the data source.

  * **Use in a Repeater:** This will include the data source element in a Repeater component. 
    * **Repeater** is a tool that can be used on the Designer application to display and repeat a list of items dynamically.

**IMPORTANT**  
---  
OptiSync does not support special characters (i.e. anything outside the scope of an English-language keyboard). This will cause the system data to read as blank, and it will not show.  
  
## Editing and Designing Your Repeater in Designer