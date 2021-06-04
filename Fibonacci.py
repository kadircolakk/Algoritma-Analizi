#Fibonacci with recursive function:
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


#Fibonacci with memoization:
def fastFib(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        return result

class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = "<" + self.name + ", " + str(self.value) + ", " + str(self.weight) + ">"

#0/1 Knapsack problem function:
def maxVal(toConsider, avail):
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        #Explore right branch only:
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        #Explore left branch:
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        #Explore right branch:
        withOutVal, withoutToTake = maxVal(toConsider[1:], avail)
        #Choose better branch:
        if withVal > withOutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withOutVal, withoutToTake)
    return result

#Test:
def smallTest():
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    val, taken = maxVal(Items, 5)
    for item in taken:
        print(item)
    print("Total value of items taken =", val)

def buldManyItems(numItems, maxVal, maxWeight):
    items = []
    for i in range(numItems):
        items.append(Item(str(i))), random.randint(1, maxVal), random.randint(1, maxWeight)
    return items

def bigTest(numItems):
    items = buildManyItems(numItems, 10, 10)
    val, taken = maxVal(items, 40)
    print("Items taken")
    for item in taken:
        print(item)
    print("Total value of items taken = ", val)

#print("fib: ", fib(5))
#print("fastFib: ", fastFib(15)) 
  