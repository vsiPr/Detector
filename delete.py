import os

global pt1, pt2

def dl1(fn):
    global pt1, pt2
    for root, dirs, files in os.walk(r'D:/'):
        for name in files:
            if name == fn:  
                if fn == 'res.png':
                        pt1 = os.path.abspath(os.path.join(root, name))
                        os.remove(pt1)
                elif fn == 'output.avi':
                        pt2 = os.path.abspath(os.path.join(root, name))
                        os.remove(pt2)
                break
            else:
                pt1 = ''
                pt2 = ''
                pass
def dl2(fn):
    global pt1, pt2
    for root, dirs, files in os.walk(r'C:/'):
        for name in files:
            if name == fn:  
                if fn == 'res.png':
                        pt1 = os.path.abspath(os.path.join(root, name))
                        os.remove(pt1)
                        print('pt1 dl2', pt1)
                elif fn == 'output.avi':
                        pt2 = os.path.abspath(os.path.join(root, name))
                        os.remove(pt2)
                        print('pt2 dl2', pt2)
                break
            else:
                pt1 = ''
                pt2 = ''
                break

dl1('res.png')
print('pt1', pt1)
if pt1 == '':
    dl2('res.png')
else:
    pass
dl1('output.avi')
print('pt2', pt2)
if pt2 == '':
    dl2('output.avi')
else:
    os._exit(1)
