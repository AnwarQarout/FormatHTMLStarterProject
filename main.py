import csv
tableData = ""
with open('test.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        tableData+="<tr>"
        tableData+="<td>"
        temp = str(row[0])
        temp=temp.replace(";","</td><td>")
        temp+= "</td>"
        tableData += temp
        tableData += "</tr>"

print(tableData)
file = open('template.html','r')
oldFile = file.read()
file.close()
oldFile = oldFile.format(tableData)
file = open('final.html','w')
file.write(oldFile)
