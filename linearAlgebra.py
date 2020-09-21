import copy
def ref(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):##incorrect, reconsider how to do?
            if not arr[i][j]==0:
                for k in range(i+1,len(arr)):
                    mult=(arr[k][j]*1.0)/arr[i][j]
                    #print(mult)
                    for l in range(0, len(arr[k])):
                        arr[k][l]=arr[k][l]-arr[i][l]*mult
                if not arr[i][j]==1:
                    ratio=arr[i][j]
                    for m in range(j, len(arr[i])):
                        arr[i][m]=arr[i][m]/ratio
                break
    return arr

def rref(arr):
    ordered_arr=ref(arr)
    #matrix_display(ordered_arr)
    #print("")
    for row in range(1,len(ordered_arr)):
        for col in range(0,len(ordered_arr[row])):
            piv=ordered_arr[len(ordered_arr)-row][col]
            if piv!=0:
                for other_row in range(row+1,len(ordered_arr)+1):
                    mult=(ordered_arr[len(ordered_arr)-other_row][col]*1.0)/piv
                    #print(mult)
                    for other_col in range(col,len(ordered_arr[row])):
                        ordered_arr[len(ordered_arr)-other_row][other_col]=ordered_arr[len(ordered_arr)-other_row][other_col]-ordered_arr[len(ordered_arr)-row][other_col]*mult
                break
        #matrix_display(ordered_arr)
        #print("")
    return ordered_arr
            

def matrix_display(arr, augment=True):
    last=len(arr[0])-1
    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])-1):
            print(str(arr[i][j])+" ",end='')
        if augment:
            print("|"+str(arr[i][last]))
        else:
            print(str(arr[i][last]))
    print("")
    
##Matrix already in rref
def solution_display(arr):
    for row in arr:
        ans=""
        for col in range(0,len(row)-1):
            if row[col]==1:
                ans="X"+str(col+1)+" = "
                ans=ans+str(row[len(row)-1])+" "
                for col_two in range(col+1, len(row)-1):
                    if row[col_two]!=0:
                        if row[col_two]>0:
                            ans=ans+"- "+ str(row[col_two])+"*X"+str(col_two+1)
                        elif row[col_two]<0:
                            ans=ans+" + "+ str(row[col_two]*-1)+"*X"+str(col_two+1)
                if len(ans)>5:
                    print(ans)
                break
    print("")
                
def transpose(arr):
    ans=[]
    for c in range(0,len(arr[0])):
        ans.append([])
        for r in range(0,len(arr)):
            ans[c].append(arr[r][c])
    return ans

def matrix_mult(arr_one,arr_two):
    if len(arr_one)!=len(arr_two[0]):
        return []
    ans=[]
    for r in arr_one:
        ans.append([])
    for c in range(0, len(arr_two[0])):
        for row in range(0,len(arr_one)):
            entry=0
            for r in range(0,len(arr_two)):
                entry=entry+arr_two[r][c]*arr_one[row][r]
            ans[row].append(entry)
    return ans