# When writing files, it is important to close the file to save the file, avoid, corrupted file and free up space. 
# This can also be achieved using try and finally 
# try:
#   stream = open('output_file.csv', 'wt')
#   stream.write('Whatever you want to write')
#finally:
#   stream.close()
with open('output_file.csv', 'wt') as stream:
    stream.write('column1, column 2, column 3 ')
    stream.write('1, 2, 3')