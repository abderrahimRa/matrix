N=int(input("enter the value please"))
lst=[]
lsst=[]
k=0
o=N
if N%2==0:
          z=int((N)/2)
          for i in range(N):
                  lst.append("0")
                  
          for i in range(z,N):#this is for adding *in the first part whish is half 
                    lst[i]="1"
                    k=N-i
                    lst[k]="1"
                    lst[0]=""
                    print(*lst)
                    
          print(*lst)
          for i in range(1,int(N/2)):#this is for deleting the * that i used in the first part :)
                    lst[i]="0"
                    o=o-1
                    lst[o]="0"                 
                    print(*lst)
          
else:
          
          z=int((N)/2)
          for i in range(N):
                  lst.append("0")
          lst[z]=("1")
          k=int(((N-1)/2))
          for i in range(z,N):#this is for adding *in the first part  the fist half  
                    lst[i]="1"
                    lst[k]="1"
                    print(*lst)
                    k=k-1
          o=N
          for i in range(0,int(N/2)):#now we gonna delete it with " " using void 
                   lst[i]="0"
                   o=o-1
                   lst[o]="0"  
                   print(*lst)
          #i used the same code and changed void to 0 and * to 1 and i only added one line in odd numbers that delete first column
          # that will appear as 0 to make it void 
