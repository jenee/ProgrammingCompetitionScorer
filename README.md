This project will let you run your own little personal programming competition,
   scored using ACM ICPC style.

   It will not, at least for now, support all of ACM ICPC features, including:
   * a central server
   * multiple people
   * submitting problems for testing
    + and subsequently, penalties for incorrect submissions 
   * 
Syntax: 

SETUP 

   To start a competition (which will be named by the time it was started)
   python competitionRunner.py start 

   To start a *named* competition:
   python competitionRunner.py start <compName>


MARK A PROBLEM SOLVED
   python competitionRunner.py <problemNum> <compName>  


SEE SCORE
   python competitionRunner.py score <compName>



FUTURE:
   To start a competition with a time limit
   python competitionRunner.py -t <lengthInHours>
   

