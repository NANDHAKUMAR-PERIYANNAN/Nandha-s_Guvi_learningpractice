class calculator:

  def mul(self,x,y):

    return x*y

  def add(self,x,y):

    return x+y

  def div(self,x,y):

    return x/y

  def sub(self,x,y):

    return x-y

  def per(self,x,y):

    return (x/y)*100

  def si(self,p,n,r):

    temp = mul(p,n)

    temp1 = div(mul(r,temp),100)

    return (temp1)