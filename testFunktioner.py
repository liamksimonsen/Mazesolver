from Generator import etStep

def testGenerator(startStr, slutStr):
    maze = []
    fronter = []
    for i in range(startStr, slutStr+1, 1):
        try:
            etStep(maze,fronter,i)
        except Exception as e:
            print("Der op stod en fejl ved:", i, "med fejlen:", e)
    print("Færdig med at teste")


testGenerator(1,500)