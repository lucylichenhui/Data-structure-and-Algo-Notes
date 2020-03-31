

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
    global num 
    #print(pt1)
    num=((int(pt1[0])-int(pt2[0]))**2+(int(pt1[1])-int(pt2[1]))**2)
    print(num)
    


def distbetweenclosestpoints(ptlist, current_dis=float("inf")): 
    #print(len(ptlist))
    #take note: when initiating 2 references, exclude the cases whereby ref1=ref2
    for i in range(1,len(ptlist)): 
        for j in range(len(ptlist)-1): 
            euclicidean_dist(pt1=ptlist[i], pt2=ptlist[j])
            if num<current_dis: 
             current_dis=num
    return current_dis



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
        #want to compare each of index i and j to at least 6 neighbours 
        for j in range(max(0, i - 6), i):
            euclicidean_dist(ptlist[i], ptlist[j])
            current_dis=num
            if current_dis < min_dis:
                min_dis = current_dis

    print(min_dis)
    return min_dis



def closestpairofpoints(ptlist): 
    global strip
    strip=[]

    #basecase: we cant divide the list into half when len(list) is equal to, or less than 3 
    #in that case, we will have at least one half with  
    if len(ptlist)<=3:
        finaldist=distbetweenclosestpoints(ptlist)

    array=returnsort(ptlist, column=0)
    #print(array)
    mid=returnmidpoint(ptlist, column=0)
    #print(mid)
    array1sthalf=array[0: mid]
    array2ndhalf=array[mid+1:len(ptlist)]
    dl=distbetweenclosestpoints(array1sthalf, current_dis=float("inf"))
    #print(array1sthalf)
    dr=distbetweenclosestpoints(array2ndhalf, current_dis=float("inf"))

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


    min_dis=dis_between_closest_in_strip(strip,min_dis=float("inf"))
    final_dist= min(min_dis,dl,dr)
    return final_dist
    #finaldist=min(strip)
    



if __name__ == "__main__":
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print("Distance:", closestpairofpoints(points))




                    #==========================#


                    """
The algorithm finds distance between closest pair of points
in the given n points.
Approach used -> Divide and conquer
The points are sorted based on Xco-ords and
then based on Yco-ords separately.
And by applying divide and conquer approach,
minimum distance is obtained recursively.
>> Closest points can lie on different sides of partition.
This case handled by forming a strip of points
whose Xco-ords distance is less than closest_pair_dis
from mid-point's Xco-ords. Points sorted based on Yco-ords
are used in this step to reduce sorting time.
Closest pair distance is found in the strip of points. (closest_in_strip)
min(closest_pair_dis, closest_in_strip) would be the final answer.
Time complexity: O(n * log n)
"""


def euclidean_distance_sqr(point1, point2):
    """
    >>> euclidean_distance_sqr([1,2],[2,4])
    5
    """
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2


def column_based_sort(array, column=0):
    """
    >>> column_based_sort([(5, 1), (4, 2), (3, 0)], 1)
    [(3, 0), (5, 1), (4, 2)]
    """
    return sorted(array, key=lambda x: x[column])


def dis_between_closest_pair(points, points_counts, min_dis=float("inf")):
    """
    brute force approach to find distance between closest pair points
    Parameters :
    points, points_count, min_dis (list(tuple(int, int)), int, int)
    Returns :
    min_dis (float):  distance between closest pair of points
    >>> dis_between_closest_pair([[1,2],[2,4],[5,7],[8,9],[11,0]],5)
    5
    """

    for i in range(points_counts - 1):
        for j in range(i + 1, points_counts):
            current_dis = euclidean_distance_sqr(points[i], points[j])
            if current_dis < min_dis:
                min_dis = current_dis
    return min_dis


def dis_between_closest_in_strip(points, points_counts, min_dis=float("inf")):
    """
    closest pair of points in strip
    Parameters :
    points, points_count, min_dis (list(tuple(int, int)), int, int)
    Returns :
    min_dis (float):  distance btw closest pair of points in the strip (< min_dis)
    >>> dis_between_closest_in_strip([[1,2],[2,4],[5,7],[8,9],[11,0]],5)
    85
    """

    for i in range(min(6, points_counts - 1), points_counts):
        for j in range(max(0, i - 6), i):
            current_dis = euclidean_distance_sqr(points[i], points[j])
            if current_dis < min_dis:
                min_dis = current_dis
    return min_dis


def closest_pair_of_points_sqr(points_sorted_on_x, points_sorted_on_y, points_counts):
    """ divide and conquer approach
    Parameters :
    points, points_count (list(tuple(int, int)), int)
    Returns :
    (float):  distance btw closest pair of points
    >>> closest_pair_of_points_sqr([(1, 2), (3, 4)], [(5, 6), (7, 8)], 2)
    8
    """

    # base case
    if points_counts <= 3:
        return dis_between_closest_pair(points_sorted_on_x, points_counts)

    # recursion
    mid = points_counts // 2
    closest_in_left = closest_pair_of_points_sqr(
        points_sorted_on_x, points_sorted_on_y[:mid], mid
    )
    closest_in_right = closest_pair_of_points_sqr(
        points_sorted_on_y, points_sorted_on_y[mid:], points_counts - mid
    )
    closest_pair_dis = min(closest_in_left, closest_in_right)

    """
    cross_strip contains the points, whose Xcoords are at a
    distance(< closest_pair_dis) from mid's Xcoord
    """

    cross_strip = []
    for point in points_sorted_on_x:
        if abs(point[0] - points_sorted_on_x[mid][0]) < closest_pair_dis:
            cross_strip.append(point)

    closest_in_strip = dis_between_closest_in_strip(
        cross_strip, len(cross_strip), closest_pair_dis
    )
    return min(closest_pair_dis, closest_in_strip)


def closest_pair_of_points(points, points_counts):
    """
    >>> closest_pair_of_points([(2, 3), (12, 30)], len([(2, 3), (12, 30)]))
    28.792360097775937
    """
    points_sorted_on_x = column_based_sort(points, column=0)
    points_sorted_on_y = column_based_sort(points, column=1)
    return (
        closest_pair_of_points_sqr(
            points_sorted_on_x, points_sorted_on_y, points_counts
        )
    ) ** 0.5


if __name__ == "__main__":
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print("Distance:", closest_pair_of_points(points, len(points)))