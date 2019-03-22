def main():

 # Write code here 
 num_i = int(input())
 counter = 0
 space = num_i -1
 for i in range(1,num_i+1):
     j = 1 + (i-1)*2
     print(' ' * (space*2),end='')
     for num in range(1,j+1):
         if(num!=j):
          print(num, end=' ')
         else:
             print(num,end='')
     space = space -1
     if(i != num_i):
      print()

main()