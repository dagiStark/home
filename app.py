objects = [0,1,1,8,8,0,0,1,8,8]

def find(i):
    if objects[i] != i:
        return find(objects[i])
    else:
        return i

def are_connected(i, j):
    x = find(i)
    y = find(j)
    return x == y

def merge(i, j):
	objects_i = find(i)
	objects_j = find(j)
	objects[objects_i] = objects_j
     

def find(p):
    # Find the root of the component/set
    root = p
    while root != objects[root]:
        root = objects[root]

    # Compress the path leading back to the root.
    # Doing this operation is called "path compression"
    # and is what gives us amortized time complexity.
    while p != root:
        next_p = objects[p]
        objects[p] = root
        p = next_p

    return root

# Finds the representative of the set that i
# is an element of.


def find(i):

	# If i is the objects of itself
	if objects[i] == i:

		# Then i is the representative 
		return i
	else:

		# Recursively find the representative.
		result = find(objects[i])

		# We cache the result by moving i’s node 
		# directly under the representative of this
		# set
		objects[i] = result
	
		# And then we return the result
		return result

# The code is contributed by Arushi Jindal. 


merge(3,5)


print(are_connected(5,3))
