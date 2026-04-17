from Generator import etStep

def testGenerator(startStr, slutStr):
    maze = []
    fronter = []
    for i in range(startStr, slutStr, 1):
        try:
            etStep(maze,fronter,i)
            print(i)
        except:
            print("Der op stod en fejl ved: ", i)


testGenerator(0,1000)