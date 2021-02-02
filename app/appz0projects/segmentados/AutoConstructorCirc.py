#//[This is an Autofile by GMAN]
from main import constructordb
from services.dbservice import * #Peso=1
if constructordb == 1:
  dbg = Maindb() #Peso=2:
  dbg.borrartabla('circuitos')
  dbg.creartabla('circuitos')
  dbg.insertnewdata('circuitos','c0','0','stringonG','stringoffG')
  dbg.insertnewdata('circuitos','c1','0','stringonG','stringoffG')

  dbg.desco()