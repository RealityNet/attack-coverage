# attack-coverage
An *excel*-centric approach for managing the MITRE ATT&amp;CK® tactics and techniques. 

## the goal

The Excel file *AttackCoverage.xlsx* can be used to get a *coverage measure* of MITRE ATT&amp;CK® tactics and techniques, in terms of *detections rules*. Working as DFIR consultants for different companies, with different SOCs and technologies in place, it was needed a *simple* and *portable* way to get a sort of *awareness* about which attackers' tactics/techniques a customer is able to detect and, more important, what is missing.

## AttackCoverage.xlsx

Before a brief explanation about the usage, please consider that all the 7 worksheet share specific characteristics. The *header* of each worksheet has colours: *gray* means a static fields, strings or numbers; *blue* means calculated values, with formulas; *white* means columns (cells) that expect an input from the users. Usually you will not mess with gray or blue columns, with exceptions. *White* columns with "Active" or "IsActive" captions expect to be blank or filled with the string "*yes*": there is not a "*no*", just "*yes*" or blank.

## adding the first *detection rule*

From the *blue team* perspective, the great part of the job will be done in the **detections** worksheet. Here is where you'll set your detection rules: the provided worksheet has the first four columns as an example, but you can add/remove/change them. Unless you're modifying the excel, do not touch the "*is active*" and "*attack1..3*" columns. Let's insert the **first** detection rule, which aims to detect attackers' attempt to access the LSASS Memory, sub-technique T1003.001.

![adding detection rule](/images/ac_img_1.png)

The first columns, the *gray* ones, are up to you. If you want to make the detection rule *active*, simply write *yes* in the column. To **map** that specific rule to one or more (could be) Attack Techniques/Sub-Techniques, just use the *attack1..3* columns.

Let's switch on **techniques** worksheet. As you will see, we have two **red** lines: one for T1003.001 (LSASS Memory sub-technique) and one for T1003, the *technique* which T1003.001 belongs to.

![techniques](/images/ac_img_2.png)

The **red** colouring reflects the *inconsistent* state reported in column *technique status*. It means you have a detection rule for a specific (sub)technique but your're **missing any data source** required to detect it: check the column *data source available*, which is zero. Techniques data sources are written in the *data sources* column, separated by a pipe '|'. To "solve" the issue you can: disable the rule since it can't work; fix the missing data source as shown in the next picture, by accessing the **source** worksheet and putting "*yes*" in the proper field.

![sources](/images/ac_img_3.png)

## the **techniques** worksheet

Going back to the *techniques* worksheet you'll get two *green* lines and multiple *yellow* ones. First, the green ones: since you have the proper (or, better, *a* proper) data source for the detection rule, the technique status changed to **detect**. It means you *could* be able to detect that specific sub-technique T1003.001. Moreover, since you're detecting a sub-technique, the "*father*" technique T1003 will reflect this detection too, in a slightly different way. The "*default counting rule*" follows:

> By default the **minimum number of expected detection rules** is **1** for Techniques without any sub-technique. For Techniques with one or more sub-techniques, the minum number of expected detection rules is **the number of sub-techniques**. This number is automatically calculated and reported in the "*minimum detection rules*" column.

In the current scenario, the minimum expected detection rule for T1003.001 is *1*, while for T1003 (the Technique) is *8* because "OS Credential Dumping" has eight sub-techniques. What about the *yellow* lines ("*technique status*" equals to "*no detect*")? Since you've enabled a *data source*, any technique using that data source **could be detected**: in different words, you have the data to detect those techniques but *no detections rules* in place! Time to fill the gaps!

![techniques](/images/ac_img_4.png)

## the **STATUS** and the **COVERAGE** worksheets

What you are currently detecting in terms of techniques and sub-techniques, organized by *tactics*, is shown into the STATUS worksheet. It's a better view of the work done, what you're missing entirely (no data sources available!) and what you could detect if you'll prepare the proper detection rules.

![STATUS](/images/ac_img_5.png)

"*Wait a moment. Why in the STATUS cells related to T1003 and T1003.001 we have 0 detection rules and 1 detection rules? And both are green?*". Remember that the STATUS worksheet represents what you are detecting (techniques and sub-techniques) and what you are not. For the *coverage* there is the COVERAGE worksheet. As shown in the next picture, the COVERAGE will report *13%* for the Technique, since you have just 1 out of 8 detection rules expected for T1003.

![COVERAGE](/images/ac_img_6.png)

You'll spot that COVERAGE will address only Techniques organized in the "*classic*" Attack way, by Tactics. In the end, for each Tactics, you'll get the total coverage.

## *I have a new fancy sub-techniques not included in the Attack framework!*

This is supercool, and the Excel file is already built to cover that. Place the detection rule by using the **detection** worksheet and assign to the "*OS Credential Dumping (T1003)*" technique, since it will not apply to any of the sub-techniques described by the Attack framework.

![detections](/images/ac_img_7.png)

Go back to **techniques**: now you got **2** detection rules for T1003, one from T1003.001 and one directly applied to T1003 (column "*detection rules for technique*"). Unfortunately this is **unexpected**: techniques with sub-techniques are not expected to have detection rules applied **directly** to them! This **error** is reported in the "*Error checks*" column: always check it!

![techniques](/images/ac_img_8.png)

> You can't have more detection rules than the expected ones! Coverage will be wrong. Remember the minimum expected ones: **1** for Techniques without any sub-technique; **n** for Techniques with *n* sub-techniques **and 0** for the Technique itself.

How to handle that? Easy, that's the reason of the *white* column "**detection rules modifier**". Just add *1* to the T1003 related cell: it means we *expect* a detection rule that will *direclty* target the "main" Technique T1003. See the pictures.

![techniques](/images/ac_img_9.png)

No more errors: STATUS and COVERAGE will reflect this new addendum.

![STATUS](/images/ac_img_10.png)

![COVERAGE](/images/ac_img_11.png)

## *I want to disable some techniques, I'm not interested in covering them!*

Again, the Excel file is built to support this, by using the "**detection rules modifier**" in the *techniques* worksheet. Suppose you want to disable "*At (Linux) (T1053.001)*" sub-technique since you have no Linux hosts. Simply put **-1** in the cell related to T1053.001, as shown in the next pictures.

![techniques](/images/ac_img_12.png)

This will be reflected in the STATUS too: note that T1053.001 is used in different Tactics.

![STATUS](/images/ac_img_13.png)

What if you want to disable not just that sub-technique but **the whole** T1053 one? Simply put **-1** in each sub-technique belonging to T1053, as shown: you don't need to put a *-1* to the Technique itself, unless it's a Technique without sub-techniques.

![techniques](/images/ac_img_14.png)

Again, the disabled technique (and its sub-techniques) will be shown in **STATUS**.

![STATUS](/images/ac_img_15.png)

What about the **COVERAGE**? It will reflect this fact by putting 100% for the Technique. It could sound *weird*, but indeed it's better not to *remove* it to maintain the *awaraness*.

![COVERAGE](/images/ac_img_16.png)

## *I have a custom data source not in the Attack list!*

This is a bit annoying to update. Use the **sources** worksheet and *insert* a new row: this *insertion* will update the *table*. For example, insert the *Custom data source* as shown

![sources](/images/ac_img_17.png)

Then, **for each of the techniques** involved by this new source you have to update the *data sources* column in the **techniques** worksheet: remember that each source is separated by the *pipe*, "|".

![techniques](/images/ac_img_18.png)

Not the best solution, indeed. A better one should be implemented. After the update, the T1098 will become *yellow*, as expected.

![techniques](/images/ac_img_19.png)

## how to update

I will update the Excel file when new Attack version will be available. Still, if you'll have a filled Excel file you need a way to update your own. As you can see in this repository, there is a folder called *20201030*: this folder contains the files used to create the actual AttackCoverage.xlsx. The most important files are the **.csv** ones, because they are used to fill the "*static*" (*gray* columns) cells for **sources** (file: data_sources.csv), **tactics** (file: tactis.csv) and **techniques** (file: techniques.csv). I will then recreate those file for the new version(s), and you can simply *diff* those CSV files to properly update/insert/remove the related lines in your Excel file. It could be "*complicated*" in case of new *tactics* (as version 8 did), because wrongly updating STATUS and COVERAGE worksheets would introduce errors: so pay attention or "shout" an issue here.

## how is built

As explained in the "*how to update*" section, the starting files to build AttackCoverage.xlsx are the CSV ones. Those files are built by using the Python3 scripts you'll find in the **script** folder: you can use by yourselves to build your own *coverage* approach. There is one major requirement, which is the (awesome) **attackcti** library provided by Roberto Rodriguez (@Cyb3rWard0g) and Jose Luis Rodriguez (@Cyb3rPandaH).

## credits

Kudos and thanks to Roberto Rodriguez (@Cyb3rWard0g) for his *attackcti* framework and, more important, for the inspiration I got from his blog post "How Hot Is Your Hunt Team? " (https://cyberwardog.blogspot.com/2017/07/how-hot-is-your-hunt-team.html)

