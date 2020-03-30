

"""

Following are the detailed steps of a O(n (Logn)^2) algortihm.
Input: An array of n points P[]
Output: The smallest distance between two points in the given array.

As a pre-processing step, the input array is sorted according to x coordinates.

1) Find the middle point in the sorted array, we can take P[n/2] as middle point.

2) Divide the given array in two halves. The first subarray contains points from P[0] to P[n/2]. The second subarray contains points from P[n/2+1] to P[n-1].

3) Recursively find the smallest distances in both subarrays. Let the distances be dl and dr. Find the minimum of dl and dr. Let the minimum be d.

4) From the above 3 steps, we have an upper bound d of minimum distance. Now we need to consider the pairs such that one point in pair is from the left half and the other is from the right half. Consider the vertical line passing through P[n/2] and find all points whose x coordinate is closer than d to the middle vertical line. Build an array strip[] of all such points.

5) Sort the array strip[] according to y coordinates. This step is O(nLogn). It can be optimized to O(n) by recursively sorting and merging.

6) Find the smallest distance in strip[]. This is tricky. From the first look, it seems to be a O(n^2) step, but it is actually O(n). It can be proved geometrically that for every point in the strip, we only need to check at most 7 points after it (note that strip is sorted according to Y coordinate). See this for more analysis.


"""

# 1)Find the mid point in the sorted array, 
# note that we only want to care about the first element (x value)
# of every tuple
def returnmidpoint(array, column=0):
    return len(sorted(array, key=lambda x: x[column]))//2

def returnsort(array, column=0): 
    return sorted(array, key=lambda x: x[column])


def euclicidean_dist(pt1, pt2): 
    return ((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)**0.5


def distbetweenclosestpoints(ptlist, mindist=float("inf")): 
    #take note: when initiating 2 references, exclude the cases whereby ref1=ref2
    for i in range(1,len(ptlist)): 
        for j in range(len(ptlist)-1): 
            dist=euclicidean_dist(ptlist[i], ptlist[j])
            if dist<mindist: 
             dist=mindist
    return mindist

def closestpairofpoints(ptlist,): 
    global strip
    strip=[]

    #basecase: we cant divide the list into half when len(list) is equal to, or less than 3 
    #in that case, we will have at least one half with  
    if len(ptlist)<=3:
        finaldist=distbetweenclosestpoints(ptlist)

    array=returnsort(ptlist, column=0)
    mid=returnmidpoint(ptlist, column=0)
    array1sthalf=array[0: mid]
    array2ndhalf=array[mid+1:len(ptlist)]
    dl=distbetweenclosestpoints(array1sthalf, mindist=float("inf"))
    dr=distbetweenclosestpoints(array2ndhalf, mindist=float("inf"))

    """


    Want an array ofall such point, not an array of all distances

    for i in range(len(array1sthalf)): 
        for j in range(len(array2ndhalf),-1, -1):
            if i and j: 
                d=euclicidean_dist(array1sthalf[j],array2ndhalf[i])
                mindist=min(dl,dr,d)
                if mindist<min(dl,dr): 
                    strip.append(mindist)
                else: 
                    break

    """
    for i in array: 
        if abs(i[0]-array[mid][0])<min(dl,dr): 
            strip.append(i)

    finaldist=min(strip)
    




def dis_between_closest_in_strip(ptlist, min_dis=float("inf")):
    """
    closest pair of points in strip
    Params :
    points, points_count, min_dis (list(tuple(int, int)), int, int)
    Returns :
    min_dis (float):  distance btw closest pair of points in the strip (< min_dis)
    dis_between_closest_in_strip([[1,2],[2,4],[5,7],[8,9],[11,0]],5)
    85
    """

    for i in range(min(6, len(ptlist) - 1), len(ptlist)):
        for j in range(max(0, i - 6), i):
            current_dis = distbetweenclosestpoints(points[i], points[j])
            if current_dis < min_dis:
                min_dis = current_dis
    return min_dis





