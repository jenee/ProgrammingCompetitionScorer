This project will let you run your own little personal programming competition,
scored using ACM ICPC style.

It will not, at least for now, support all of ACM ICPC features, including:

   * a central server
   * multiple people
   * submitting problems for testing
    + and subsequently, penalties for incorrect submissions

# Syntax

## Setup

To start a competition (which will be named by the time it was started):

    python competitionRunner.py start 

To start a *named* competition:

    python competitionRunner.py start <compName>


## Mark a Problem Solved

    python competitionRunner.py <problemNum> <compName>  


## See Score

    python competitionRunner.py score <compName>

# Future

To start a competition with a time limit:

    python competitionRunner.py -t <lengthInHours>
