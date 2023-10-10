# my-wc-tool
Coding challenge #1

This is my implementation of the UNIX command line tool `wc` in python. This gives the count of words, bytes, lines characters as output for a given input file or input

## Run this functionality locally
1. Clone this repository
2. run `pip install -r requirements.txt`
3. To run this functionality on the command line run the following commands to form a symlink for the python file
```
sudo ln -s /path/to/wc-tool.py /usr/local/bin/ccwc
readlink -f /usr/local/bin/ccwc   (you should see the full path to the wc-tool.py)
``` 

4. Now you can use the command from any directory:
# To count words
ccwc input.txt -w

# To count lines
ccwc input.txt -l

# To count bytes
ccwc input.txt -b

# To count characters
ccwc input.txt -c

You can replace input.txt with the path to your desired text file.

If no filename is specified, you can provide input directly, and the tool will read from standard input.

5. Enjoy the Results!
The tool will display the requested count along with the input file name (if applicable).

Requirements
Python 3.x
Click library