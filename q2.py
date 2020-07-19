import re

fp = open('Data/FloridaVoters.html', 'r')

### NOTE: I TOOK OUT TOTAL. CHECK WITH PROF
'''
# Copy to text file to see what's going on

# Open txt file to Copy FloridaVoters into
outF = open('Data/FloridaVotersHTMLText.txt', 'w')

# Initialize Line with first line
line = fp.readline()
while line is not '':
    # Copy line to txt file
    outF.write(line)
    outF.write("\n")
    
    # Advance to next line
    line = fp.readline()
outF.close()
'''

def identifyTableEntry(line):
    matches = re.findall('<td>', line)
    if len(matches) > 0:
        return True

def identifyCounty(line):
    matches = re.findall('[a-zA-Z]', line)
    if len(matches) > 0 and ''.join(matches) != "Total":
        return True

def sortTuple(tuple, element):

    tuple.sort(key = lambda x:x[element-1])
    return tuple

# Advance file to table
# Initialize Line with first line

countyHeader = 1
republicanHeader = 2
democratHeader = 3

field_tracker = 0
florida_voters = []

line = fp.readline()
while line is not '':
    line = line.rstrip()
    line = line.lstrip()


    if identifyTableEntry(line):
        line = line.lstrip("<td>")
        line = line.rstrip("</td>")

        if identifyCounty(line):
            field_tracker = 1
            county = line
            print(county)

        if field_tracker != 0:
            resetFalse = True
            print("FT: " + str(field_tracker))
            if field_tracker > democratHeader:
                field_tracker = 0
                florida_voters.append((county, republicanVotes, democratVotes))
                resetFalse = False
            elif field_tracker == republicanHeader:
                republicanVotes = int(''.join(line.split(",")))
                print(republicanVotes)
            elif field_tracker == democratHeader:
                democratVotes = int(''.join(line.split(",")))
                print(democratVotes)

            if resetFalse:
                field_tracker += 1

    # Advance to next line
    line = fp.readline()

sortedCounties = sortTuple(florida_voters, 3)
for countyInfo in sortedCounties:
    print(countyInfo)







