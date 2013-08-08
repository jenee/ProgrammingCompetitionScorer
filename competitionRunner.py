import sys
import time

for arg in sys.argv: 
   print arg

taskArg =""
if len(sys.argv) > 1:
   taskArg = sys.argv[1]

print taskArg

competitionStart = 0;
competitionName = "";

if taskArg == "start":
   competitionStart = time.time()
   print competitionStart
   if len(sys.argv) > 2:
      competitionName = sys.argv[2]
   else:
      competitionName = str(competitionStart)
   # file io: http://www.tutorialspoint.com/python/python_files_io.htm
   compRecordFile = open( competitionName, "w" )

   compRecordFile.write( str(competitionStart) );

   compRecordFile.close();
elif taskArg == "score":
   print "This will someday compute the score"
elif taskArg.isnumeric():
   print "This will say that you've solved a problem!"


