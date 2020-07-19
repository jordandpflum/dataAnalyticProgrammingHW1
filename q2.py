import re

def identifyTableEntry(line):
    """
    identify lines which are entries of a table

    Parameters
    ----------
    line = line of file

    Returns
    -------
    True :  Boolean, True if line is part of table
    """
    matches = re.findall('<td>', line)
    if len(matches) > 0:
        return True

def identifyCounty(line):
    """
    identify lines of table which contain county name

    Parameters
    ----------
    line = line of file

    Returns
    -------
    True :  Boolean, True if line contains county name
    """
    matches = re.findall('[a-zA-Z]', line)
    if len(matches) > 0 and ''.join(matches) != "Total":
        return True

def sortTuple(lstTuples, element):
    """
    Sort list of tubles by element n in tuple

    Parameters
    ----------
    lstTuples = lst, a list containing tuples
    element = numeric, index of tuple you want to sort list of tuples by

    Returns
    -------
    lstTuples :  lst, sorted list of tuples
    """

    lstTuples.sort(key=lambda x: x[element-1])
    return lstTuples


def extractVoterTableInfo(textFile):
    # Initialize Field Locations
    countyHeader = 1
    republicanHeader = 2
    democratHeader = 3

    # Initialize Filed Tracker
    field_tracker = 0

    # Initailize Florida Votes List
    florida_voters = []

    # Read all lines of file
    line = textFile.readline()
    while line is not '':
        # Strip white space before and after line
        line = line.rstrip()
        line = line.lstrip()

        # Identify if line is a table entry
        if identifyTableEntry(line):
            # Strip extra txt before and after line
            line = line.lstrip("<td>")
            line = line.rstrip("</td>")

            # Identify if line is County Name
            if identifyCounty(line):
                field_tracker = 1
                county = line

            # If Not County Header
            if field_tracker != 0:
                # Set resetFalse field_tracker to True
                resetFalse = True

                if field_tracker > democratHeader:
                    field_tracker = 0
                    # Append Tuple of County Info to florida_voters
                    florida_voters.append((county, republicanVotes, democratVotes))
                    resetFalse = False
                elif field_tracker == republicanHeader:
                    # Extract republicanVotes as int
                    republicanVotes = int(''.join(line.split(",")))
                elif field_tracker == democratHeader:
                    # Extract democratVotes as int
                    democratVotes = int(''.join(line.split(",")))

                # Increment field_tracker if resetFalse==True
                if resetFalse:
                    field_tracker += 1

        # Advance to next line
        line = textFile.readline()

    # Sort County Tuple by Democratic Votes (Least -> Greatest)
    sortedCounties = sortTuple(florida_voters, 3)
    return sortedCounties

fp = open('Data/FloridaVoters.html', 'r')
sortedCounties = extractVoterTableInfo(fp)

for countyInfo in sortedCounties:
    print(countyInfo)

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




