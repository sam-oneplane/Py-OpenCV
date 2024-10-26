import math

class Tracker:
    
    def __init__(self) -> None:
        self.centroids =  {} # item = id : centroid
        self.idCounter = 0

    def update(self, objects) -> list:
        updateCentroids = {} 
        updateCentroidsObjs = []
        def detectObj(X, Y, M) -> bool:
            isSameObj = False
            retId = None
            for objId, point in self.centroids.items():
                # calculate euclidean distance sqrt(X^2 + Y^2)
                eucledianDist = math.hypot(X-point[0], Y-point[1])
                print(f'ID: {objId}, EUC: {eucledianDist}, MaxDistM: {M}')
                if eucledianDist < M:
                    isSameObj = True
                    # update the tracker centroid and centroid's id
                    self.centroids[objId] = (X,Y)
                    retId = objId 
                    break
            return isSameObj, retId
        
        
        for (x,y,w,h) in objects:
            centerX = (x + (x+w))//2
            centerY = (y + (y+h))//2
            maxEucDist = max(w, h)
            # if no detection founds create new centroid and update id counter
            isDetected, id = detectObj(centerX, centerY, maxEucDist)
            if isDetected:
                updateCentroidsObjs.append((x,y,w,h,id))
            else: # not detected    
                self.centroids[self.idCounter] = (centerX,centerY)
                updateCentroidsObjs.append((x,y,w,h,self.idCounter))
                self.idCounter+= 1
        
        # exclude unrelevant centroids points
        
        for updateBBObj in updateCentroidsObjs:
            _,_,_,_,bbId = updateBBObj
            updateCentroids[bbId] = self.centroids[bbId]

        self.centroids = updateCentroids.copy()
        return updateCentroidsObjs
        


