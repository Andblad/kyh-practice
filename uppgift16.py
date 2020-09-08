import pathlib
p = pathlib.Path('system.log')


#content=p.read_text()
#print(content)
#line = p.readline()


searchfile = open(p)
for line in searchfile:
    if 'BEAR' in line: print(line)
    if 'X-RAY' in line: print(line)
searchfile.close()

