import os
data = open('data.txt', 'r')
# print(data)
line = "_"
num = -2
while line != '':
    number = str(num)
    line = data.readline()
    line = line.replace('|'+number+'    |', '', 1)

    line = line.replace(' [Second Project](https://github.io/)| [Third Project](https://github.io/)|[Final Project](https://github.io/) | ', '')
    line = line.replace('[', '{ \n name:"', 1)
    line = line.replace(']', '", \n', 1)
    line = line.replace('(', 'URL :"', 1)

    line = line.replace(') | [', '", \n gameName: "', 1)
    line = line.replace('](', '", \n gameURL: "', 1)
    line = line.replace(') |', '", \n id:"'+ number + '", \n image: "../Images/' + number +'.png"\n},', 1)


    num = num + 1




    seg = open("final.txt", "a+")
 
    seg.write(line)
    seg.close()