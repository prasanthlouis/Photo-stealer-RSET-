#-------------------------------------------------------------------------------
# Name		: Photo-stealer-RSET
# Purpose	: To download your id-picture
#
# Authors	: Prasanth Louis
#-------------------------------------------------------------------------------

import urllib
x=raw_input("Enter the id of the student's photo")
urllib.urlretrieve('http://www.rajagiritech.ac.in/stud/Photo/'+x+'.jpg', 'student.jpg')
