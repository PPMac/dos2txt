import os
cmd = input("input cmd:")
p = os.popen(cmd)
txt = p.read()
fname = cmd + ".txt"
f = open(fname,'w')
f.write(txt)
f.close()
