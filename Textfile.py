text_file = open("TextFile.txt", "a")
text_file.write("Student Name: " + name + "\n")
text_file.write("Student ID: " + student_ID + "\n")
text_file.write("Time: " + str(Sec) + " Seconds" + "\n" )
text_file.close()
