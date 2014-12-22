#Python Sort Script

inputFile = open("input.txt", 'r')
linesOfText = inputFile.readlines()
inputFile.close()

splitFile = []
numericalEntry = []


for entry in linesOfText:
    temp = entry.split("///")
    numericalEntry.append(temp[0])
    splitFile.append(temp[1])

quiz1 = open("Quiz1.txt", 'w')
quiz2 = open("Quiz2.txt", 'w')
quiz3 = open("Quiz3.txt", 'w')
quiz4 = open("Quiz4.txt", 'w')
quiz5 = open("Quiz5.txt", 'w')
quiz6 = open("Quiz6.txt", 'w')
quiz7 = open("Quiz7.txt", 'w')
quiz8 = open("Quiz8.txt", 'w')
quiz9 = open("Quiz9.txt", 'w')
quiz13 = open("Quiz13.txt", 'w')

fileNames = [quiz1, quiz2, quiz3, quiz4, quiz5, quiz6, quiz7, quiz8, quiz9, quiz13]

print len(numericalEntry)

for i in range(len(numericalEntry)):
    print i
    #print "NumEntry", numericalEntry[i]
    #print "splitEntry", splitFile[i]
    try:
        fileNames[int(numericalEntry[i])].write(splitFile[i])
    except:
        try:
            fileNames[9].write(splitFile[i])
        except:
            pass


for fileName in fileNames:
    fileName.close()

