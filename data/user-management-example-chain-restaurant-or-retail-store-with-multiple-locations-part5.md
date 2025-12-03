# User Management Example - Chain Restaurant or Retail Store with Multiple Locations
**Article URL:** https://support.optisigns.com/hc/en-us/articles/43657735780627-User-Management-Example-Chain-Restaurant-or-Retail-Store-with-Multiple-Locations
**Article ID:** 43657735780627

![how to change security permissions](https://support.optisigns.com/hc/article_attachments/43657783485715)

Now only the Pacific Region Team and the Default Team will have access to this folder. You can also choose whether to make this Folder and its subfolders Editable or View-only:

![edit and view permissions for folder](https://support.optisigns.com/hc/article_attachments/43657783486099)

Any folders created inside a folder will automatically inherit its permissions. However, if you’ve already created a folder and then change the parent folder permissions, those child folders will not inherit them.

### Complete Folder-Level Security Example

OptiSigns uses a top-down setup, meaning that the highest-level folders will need the most Teams with permissions.

To illustrate this, let’s go back to our example. Here is a partial nested setup:

![complete folder nesting setup](https://support.optisigns.com/hc/article_attachments/43657735762323)

Each layer will require fewer and fewer permissions. For example, here is the permission structure we’d want for the **Pacific** folder:

![regional level folder permissions example](https://support.optisigns.com/hc/article_attachments/43657783490451)

Note how _**every Team operating in the region**_ has permissions for this folder. 

As we go deeper into the nesting, we can eliminate teams that do not need certain permissions. For example, here are the Teams needing **California** folder permissions:

![state level folder security example](https://support.optisigns.com/hc/article_attachments/43657735765779)

Notice how we’ve filtered out the other State-level teams. This means that members of the Oregon or Washington teams will be able to enter the Pacific folder, but would _**not even see**_ the California one.

Going a step further, here are the City/County level permissions we’d want on the **Los Angeles** folder:

![city level folder security example](https://support.optisigns.com/hc/article_attachments/43657783497363)

Here, we’ve filtered out Eagle Mountain (the other city-level team we’ve set up), but kept all the teams corresponding to Los Angeles area store locations. Going down to the **Cosmos Space Center** folder will complete the picture:

![store location folder security example](https://support.optisigns.com/hc/article_attachments/43657783497875)

All the other store locations have been filtered out. If we were to look at another store location, we’d exchange the Cosmos Space Center team for the team corresponding to that store. This way, the people assigned to the lowest level teams will only have access to the single folder that applies to them, but members of “higher level” teams will be able to see all the stores in their respective level.