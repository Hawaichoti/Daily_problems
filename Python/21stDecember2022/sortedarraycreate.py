#im = int(input("Enter a list"))
my_list = []
a = []
out = []
my_list = input("Enter a list").split()
for i in my_list:
  a.append(int(i))
lower = int(input("Enter lower range"))
upper = int(input("Enter upper range"))
for i in range(lower,upper+1):
  if i not in a:
    out.append(i)
if not out:
  print(out)
else:
  def groups(d):
    c, start = [d[0]], d[0]
    for i in d[1:]:
      if abs(i-start) != 1:
        yield c
        c = [i]
      else:
        c.append(i)
      start = i
    yield c

    results = [str(a) if not b else f'{a}->{b[-1]}' for a, *b in groups(out)]
    
  print(results)
