# modules
import datetime
import subprocess
import os
import time

# getting current working directory from OS module.
cwd = os.getcwd()

# host variable for myping function.
host = input("Please input ip adress: ")

# string variables for myping function returns
test_complete = "Test is complete! Logfile.txt is located in: "
test_failed = "Test has failed!"

#variables for myping function.
wait_interval_input = input("Enter pinginterval in seconds: ")
hours_to_watch_input = input("Enter the period of test in hours: ")
minutes_to_watch_input = input("Enter the period of test in minutes: ")

# function for doing ping command in CMD and parsing it into a .csv file using the OS module.
# if response is 0 then test_complete + cwd is returned
# if response is false then test_failed is returned
def myping(host, wait_interval=int(wait_interval_input), hours_to_watch=int(hours_to_watch_input), minutes_to_watch=int(minutes_to_watch_input), logfile="myping.csv"):
    end_date = datetime.datetime.now() + datetime.timedelta(hours=hours_to_watch, minutes=minutes_to_watch,)
    current_date = datetime.datetime.now()
    print("Test will end on: " + str(end_date))

    #while loop is set up to run while current date is less than or equal to the end_date.
    while current_date <= end_date:
        # Reset current_date variable to keep track of current time for the while loop
        current_date = datetime.datetime.now()
        #Execute the command we want to do and return the command response
        p = subprocess.Popen("ping -n 1 " + host, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        # Convert binary string to 'normal' string, and split on newline
        ping_response = p.decode('ascii').split("\r\n")[2]
        # Prepare a final text string that we can then use to write to a file.
        final_response = "[" + current_date.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] + "] " + ping_response + "\n"

        file_object = open(logfile, 'a')  # Open file in append mode
        file_object.write(final_response)  # Append the ping response to the end of the file
        file_object.close()  # Close the file write object to prevent file locking

        # Lets wait before we loop again
        time.sleep(wait_interval)

    print(test_complete + cwd)


print("The test is running!")
print("If test needs to end prematurely press 'CTRL-C' and find partial logfile located in: " + cwd)
myping(host)
input("Press any button to exit!")