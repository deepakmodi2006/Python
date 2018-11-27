file = open("Testfile.txt","w"); 
file.write("Hello Python by Deepak\n"); 
file.write("This is our new text file\n"); 
file.write("and this is another line.\n") 
file.write("Why? Because we can write again.\n"); 
file.close(); 

print("File is Created and Contents are written into.")
print("Writing Colon at end in Python is not mandatory");

print("Now we will read the file\n\n\n")
file = open("Testfile.txt", "r"); 
print(file.read()); 

print("File Read is done.\n\n")

print ("Return the 4 first characters of the file");
f = open("Testfile.txt", "r")
print(f.read(4))

print ("Return 2 Lines of the file");
f = open("Testfile.txt", "r")
print(f.readline())
print(f.readline())