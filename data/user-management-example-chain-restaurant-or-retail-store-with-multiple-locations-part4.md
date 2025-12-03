# User Management Example - Chain Restaurant or Retail Store with Multiple Locations
**Article URL:** https://support.optisigns.com/hc/en-us/articles/43657735780627-User-Management-Example-Chain-Restaurant-or-Retail-Store-with-Multiple-Locations
**Article ID:** 43657735780627

**IMPORTANT NOTE**  
---  
There are no such things as “Sub-Teams” in OptiSigns. While it is possible to provide regional managers (in our example) access to all the screens or content under their purview, they WILL NOT be able to manage their users in kind. This can only be done by Super Admins, who can manage Users across teams. Set up your teams accordingly.  
  
Now we’ll proceed to create all our Teams. A basic setup might look something like this:

![teams setup with admins and users](https://support.optisigns.com/hc/article_attachments/43657735756435)  
A bit about User Roles before we continue:

  * **Owner / Super Admin** -**** Have full access to all teams. Can create teams and access billing. Capable of inviting users to teams, managing all screens, and resetting passwords across multiple teams.
  * **Admin** \- Has full access to an individual team. Can invite users to the team, manage the number of screens available per team, and reset passwords for other users.
  * **User** \- Can create, edit, and delete all content within the folders they have access to. Can add or remove screens.



The others, we don’t need to worry about for this example. For more on User Roles, see our article on [**Managing User Roles**](https://support.optisigns.com/hc/en-us/articles/360046356113-Advanced-Security-Managing-User-Roles).

For this example, we’ve given Admin access to all our regional and local managers, as well as the store manager. A User has been added to the store as well, who will be able to add content and edit the screens only within that store. 

**NOTE**  
---  
If you plan to add Users to the platform via SSO, you may skip this step. We’ve created the users above for demonstration purposes.  
  
Finally, _**Refresh your browser**_. You’ll need to do this before the next step.

* * *

## Set Up Folder-Level Security

Now that we’ve made our Teams, it’s time to set up Folder Level security. We only want to grant access to screens that the users on the Team will actually use, and no more.

To do this, go to your **Screens** tab. Find the Folder you want to set permissions for. In this case, we’ll start with the **Pacific** folder at the top of the structure. Click the **Three Dots → Change Permissions:**

![find change permission tab on folder](https://support.optisigns.com/hc/article_attachments/43657783484051)

The **Change Security** screen will appear. Click underneath where it says “Everyone on this team” and a list of Teams will appear. In our example, we’ll choose the **Pacific Region** team.