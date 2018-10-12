#Exercise 5b
#Allowing inputs to your script with arcpy.GetParameterAsText()
#Try running with: ENV859 "100 meters" 100 17.6

import arcpy

className = arcpy.GetParameterAsText(0)
distance = arcpy.GetParameterAsText(1)
A = arcpy.GetParameterAsText(2)
B = arcpy.GetParameterAsText(3)

print ("Class name is {}".format(className))
print ("Distance is {}".format(arcpy.GetParameterAsText(1)))
print ("{} + {} = {}?!".format(A,B,A+B))