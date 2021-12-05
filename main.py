#modules
import os

#getting current working directory from OS module.
cwd = os.getcwd()

#host variable for myping function.
host = input("Please input ip adress: ")

#string variables for myping function returns
test_complete = "Test is complete! Logfile.txt is located in: "
test_failed = "Test has failed!"


#funtion for doing ping command in CMD and parsing it into a .csv file using the OS module.
#if response is 0 then test_complete + cwd is returned
#if response is false then test_failed is returned
def myping(host):
    response = os.system("ping -t " + host + " > pingtest.csv")
    
    if response == 0:
        return test_complete + cwd
    else:
        return test_failed

print("The test is running!")
print("If test needs to end prematurely press 'CTRL-C' and find logfile located in: " + cwd)
myping(host)
input("Press any button to exit!")

