import sys

if len(sys.argv) == 3:
  script_name = sys.argv[0]
  name = sys.argv[0]
  rollno = sys.argv[0]
  print("User provided input values:")

else :
  script_name = sys.argv[0]
  name = "Gaurav"
  rollno = "101"
  print("No input given - using default values:")

print("Script name : ",script_name)
print("Name : ",name)
print("Roll Number : ",rollno)
