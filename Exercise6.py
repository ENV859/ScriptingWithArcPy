import arcpy

#Set variable names to the 4 user inputs
className = arcpy.GetParameterAsText(0)
distance = arcpy.GetParameterAsText(1)
A = arcpy.GetParameterAsText(2)
B = arcpy.GetParameterAsText(3)

#Message results back to the status window when run
arcpy.AddMessage("The class name is {}.".format(className))
arcpy.AddWarning("The distance is {}.".format(distance))
arcpy.AddError("{} + {} = {}?!".format(A,B,A+B))