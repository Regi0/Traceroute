Completed by chatGPT prompting
I suggest using the Excel file, since it can use txt and Excel files + it will add colour coding to the attempts.


Objective:
do the same, but for ping, see: https://github.com/Regi0/Ping

It will try and do tracert for the hostnames, the program will ask you a filename and it will use that data
Input: txt file/Excel file


2 options: 
txt files -> traceroute_txt.py
input: txt file
Output: txt file
name of the host + IP address if hostname
timestamp
attempts

Excel files -> traceroute_excel.py
input: txt file or Excel file
Output: Excel file
name of the host + IP address if hostname
timestamp
attempts
colourcode the attempts: green is OK, red is failed
