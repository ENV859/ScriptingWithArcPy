# Name: Select_Example2.py
# Description: Select roads of Class 4 from major roads tin the gnatcatcher habitat study area

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "V:/ArcPyDemo1/Data/SanDiego"

# Set local variables
in_features = "majorrds.shp"
out_feature_class = "V:/ArcPyDemo1/scratch/majorrdsClass4.shp"
where_clause = '"CLASS" = \'4\''

# Execute Select
arcpy.Select_analysis(in_features, out_feature_class, where_clause)

# Buffer the selected roads feature class we just created
buffRoads = "V:/ArcPyDemo1/scratch/BufferedRoads.shp"
buffDist = "500 meters"
arcpy.Buffer_analysis(out_feature_class,buffRoads,buffDist,'','','ALL')