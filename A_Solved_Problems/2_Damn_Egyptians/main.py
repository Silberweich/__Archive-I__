#This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main

print(add_time("3:00 PM", "3:10"))
print(">Returns: 6:10 PM")
 
print(add_time("11:30 AM", "2:32", "Monday"))
print(">Returns: 2:02 PM, Monday")
 
print(add_time("11:43 AM", "00:20"))
print(">Returns: 12:03 PM")
 
print(add_time("10:10 PM", "3:30"))
print(">Returns: 1:40 AM (next day)")
 
print(add_time("11:43 PM", "24:20", "tueSday"))
print(">Returns: 12:03 AM, Thursday (2 days later)")
 
print(add_time("6:30 PM", "205:12"))
print(">Returns: 7:42 AM (9 days later)")

#Run unit tests automatically
main(module='test_module', exit=False)