# digitalstrom-export-csv
A simple Python script with Selenium which opens the digitalSTROM server and then downloads the CSV file via PyAutoGUI.

## Installation

Plese edit your crontab file with `sudo crontab -e` and add something like this:

```
*/59 */9 * * * DISPLAY=:0 /usr/bin/python3 /home/<path_to_python_file>/digitalstrom.py
```

As a note, in my metering application I can only look at the values for 9 hours and 59.

You have to replace following in the python code:

```
<path_to_pictures>
<path_to_geckodriver>
<ip_to_dss>
<username>
<password>
```
