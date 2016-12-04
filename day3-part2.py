__author__ = 'Richard Craggs'

with open("./data/day3.txt") as f:

    pointer = 0
    content = f.readlines()

    triangles = []

    for i in range(0, len(content)//3):

        line1 = content[i*3].split()
        line2 = content[i*3+1].split()
        line3 = content[i*3+2].split()

        triangles.append((int(line1[0]), int(line2[0]), int(line3[0])))
        triangles.append((int(line1[1]), int(line2[1]), int(line3[1])))
        triangles.append((int(line1[2]), int(line2[2]), int(line3[2])))

    counter = 0

    for triangle in triangles:

        print(triangle)

        if max(triangle) < (sum(triangle) - max(triangle)):
            counter += 1

    print(counter)
