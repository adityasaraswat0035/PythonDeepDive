class Point2D:
    def __init__(self,x,y):
        self._x=x
        self._y=y
    def __str__(self):
        return "({s._x},{s._y})".format(s=self)
    
    def __repr__(self):
        return "Point2D(x={s._x},y={s._y})".format(s=self)
    def __format__(self, format_spec):
        if format_spec=='r':
            return '{},{}'.format(self._y,self._x)
        else:   
            return '{},{}'.format(self._x,self._y)
        #return '[Formatted point: {}, {}, {}]'.format(self._x, self._y,format_spec)

if __name__=="__main__":
    p=Point2D(42,69)
    print(p)
    print(str(p))
    print(repr(p))
    print('This is a point: {}'.format(Point2D(1, 2)))
    print('This is a point: {:r}'.format(Point2D(1, 2)))
    #forcing format to call __repr__
    print('{!r}'.format(Point2D(1,2)))
    #forcing format to call __str__
    print('{!s}'.format(Point2D(1,2)))