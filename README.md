# attack-coverage
An *excel*-centric approach for managing the MITRE ATT&amp;CK® tactics and techniques. 

## the goal

The Excel file *AttackCoverage.xlsx* can be used to get a *coverage measure* of MITRE ATT&amp;CK® tactics and techniques, in terms of *detections rules*. Working as DFIR consultants for different companies, with different SOCs and technologies in place, it was needed a *simple* and *portable* way to get a sort of *awareness* about which attackers' tactics/techniques a customer is able to detect and, more important, what it's missing.

## AttackCoverage.xlsx

Before a brief explanation about the usage, please consider that all the 7 worksheet share specific characteristics. The *header* of each worksheet has colours: *gray* means a static fields, strings or numbers; *blue* means calculated values, with formulas; *white* means columns (cells) that expect an input from the users. Usually you will not mess with gray or blue columns, with exceptions. *White* columns with "Active" or "IsActive" captions expect to be blank or filled with the string "*yes*": there is not a "*no*", just "*yes*" or blank.

## inserting the first *detection rule*

From the *blue team* perspective, the great part of the job will be done in the **detections** worksheet. Here is where you'll set your detection rules: the provided worksheet has the first four columns as an example, but you can add/remove/change them. 

## how is built


## credits
