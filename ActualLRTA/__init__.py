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
visited=[]
#This function returns the point that has the least LRTA cost given an obstruction
def nearestPoint(intersectPolygons,xyLine,end):
    start=numpy.array(mapping(xyLine)['coordinates'][0])
    point=end
    end=numpy.array(end)
    #print(intersectPolygons)
    leastpoint=sys.maxsize
    for polygon in intersectPolygons:
        for i in range(len(mapping(polygon)['coordinates'][0])):
            current=numpy.array(mapping(polygon)['coordinates'][0][i])
            if((mapping(xyLine)['coordinates'][0]==mapping(polygon)['coordinates'][0][i]) & (mapping(polygon)['coordinates'][0][i] in visited)):
                #print("The same")
                continue
            else:
                if ((mapping(xyLine)['coordinates'][0]) in mapping(polygon)['coordinates'][0]):
                    if (LineString([(mapping(xyLine)['coordinates'][0]),(mapping(polygon)['coordinates'][0][i])]).touches(polygon)): 
                        #print(mapping(polygon)['coordinates'][0][i],False)
                        distance=numpy.linalg.norm(start-current)+numpy.linalg.norm(current-end)
                        if distance<leastpoint:
                            leastpoint=distance
                            point=mapping(polygon)['coordinates'][0][i]
                    else:
                        #print(mapping(polygon)['coordinates'][0][i],True)
                        continue
                else:
                    intersectFlag=False
                    newLine=LineString([(mapping(xyLine)['coordinates'][0]),(mapping(polygon)['coordinates'][0][i])])
                    for p in polygons:
                        if newLine.intersects(p) &  (~(newLine.touches(p))):
                            intersectFlag=True
                    if intersectFlag==False:
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
    return xyline.intersects(polygon) &  ~xyline.touches(polygon)

#The LRTA implementation
def LRTA(start,end):
    loopFlag=True
    print("Start",start,"End",end)
    visited.append(start)
    while(loopFlag):
        path=LineString([(start[0],start[1]),(end[0],end[1])])
        (x,y)=checkPolygons(path,end)
        #print(x,y)
        visited.append((x,y))
        if((x,y)==end):
            loopFlag=False
        else:
            start=(x,y)
            #print(start)

sample=Polygon(((10,10),(10,20),(20,10),(20,20)))
polygons.append(sample)
sample=Polygon(((30, 55),(30, 30),(55, 30),(55, 55)))
polygons.append(sample)
sample=Polygon(((20,70),(20,90),(40,70)))
polygons.append(sample)
#sample=Polygon(((22,20),(22,25),(25,20),(25,25)))
#polygons.append(sample)
#sample=Polygon(((27,20),(27,25),(29,20),(29,25)))
#polygons.append(sample)
LRTA((2,2),(85,90))
print(visited)
