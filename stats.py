def mean(arr):
    if len(arr)==0:
        return 0
    #average = sum of elements/no of elements
    return sum(arr)/len(arr)

def median(arr):
    if len(arr)==0:
        return 0
    #sorting the list in ascending order
    arr.sort()
    n=len(arr)
    #if len is even
    if n%2==0:
        #returing sum of middle elements/2
        return (arr[n//2]+arr[n//2-1])/2
    else:
        #returning middle of list
        return arr[n//2]
    
def mode(arr):
    if len(arr)==0:
        return 0
    cnt=0
    md=0
    #sorting list to return least repeated
    arr.sort()
    for i in arr:
        #if count of i greater then previous
        if arr.count(i)>cnt:
            #new max count is assigned
            cnt=arr.count(i)
            #new mode is assigned
            md=i
    return md

def main():
    arr=[1,2,3,4,1,2,3,4,1,2,1,3]
    print("Mean:",mean(arr))
    print("Median:",median(arr))
    print("Mode:",mode(arr))
main()
