import time
import random

# 3 döngülü MaxSubSum3 fonksiyonu O(n^3):
def maxSubSum3(my_array):

    maxSum = 0
    n = len(my_array)

    for i in range(n):

        for j in range(i,n):

            thisSum = 0

            for k in range(i,j):

                thisSum += my_array[k]

                if(thisSum > maxSum):

                    maxSum = thisSum
                    
    return maxSum

# 2 döngülü MaxSubSum2 fonksiyonu O(n^2):
def maxSubSum2(my_array):
     
    maxSum = 0
    n = len(my_array)
     
    for i in range(n):
         
        thisSum = 0

        for j in range(i,n):

            thisSum += my_array[j]

            if(thisSum > maxSum):

                maxSum = thisSum
    
    return maxSum

# 1 döngülü MaxSubSum1 fonksiyonu O(n):
def maxSubSum1(my_array):

    maxSum=0 
    thisSum = 0
    n = len(my_array)

    for i in range(n):

        thisSum += my_array[i]

        if(thisSum > maxSum):
            maxSum = thisSum
        elif(thisSum < 0):
            thisSum = 0

    return maxSum

# Recursive fonksiyon O(n*log n):
def maxSubSumRec(my_array):

    n = len(my_array)
    if(n == 1):
        return my_array[0]
    
    left_i = 0
    left_j = n // 2
    right_i = n // 2
    right_j = n

    left_sum = maxSubSumRec(my_array[left_i:left_j])
    right_sum = maxSubSumRec(my_array[right_i:right_j])

    temp_left_sum = 0
    t = 0

    for i in range(left_j-1, left_i-1, -1):
        
        t += my_array[i]

        if(t > temp_left_sum):
            temp_left_sum = t
    
    temp_right_sum = 0
    t = 0

    for i in range(right_i, right_j):
        
        t += my_array[i]
        
        if(t > temp_right_sum):
            temp_right_sum = t
    
    center_sum = temp_left_sum + temp_right_sum

    return max_of_three(left_sum, right_sum, center_sum)

# 2 elemanın max'ını bulan fonksiyon:
def max_of_two(a,b):
    if(a > b):
        return a
    else:
        return b

# 3 elemanın max'ını bulan fonksiyon:
def max_of_three(a, b, c):
    return max_of_two(a, max_of_two(b,c))

# Rastgele liste oluşturma fonksiyonu:
def createList(n):
    list = []
    for i in range(n):
        list.append(random.randint(-100,100))
    return list


# Rastgele liste oluşturma fonksiyonu çağırımı:  
print("liste uzunluğu(n) giriniz...")
n = int(input())
startList = time.time()
list = createList(n)
endList = time.time()
print(n, "elemanlı liste",  (endList - startList), "saniyede oluşturuldu")

#list = [4, -3, 5, -2, -1, 2, 6, -2, 4, -3, 5, -2, -1, 2, 6, -2, 4, -3, 5, -2, -1, 2, 6, -2]

# 3 döngülü MaxSubSum3 fonksiyonu çağrısı:
start3 = time.time()
print("\nMaxSubSum3 = ", maxSubSum3(list))
end3 = time.time()
print("MaxSubSum3 süre: ",(end3 - start3))

# 2 döngülü MaxSubSum2 fonksiyonu çağrısı:
start2 = time.time()
print("\nMaxSubSum2 = ", maxSubSum2(list))
end2 = time.time()
print("MaxSubSum2 süre: ",(end2 - start2))


# 1 döngülü MaxSubSum1 fonksiyonu çağrısı:
start1 = time.time()
print("\nMaxSubSum1 = ", maxSubSum1(list))
end1 = time.time()
print("MaxSubSum1 süre: ",(end1 - start1))

# Recursive fonksiyonun çağrısı:
startRec = time.time()
print("\nMaxSubSumRec = ", maxSubSumRec(list))
endRec = time.time()
print("MaxSubSum1 süre: ",(endRec - startRec))

#Çıkış
exit = input()