inFile = open("resources.txt", 'r')
files = inFile.readlines()
print files
inFile.close

outFile = open("FormattedResourceFile.txt", 'w')
for fileEntry in files:
    outFile.write('"'+fileEntry+'"')
outFile.close()
