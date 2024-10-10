line = input(). split()
sett = list(set(line))


for (l) in sett :
  
  print( l, '=' , line.count(l) )
