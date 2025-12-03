# Remotely Control and Command OptiSigns Devices
**Article URL:** https://support.optisigns.com/hc/en-us/articles/360055486554-Remotely-Control-and-Command-OptiSigns-Devices
**Article ID:** 360055486554

To submit the command to manage the devices remotely, you will need to go to the remote command execution console. Click **Screens** , then the **More Options (Three Dots)**

Screens -> More Options Icon -> Execute Remote Commands

![more options execute remote commands](https://support.optisigns.com/hc/article_attachments/43590071795219)

The Execute Remote Commands console can be broken down into three sections:

  * **Section 1** \- Where you specify the target of the commands.
  * **Section 2** \- The command you want to execute.
  * **Section 3** \- The execution result and history.



![execute remote commands steps](https://support.optisigns.com/hc/article_attachments/43590102885907)

For section 1, there are 2 types of targets you can choose from:

  * **Screens** \- You can select the screen name here, it can be one screen or multiple screens.
  * **Tags** \- Utilizing tags, you can execute the command on a group of devices. In the below example, the command will be submitted to all devices tagged as Windows or Raspberry Pi.



![target and tags execute remote commands](https://support.optisigns.com/hc/article_attachments/43590071798035)

For section 2, you can enter the command you want to execute in the text box. The command needs to be OS-specific, depending on the OS your device is running on (Android for Android Stick, Linux for OptiSigns Pro / ProMax players), you will need to build the scripts accordingly. Once you have your commands ready, just click the submit button. The command will be pushed to the devices for execution.

Other than the free-form scripts, there are some common commands built into the platform, to achieve these functions, you will just need to select it from the drop-down menu. Depending on the type of device OS, the command will be submitted accordingly.

![refresh and relaunch](https://support.optisigns.com/hc/article_attachments/43590071799571)

After a command is executed, it will appear in section 3: the command history.

**NOTE**  
---  
The **Refresh & Relaunch **command can be used on any device. The **Reboot Device** command cannot be used on certain Android devices.  
  
### Controlling Remote Commands Received by Players

In some cases, you may not want some of your devices to be controlled remotely for any reason. The ability to receive remote commands can be toggled on the device.

Go to the side menu on the OptiSigns player, click **Advanced Options** , and you'll find the toggle for **Execute Remote Commands**. Toggling this off will cause the device to reject remote commands.

![controlling remote commands in-app menu](https://support.optisigns.com/hc/article_attachments/43590102889363)