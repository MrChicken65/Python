# convert raingfall to CM

# read the file and write out to it
with open("rainfall.txt", "r") as rainFile:
    with open("rainfallinCM.txt", "w") as outFile:
        for line in rainFile:
            values = line.split()

            #grab inches
            inches = float(values[1])

            cm = 2.54 * inches

            outFile.write(values[0] + " " + str(cm) + "\n")

            outFile.write