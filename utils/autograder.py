from unittest.mock import patch 
from io import StringIO 
import random

# match variable output
def var_cmp(v1,v2):
  passed = 'Salah'
  if v1 == v2:
    passed = 'Benar'
  l = [passed,v1,type(v1),v2,type(v2)]
  return l

def func_cmp(f1,f2,rng,*args,**kwargs):
  passed = 'Salah'
  e=None
  random.seed(rng)
  o1 = f1(*args,**kwargs)  
  try:
    random.seed(rng)
    o2 = f2(*args,**kwargs)
  except Exception as er:
    e=er
  finally:
    if e:
      return ['Error',str(e)]
    else:
      if type(o1) == float:
        o1 = round(o1,6)
        o2 = round(o2,6)
      if o1 == o2:
        passed = 'Benar'
      l = [passed,o1,type(o1),o2,type(o2)]
      return l

def get_printout(f,*args,**kwargs):    
    with patch('sys.stdout', new = StringIO()) as fake_out: 
        f(*args,**kwargs)
        return fake_out.getvalue()

def funcout_cmp(f1,f2,rng,*args,**kwargs):
  passed = 'Salah'
  e=None
  random.seed(rng)
  o1 = get_printout(f1,*args,**kwargs)
  try:
    random.seed(rng)
    o2 = get_printout(f2,*args,**kwargs)
  except Exception as er:
    e=er
  finally:
    if e:
      return ['Error',str(e)]
    else:
      if o1 == o2:
        passed = 'Benar'
      l = [passed,o1,type(o1),o2,type(o2)]
      return l

class CmpTestcase():
  def __init__(self, v1,v2, rng=0,tCases=None,cmp_out=False):
    self.tCases=tCases
    self.score = 0
    self.v = v1
    if not callable(v1):
      self.out = var_cmp(v1,v2)
      self.score = 1 if self.out[0] == 'Benar' else 0 
  
    elif tCases==None:
      raise 'Please provide tCases list of tupple [(*args,*kwargs)]'
    else:
      self.out = []
      if cmp_out:
        f = funcout_cmp            
      else:
        f = func_cmp

      for i, (args,kwargs) in enumerate(tCases):
        out = f(v1,v2,rng+i,*args,**kwargs)
        self.score += 1 if out[0] == 'Benar' else 0
        out.append('seed : ' + str(rng+i))
        self.out.append(out)

      self.score /= len(tCases)
      

         
  def __str__(self,name='var'):
    summary=''
    if not callable(self.v):
      summary = str(self.out)+'\n'
    else:
      if name == 'var':
        name = self.v.__name__
      for o,c in zip(self.out,self.tCases):
          summary+='case inputs: '+ str(c)+'\nResults: '+str(o)+'\n'
    
    return name +' :\n'+summary
    
