tags = []

#turns pixels into distance in inches based on an undetermined function derrived from testing the realitive size of tags at diffrent distances, something like distance = real width times something over seen pixeles
def get_distance(width, hight):
    distance_constant = 50 #temp
    tag_dimension = 20 #temp
    distance= (width*distance_constant)/tag_dimension #random example test real
    return distance

def get_pose(snapshot_tags[]):
    distances = []
    for i in range(snapshot_tags.length()):
        distances.append(snapshot_tags[i].