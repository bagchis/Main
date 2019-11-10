#placing 8 queens in the chess board
def is_diagonal_taken(r,c,v): #i =1; r=2;c=2
  for i in range(8):#i is row. v[i] is col.
    if (v[i]==-1):
      continue
    match = (abs(r - i) == abs(c - v[i]));
    if(match) :
      return (True)
  return (False)

v=[0,-1,-1,-1,-1,-1,-1,-1]#each element is the row pos in that col. 1st queen in corner.
r=1; c=2 #initialize for 2nd queen. 2nd row 3rd col

while (r <8) :
  while (c <8) :
    col_taken = c in v
    diagonal_taken = is_diagonal_taken(r,c,v)
    if(col_taken | diagonal_taken) : #cannot place q here
      if(c<7):# go to next col
        c= c+1
      else:# If no col left go to prev row
        r=r-1
        c=v[r]+1
        v[r]=-1
        while(c==8):#u hit last col. go prev row 1 more time
          r=r-1
          c=v[r]+1
          v[r]=-1
        print('<= Not working. Go back and adjust col position for last row:'+' r ='+str(r)+', c ='+str(c)) #to see details
        break
    else:#good spot for q
      v[r]=c
      print('=> r ='+str(r)+', c ='+str(c))#to see details
      r=r+1;c=0
      break
print(['row ='+str(i+1)+', col ='+str(v[i]+1) for i in range(8)])
