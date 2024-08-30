# import the time module
import time

# get the current time in seconds since the epoch
seconds = time.time()

print("Seconds since epoch =", seconds)	


# Output: Seconds since epoch = 1672214933.6804628


# convert the time in seconds since the epoch to a readable format
local_time = time.ctime(seconds)

print("Local time:", local_time)

print("-----------------------------------------------")
#local time
result = time.localtime(1672214933)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

print("-----------------------------------------------")

#gmtime 
result = time.gmtime(1672214933)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

print("-----------------------------------------------")
#mktime 
time_tuple = (2022, 12, 28, 8, 44, 4, 4, 362, 0)

# convert time_tuple to seconds since epoch
seconds = time.mktime(time_tuple)

print(seconds)

# Output: 1672217044.0


print("-----------------------------------------------")

#asctime
t = (2022, 12, 28, 8, 44, 4, 4, 362, 0)

result = time.asctime(t)
print("Result:", result)

# Output: Result: Fri Dec 28 08:44:04 2022