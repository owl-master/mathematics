import math

class pascTriangle():
    def __init__(self,rows_qty):
        if rows_qty>0 and self._is_int(rows_qty):
            self.rows=[[] for i in range(rows_qty)]
            for i in range(rows_qty):
                j=0
                while j <=i:
                    self.rows[i].append(self._binominal(i,j))
                    j+=1
        else:
            print('Quantity of rows must be natural and >0')
    def get_binominal(self,n,k):
        return self.rows[n-1][k-1]
    def print_triangle(self):
        for i in self.rows:
            print(','.join([str(int(x)) for x in i]))
    def _binominal(self,n,k):
        return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    def _is_int(self,x):
        try:
            int(x)
            return True
        except ValueError:
            return False

        
                    
            
        
