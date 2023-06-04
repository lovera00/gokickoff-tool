Sure, here is the English version:

# Gokickoff Autologin and Player Efficiency

This Python script uses Selenium to automatically log into gokickoff.com, navigate to the team tactics page, and find the player with the lowest efficiency. If all players have an efficiency over 92%, the script performs activities to earn money.

## Requirements

1. Python 3.7 or higher installed.
2. Selenium WebDriver installed. You can install it with the following command: `pip install selenium`
3. Chrome browser and its corresponding ChromeDriver installed. The ChromeDriver should be in your system PATH or in the same directory as this script. You can download it from [here](https://sites.google.com/chromium.org/driver/).
4. A `credentials.txt` file in the same directory as the script. This file should contain your username and password for gokickoff.com, one per line.

## Usage

1. Clone this repository or download the .py file directly.

2. Create a `credentials.txt` file in the same directory as the script. The first line of this file should be your username on gokickoff.com and the second line should be your password. For example:

    ```
    username
    password
    ```

3. Run the script with Python:

    ```
    python3 verificaEnergia.py
    ```

    (Replace `verificaEnergia.py` with the name of the script file).

The script will open Chrome, log into gokickoff.com, and look for the player with the lowest efficiency. If all players have an efficiency above 92%, the script will perform money-earning activities.

## Security Notes

This script reads the username and password from an unencrypted text file. This is not secure. Do not share the `credentials.txt` file with anyone and do not upload it to any public online location. Consider using additional security measures, such as encryption, in a real production environment.
