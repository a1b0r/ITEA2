try:
    file = open('read.txt','w')
except IOError:
    pass
finally:
    file.close()
