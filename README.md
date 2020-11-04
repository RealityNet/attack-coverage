# attack-coverage
An *excel*-centric approach for managing the MITRE ATT&amp;CK® tactics and techniques. 

## the goal

The Excel file *AttackCoverage.xlsx* can be used to get a *coverage measure* of MITRE ATT&amp;CK® tactics and techniques, in terms of *detections rules*. Working as DFIR consultants for different companies, with different SOCs and technologies in place, it was needed a *simple* and *portable* way to get a sort of *awareness* about which attackers' tactics/techniques a customer is able to detect and, more important, what it's missing.

## AttackCoverage.xlsx

Before a brief explanation about the usage, please consider that all the 7 worksheet share specific characteristics. The *header* of each worksheet has colours: *gray* means a static fields, strings or numbers; *blue* means calculated values, with formulas; *white* means columns (cells) that expect an input from the users. Usually you will not mess with gray or blue columns, with exceptions. *White* columns with "Active" or "IsActive" captions expect to be blank or filled with the string "*yes*": there is not a "*no*", just "*yes*" or blank.

## adding the first *detection rule*

From the *blue team* perspective, the great part of the job will be done in the **detections** worksheet. Here is where you'll set your detection rules: the provided worksheet has the first four columns as an example, but you can add/remove/change them. Unless you're modifying the excel, do not touch the "*is active*" and "*attack1..3*" columns. Let's insert the **first** detection rule, which aims to detect attackers' attempt to access the LSASS Memory, sub-technique T1003.001.

![adding detection rule](/images/ac_img_1.png)

The first columns, the *gray* ones, are up to you. If you want to make the detection rule *active*, simply write *yes* in the column. To **map** that specific rule to one or more (could be) Attack Techniques/Sub-Techniques, just use the *attack1..3* columns.

Let's switch on **techniques** worksheet. As you will see, we have two **red** lines: one for T1003.001 (LSASS Memory sub-technique) and one for T1003, the *technique* which T1003.001 belongs to.

![techniques](/images/ac_img_2.png)

The **red** colouring reflects the *inconsistent* state reported in column *technique status*. It means you have a detection rule for a specific (sub)technique but your're **missing any data source** required to detect it: check the column *data source available*, which is zero.


## how is built


## credits
