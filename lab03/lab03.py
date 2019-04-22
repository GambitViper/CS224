from random import random, randrange

def uniform_crossover(parent1, parent2, indpb = 0.2):
    child1 = [x for x in parent1]
    child2 = [y for y in parent2]

    for i in range(len(parent1)):
        if random() < indpb:
            child2[i] = parent1[i]
        if random() < indpb:
            child1[i] = parent2[i]
    
    return child1, child2

def one_point_crossover(parent1, parent2):
    k = randrange(0,len(parent1))

    child1 = parent1[0:k] + parent2[k:len(parent2)]
    child2 = parent2[0:k] + parent1[k:len(parent1)]

    return child1, child2

def two_point_crossover(parent1, parent2):
    k = randrange(0,len(parent1))
    j = k
    while j == k:
        j = randrange(0,len(parent1))

    if j < k:
        tmp = k
        k = j
        j = tmp

    child1 = parent1[0:k] + parent2[k:j] + parent1[j:len(parent1)]
    child2 = parent2[0:k] + parent1[k:j] + parent2[j:len(parent2)]

    return child1, child2

def main():
    parent1 = [0] * 20
    parent2 = [1] * 20

    print("Parent 1: {}".format(parent1))
    print("Parent 2: {}".format(parent2))

    print("------- Uniform Crossover ----------")
    child1, child2 = uniform_crossover(parent1, parent2)

    print("Child  1: {}".format(child1))
    print("Child  2: {}".format(child2))

    print("------- One Point Crossover ------- ")
    child1, child2 = one_point_crossover(parent1, parent2)

    print("Child  1: {}".format(child1))
    print("Child  2: {}".format(child2))

    print("------- Two Point Crossover ------- ")
    child1, child2 = two_point_crossover(parent1, parent2)

    print("Child  1: {}".format(child1))
    print("Child  2: {}".format(child2))

if __name__ == "__main__":
    main()