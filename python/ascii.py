strTable = "<html><table><tr><th>Char</th><th>ASCII</th></tr>"
 
for num in range(33,48):
 symb = chr(num)
 strRW = "<tr><td>"+str(symb)+ "</td><td>"+str(num)+"</td></tr>"
 strTable = strTable+strRW
 
strTable = strTable+"</table></html>"
 
hs = open("asciiCharHTMLTable.html", 'w')
hs.write(strTable)
 
print(strTable)
