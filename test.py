"""
generate some test cases
define functions to evaluate the performance of the red black tree
"""
from RedBlackTree import RedBlackTree, intersection
import random
from tqdm import tqdm
from timeit import default_timer as timer
import matplotlib.pyplot as plt


def writeLineInLog(words):
    """
    write a line in the log file
    :param words: the words to be logged
    :return:
    """
    fo = open("log.txt", "a")
    fo.write(words + '\n')
    fo.close()


def generateRandomArrays(scale):
    """
    generate nonredundant array with a perticular scale randomly
    :param scale: the length of the generated arrays
    :return:
    """
    return random.sample(range(0, 10 * scale), scale)


def measure_time(func, *args):
    """
    measure the time that func runs
    :param func: particular function
    :param args: the arguments of the input function
    :return:
    """
    tic = timer()
    func(*args)
    toc = timer()
    return toc - tic


def verify(tree, operation):
    """
    verify a tree is a red black tree
    :param operation: the name of the operation
    :param tree: the input tree
    :return:
    """
    status, blackHeight = tree.verify()
    if status and blackHeight is not False:
        writeLineInLog("The tree is a red black tree after " + operation + " operation!")
    else:
        writeLineInLog("ERROR: THE TREE IS NOT A RED BLACK TREE AFTER " + operation.upper() + " OPERATIONS!!!")


def meanFilter(List, window=100):
    """
    smooth the list
    :param window:
    :param List:
    :return:
    """
    if len(List) >= window:
        for i in range(len(List)):
            slice = List[i:i + window]
            List[i] = sum(slice) / len(slice)


def medFilter(List, window=100):
    """
    smooth the list
    :param window:
    :param List:
    :return:
    """
    if len(List) >= window:
        for i in range(len(List)):
            slice = List[i:i + window]
            slice.sort()
            List[i] = slice[int(len(slice) / 2)]


def normalization(List):
    """
    min max normalization
    :param List:
    :return:
    """
    return [(i - min(List)) / (max(List) - min(List)) for i in List]


def test():
    """
    test if all the operations of red black tree work well
    """
    # clear the log file
    fo = open("log.txt", "w")
    fo.close()

    scale = 1000  # the length of the list generated, change it to any non-negative integer if you like

    """ TEST INSERT OPERATION """
    writeLineInLog("########################## TEST INSERT AND TRAVERSE OPERATION ##########################")
    # initialize a empty red black tree
    treeA = RedBlackTree()
    # generate a random int list with nonredundent values
    listA = generateRandomArrays(scale)
    # update log
    writeLineInLog("Generated listA (the first 20 elements): " + str(listA[0:20]))
    for i in listA:
        # insert while test the time spent by each insert operation
        treeA.insert(i)
    verify(treeA, "insert")

    """ TEST TRAVERSE OPERATION """
    """
    traverse the tree and compare the values obtained with the input listA,
    if they are equal then both insert and traverse operations work well
    """
    traversed_resultA = treeA.traverse()
    listA.sort()
    if listA == traversed_resultA:
        writeLineInLog("Inserted " + str(scale) + " values successfully!")
        writeLineInLog("Traversed the red black tree successfully!")
    else:
        writeLineInLog("ERROR: TRAVERSE OR INSERT OPERATION FAILED!!!")

    """ TEST SEARCH OPERATION """
    """
    generate a listB which is different from listA
    check if each value of listB is in listA by both search operation of red black tree and "in" key word of python
    check if the results of the two operations are same or not
    """
    writeLineInLog("########################## TEST SEARCH OPERATION ##########################")
    status = True  # the status of the search operation works well
    listB = generateRandomArrays(scale)
    for i in listB:
        if (i in listA) == (treeA.search(i) is not None):
            continue
        else:
            status = False
    if status:
        writeLineInLog("Search all values successfully!")
    else:
        writeLineInLog("ERROR: SEARCH OPERATION FAILED!!!")

    """ TEST MIN AND MAX OPERATIONS """
    """
    call min and max operation and compare the results with min/max of python
    """
    writeLineInLog("########################## TEST MIN AND MAX OPERATION ##########################")
    if treeA.min() == min(listA):
        writeLineInLog("Find the minimized value of " + str(treeA.min()) + " in the red black tree successfully!")
    else:
        writeLineInLog("ERROR: MIN OPERATION FAILED!!!")
    if treeA.max() == max(listA):
        writeLineInLog("Find the maximized value  of " + str(treeA.max()) + " in the red black tree successfully!")
    else:
        writeLineInLog("ERROR: MAX OPERATION FAILED!!!")

    """ TEST MEDIAN OPERATION """
    """
    compare the median value found by red black tree and sort method
    """
    writeLineInLog("########################## TEST MEDIAN OPERATION ##########################")
    index = len(listA)
    if index % 2 == 0:
        median_traverse = (listA[int(index / 2) - 1] + listA[int(index / 2)]) / 2
    else:
        median_traverse = listA[int(index / 2)]
    median_value = treeA.median()
    if median_value == median_traverse:
        writeLineInLog("Find the median value of " + str(median_traverse) + " successfully!")
    else:
        writeLineInLog("ERROR: MEDIAN OPERATION FAILED!!!")

    """ TEST INTERSECTION OPERATION """
    """
    find the intersection of listA and listB and compare it with te results obtained by intersection method
    """
    writeLineInLog("########################## TEST INTERSECTION OPERATION ##########################")
    # generate correct answer
    intersection_label = []
    for i in listA:
        if i in listB:
            intersection_label.append(i)
    # initialize another red black tree B
    treeB = RedBlackTree()
    for i in listB:
        # insert while test the time spent by each insert operation
        treeB.insert(i)
    # find the intersection between the two trees
    intersection_trees = intersection(treeA, treeB)
    if intersection_trees == intersection_label:
        writeLineInLog("Find the intersection successfully!")
    else:
        writeLineInLog("ERROR: FIND THE INTERSECTION FAILED!!!")

    """ TEST DELETE OPERATION """
    """
    select a value in listA randomly and delete it in the red black tree
    traverse the tree after being deleted and check if the selected value is still in the tree
    """
    writeLineInLog("########################## TEST DELETE OPERATION ##########################")
    delete_value = random.sample(listA, 1)[0]
    writeLineInLog("Select a value of " + str(delete_value))
    treeA.delete(delete_value)
    traversed_resultA = treeA.traverse()
    if delete_value not in traversed_resultA and len(traversed_resultA) == len(listA) - 1:
        writeLineInLog("Deleted " + str(delete_value) + " successfully!")
    else:
        writeLineInLog("ERROR: DELETE OPERATION FAILED!!!")
    verify(treeA, "delete")


def complexity():
    """
    test the complexity of each operation of red black tree
    :return:
    """
    scale = 5000  # the length of the list generated, change it to any non-negative integer if you like

    # test the complexity of median operation
    # initialize a empty red black tree
    treeA = RedBlackTree()
    # generate a random int list with nonredundent values
    listA = generateRandomArrays(scale)
    # initialize a list to store the time cost of insert operation
    median_deltas = []
    for i in tqdm(range(len(listA)), desc="median"):
        treeA.insert(listA[i])
        if (i + 1) % 50 == 0:
            median_deltas.append(measure_time(treeA.median))

    # medFilter(median_deltas, window=5)
    # meanFilter(median_deltas, 5)
    median_deltas = normalization(median_deltas)
    # median_deltas = median_deltas[:int(0.9 * scale)]

    # test the complexity of traverse
    # initialize a list to store the time cost of each operation
    traverse_deltas = []
    scale = 5000
    for i in tqdm(range(scale), desc="traverse"):
        if (i + 1) % 5 == 0:
            treeA = RedBlackTree()
            # generate a random int list with nonredundent values
            listA = generateRandomArrays(i)
            for i in range(len(listA)):
                treeA.insert(listA[i])
            traverse_deltas.append(measure_time(treeA.traverse))
    meanFilter(traverse_deltas)
    traverse_deltas = normalization(traverse_deltas)
    traverse_deltas = traverse_deltas[:int(0.9 * scale)]

    # test the complexity of intersection
    # initialize a list to store the time cost of each operation
    intersection_deltas = []
    scale = 5000
    for i in tqdm(range(scale), desc="intersection"):
        if (i + 1) % 5 == 0:
            treeA = RedBlackTree()
            treeB = RedBlackTree()
            # generate a random int list with nonredundent values
            listA = generateRandomArrays(i)
            listB = generateRandomArrays(i)
            for i in range(len(listA)):
                treeA.insert(listA[i])
                treeB.insert(listB[i])
            intersection_deltas.append(measure_time(intersection, treeA, treeB))
    meanFilter(intersection_deltas)
    intersection_deltas = normalization(intersection_deltas)
    intersection_deltas = intersection_deltas[:int(0.9 * scale)]

    # test the complexity of insert/min/max/delete/search
    # initialize a list to store the time cost of each operation
    insert_deltas = []
    min_deltas = []
    max_deltas = []
    delete_deltas = []
    search_deltas = []
    scale = 5000
    treeA = RedBlackTree()
    # generate a random int list with nonredundent values
    listA = generateRandomArrays(scale)
    for i in tqdm(range(len(listA)), desc="insert/min/max/delete/search"):
        if (i + 1) % 10 == 0:
            insert_deltas.append(measure_time(treeA.insert, listA[i]))
            min_deltas.append(measure_time(treeA.min))
            max_deltas.append(measure_time(treeA.max))
            search_deltas.append(measure_time(treeA.insert, listA[i - 1]))
        else:
            treeA.insert(listA[i])
    for i in range(len(listA)):
        if (i + 1) % 10 == 0:
            delete_deltas.append(measure_time(treeA.delete, listA[i]))
        else:
            treeA.delete(listA[i])
    medFilter(insert_deltas, window=7)
    medFilter(min_deltas, window=7)
    medFilter(max_deltas, window=7)
    medFilter(delete_deltas, window=7)
    medFilter(search_deltas, window=7)

    meanFilter(insert_deltas, window=7)
    meanFilter(min_deltas, window=7)
    meanFilter(max_deltas, window=7)
    meanFilter(delete_deltas, window=7)
    meanFilter(search_deltas, window=7)

    insert_deltas = normalization(insert_deltas)
    min_deltas = normalization(min_deltas)
    max_deltas = normalization(max_deltas)
    delete_deltas = normalization(delete_deltas)
    delete_deltas.reverse()
    search_deltas = normalization(search_deltas)

    plt.plot(range(1, scale + 1, 10), insert_deltas, label="insert")
    plt.plot(range(1, scale + 1, 10), min_deltas, label="min")
    plt.plot(range(1, scale + 1, 10), max_deltas, label="max")
    plt.plot(range(1, scale + 1, 10), delete_deltas, label="delete")
    plt.plot(range(1, scale + 1, 10), search_deltas, label="search")
    plt.plot(range(1, scale + 1, 50), median_deltas, label="median")
    plt.plot(range(1, scale + 1, 5), traverse_deltas, label="traverse")
    plt.plot(range(1, scale + 1, 5), intersection_deltas, label="intersection")
    plt.legend()
    plt.xlabel('n')
    plt.ylabel('normalized time cost')
    plt.title('Complexity Curves')
    plt.show()
