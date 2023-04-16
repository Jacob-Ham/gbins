# Terminal GTFOBins

This Python script allows you to fetch the GTFOBins (https://gtfobins.github.io/) for a specified command-line tool and displays its privilege escalation techniques on the terminal.
## Installation

Clone this repository or download the gbins.py file.
Run the shell script located in /scripts to make the script executable and copy it to /usr/bin:

```bash
git clone https://github.com/Jacob-Ham/gbins.git
cd gbins
pip install -r requirements.txt
cd scripts
sudo bash install.sh  
```
## Usage

Once you have installed the script and its dependencies, you can run the script with the following command:

```bash
gbins <command>
```
Replace <command> with the binary you want to fetch GTFOBins for. For example, to fetch GTFOBins for the 7z tool, run:
```bash
gbins 7z
```
If you don't specify a command, the script will prompt an error message to specify a GTFOBin.

The script will display the privilege escalation techniques on the terminal.

## Dependencies

requests: A library for making HTTP requests in Python.

beautifulsoup4: A library for parsing HTML and XML documents.

rich: A library for creating beautiful and interactive rich text on the terminal.

