# User Management Example - Chain Restaurant or Retail Store with Multiple Locations
**Article URL:** https://support.optisigns.com/hc/en-us/articles/43657735780627-User-Management-Example-Chain-Restaurant-or-Retail-Store-with-Multiple-Locations
**Article ID:** 43657735780627

In this example, we’ll be using a centrally managed system, but with some degree of local control. We want:

  * Organization of screens to mirror our corporate structure
  * End users to be able to manage their own screens and upload their own content
  * To provide content for all our end users that they are required to display (i.e. large scale promotions, brand identity displays, etc.).
    * For this, we’ll assume several layers of management. For example, you may have national, regional, or local promotions. You might not want a promotion targeting Boston to appear in Dallas, for instance.
  * To enforce brand guidelines



With our needs identified, we can begin.

* * *

## Folder and Screen Organization

How you choose to organize your screens will depend on your needs, but there are many ways it can be done.

In our example, we will focus on location. This is the single most common way we have seen our customers set up OptiSigns. That said, you can organize however works best to you.

For our hypothetical chain restaurant or retail store, we will create an internal folder structure to mirror the corporate organizational structure. So, in this case, that is **Region → State → City/Sub-region → Store Location/Number.** We’ll create nested sub-folders corresponding to these values. When set up, it will look something like this:

#### **Top Level:**

**![top level folders for default team](https://support.optisigns.com/hc/article_attachments/43657735752211)**

#### **Screen Level:**

![screen level display showing nesting](https://support.optisigns.com/hc/article_attachments/43658114517651)

Note the level of nesting we’ve set up. The reason for this? Each of these folders can be granted different levels of permissions. We’ll set that up soon.

For the rest of this example, we’ll be focusing on a single store: the **Cosmos Space Center** , with the following nesting:

  * **Pacific -** Region
    * **California -** State
      * **Los Angeles** \- City/Sub-region
        * **Cosmos Space Center** \- Store Location
          * Screens at this location will be placed in this folder.



We want to ensure only the proper users can access the screens and content for this location. We also want to make sure that any local, state, or regional managers can provide content as needed.

* * *

## Creating Teams