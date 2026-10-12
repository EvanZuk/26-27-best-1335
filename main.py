# array of tag instances corrosponding to the feild and sorted by id
from cmath import sqrt

tags = []

#turns pixels into distance in inches based on an undetermined function derrived from testing the realitive size of tags at diffrent distances, something like distance = real width times something over seen pixeles
def get_distance(width, hight):
    distance_constant = 50 #temp
    tag_dimension = 20 #temp
    distance= (width*distance_constant)/tag_dimension #random example test real
    return distance

#snapshot tags is a nested array, the first element is tag id the second is width third is hight fourth is rotation
def get_pose(snapshot_tags):
    distances = []
    for i in range(snapshot_tags.length()):
        distances.append(get_distance(snapshot_tags[i][1], snapshot_tags[i][2]))


    #circles
    # circle formula (x - tags[snapshot_tags[0][0]].get_x())**2 + (y + tags[snapshot_tags[0][0]].get_y())**2 == distances[0]**2
    #d is center distance between circles, |x0-x1|
    #formula for a is (r0^2-r1^2+d^2)/2d
    #a is x dimension of intersection, find y using pythagorean theorem
    #a^2+r0^2=h^2
    #final stuff i think, p0 is center of first circle = (x0, y0) p1 is center of second circle = (x1, y1) p2 
    #a2+b2=r02

    #pose estimation with two points, aligned on x axis needs to be adjusted for any orientation
    d = abs(tags[snapshot_tags[0][0]].get_x()-tags[snapshot_tags[1][0]].get_x())
    x = (distances[0]**2-distances[1]**2+d**2)/(2*d)
    y = sqrt(distances[0]**2-x**2)
    