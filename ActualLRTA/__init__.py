import numpy
import sys
from shapely.geometry import Polygon, LineString
from shapely.geometry.geo import mapping
#Algorithm LRTA (start,states,end)
#    
#    if(start can reach the destination):
#        get to the destination
#        return the end state
#    else
#        for every point in the obstacle, find if the point can see that point
#            compute the LRTA cost and find the point with the least LRTA cost.
#            go to that node
#        LRTA(new_start, states,end)
#
#Algorithm LRTA_Cost(start,intermediate,destination)
#
#    return euclidean(start, intermediate)+euclidean(intermediate,destination)

#set of polygons
polygons=[]

#This function returns the point that has the least LRTA cost given an obstruction
def nearestPoint(intersectPolygons,xyLine,end):
    start=numpy.array(mapping(xyLine)['coordinates'][0])
    point=end
    end=numpy.array(end[0],end[1])
    leastpoint=sys.maxsize()
    for polygon in intersectPolygons:
        for i in range(len(mapping(polygon)['coordinates'][0])):
            current=numpy.array(mapping(polygon)['coordinates'][0][i])
            distance=numpy.linalg.norm(start-current)+numpy.linalg.norm(current-end)
            if distance<leastpoint:
                leastpoint=distance
                point=mapping(polygon)['coordinates'][0][i]
    return point

#This function checks if there are any polygons intersecting the start and the end
def checkPolygons(xyline,end):
    intersectPolygons=[]
    flag=False
    for polygon in polygons:
        if intersect(xyline, polygon):
            flag=True
            intersectPolygons.append(polygon)
    
    if flag:
        return nearestPoint(intersectPolygons, xyline,end)
    else:
        return end

#Returns true if line intersects the polygon
def intersect(xyline,polygon):
    return xyline.intersects(polygon)

#The LRTA implementation
def LRTA(start,end,states):
    loopFlag=True
    path=LineString([(start.x,start.y),(end.x,end.y)])
    while(loopFlag):
        x,y=checkPolygons(path,end)
        if(x,y==end):
            loopFlag=False