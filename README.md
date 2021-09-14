# Stock-Checker
Stock-Checker is a stock checker that can be used for a variety of products on a large majority of sites, although originally primarily created for Xbox stock finding (Managing to land myself a Limited Edition Halo Xbox Series X, which at the time of writing this, are selling for almost 100% profit on eBay), hence the pre-made aliases.  However, I have since modified it to be more adaptable to different uses.

The way this stock checker works is by using the stockCheck.py program.  This program takes in arguments such as the webpage URL you are looking for stock on, what the notification should say when you find stock, who the notification should be sent to, etc.  To see the full argument list, run stockCheck.py without any arguments.

Arguably the most important argument passed is the text-to-find-in-page-for-match argument.  This states what text must be found in the fetched webpage in order for the program to have found stock.  For example, on amazon.co.uk, an item is generally in stock if "Add to Basket" is found on the page.  In this case you would pass "Add to Basket" for the text-to-find-in-page-for-match argument.

To ease having to type out all the arguments every time you want to find stock, aliases can be created, which are explained in the Creating You Own Stock Checks section.

<br><br>

## Prerequisites (Required If Wanting Notifications)
1. A (preferably throwaway) gmail account (or other provider) which will send notifications as emails to recipient addresses

<br><br>

## To Use (All Steps Required)
1. Clone the project to a directory of your choosing.
2. Create and export (important) three environment variables listed below, preferably in a shell rc file, or a file sourced by it (something all shells can have access to)
    * `stockCheckerLocation` - Set this as the absolute path to the location of this project
    * `stockCheckerSenderEmail` - Set this to the email address of your throwaway notifier account
    * `stockCheckerPassword` - Set this to the password of your email account
3. Add this command to the end of your rc file, or a file sourced by your rc, in order to gain the pre-made Xbox aliases for select stores, as well as any future aliases you may create
    ```bash
    source $stockCheckerLocation/.stockAliases.sh
    ```
4. Resource your shell or open a new one and you should now be able to use the aliases in `.stockAliases.sh`.

<br><br>

## Creating Your Own Stock Checks (Optional)
To create your own stock check for a specific product and site, you have two options:
1. Manually run the stockCheck.py program by typing out each argument it expects (simpler but more time consuming in the long run)
2. Creating an alias (faster in the long run but extra steps to create one)
    * Create an alias in `$stockCheckerLocation/.stockAliases.sh`, such as `alias penFinder="bash $stockCheckerScriptsLocation/penFinder.sh"`.  It makes it simpler if the shell script in `$stockCheckerScriptsLocation` matches the name of the alias, i.e. they share the common name penFinder, with the shell script simply extending the name with a .sh extension
        * This alias will run a script (created in the next step) in the `$stockCheckerLocation/stockCheckerScripts` directory (equivalent to `$stockCheckerScriptsLocation`) that will in turn execute stockCheck.py, giving it the correct arguments.
        * Note: This structure was used to avoid the naunces of bash quotations
        * Note: You do not need to define `$stockCheckerScriptsLocation`; it is done for you once you set `$stockCheckerLocation` and complete step 4 of To Use above
    * Create a shell script in `$stockCheckerScriptsLocation` matching the name of that in the last step, i.e. `touch $stockCheckerScriptsLocation/penFinder.sh`
    * In this script simply type `python3 $stockCheckerLocation/stockCheck.py ...`, where `...` represents the arguments desired for stockCheck.py
