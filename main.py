import base64

outputFile = open('output.bin', 'wb')
with open('base64.txt', 'r') as f:
    lines = f.readlines()
for line in lines:
    decodedLine = line.replace(' ', '').strip()
    decodedLine = decodedLine.encode('utf-8')
    decodedLine = base64.decodebytes(decodedLine)
    outputFile.write(decodedLine)
outputFile.close()
