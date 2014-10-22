<script src="http://yandex.st/highlightjs/7.3/highlight.min.js"></script>
<link rel="stylesheet" href="http://yandex.st/highlightjs/7.3/styles/github.min.css">
<script>
  hljs.initHighlightingOnLoad();
</script>
#Decorator pattern in classic way    
    
    
    1:  class Beverage:  
	2:    """ beverage class """  
	3:    def __init__(self):  
	4:      self._desc = "Abstract Drink"  
	5:      self._cost = 0.0  
	6:      
	7:    def get_cost(self):  
	8:      return self._cost  
	9:      
	10:    def get_desc(self):  
	11:      return self._desc  
	12:      
	13:  class DarkRoast(Beverage):  
	14:    def __init__(self):  
	15:      self._cost = 3.5  
	16:      self._desc = "Dark Roast ($" + str(self._cost) + ")"  
	17:          
	18:  class Espresso(Beverage):  
	19:    def __init__(self):  
	20:      self._cost = 3.0  
	21:      self._desc = "Espresso ($" + str(self._cost)+ ")"  
	22:    
	23:    
	24:  # Design Pattern   
	25:  # Abstract Decorator  
	26:  class Condiments(Beverage):  
	27:    def __init__(self):  
	28:      self._desc = "Abstract Condiments class"  
	29:      self._cost_condiment = 0.0      
	30:      
	31:  class Mocha(Condiments):  
	32:    def __init__(self, beverage):  
	33:      self._cost_condiment = 1.0  
	34:      self._beverage = beverage;      
	35:      self._desc = "Mocha($"+ str(self._cost_condiment)+ ") " + self._beverage.get_desc()   
	36:      self._cost = self._cost_condiment + self._beverage.get_cost()   
	37:        
	38:  class Vanilla(Condiments):  
	39:    def __init__(self, beverage):  
	40:      self._cost_condiment = 0.6  
	41:      self._beverage = beverage;      
	42:      self._desc = "Vanilla($"+ str(self._cost_condiment)+ ") " + self._beverage.get_desc()   
	43:      self._cost = 0.6 + self._beverage.get_cost()   
	44:           
	45:    
	46:  class WhipCream(Condiments):  
	47:    def __init__(self,beverage):  
	48:      self._cost_condiment = 0.4  
	49:      self._beverage = beverage;      
	50:      self._desc = "WhipCream($"+ str(self._cost_condiment)+ ") " + self._beverage.get_desc()   
	51:      self._cost = 0.4 + self._beverage.get_cost()   
	52:        
	53:  ########################################################################################3    
	54:    
	55:    
	56:  b = DarkRoast()  
	57:  print(b.get_desc(), "Cost is", b.get_cost())      
	58:    
	59:  b = Mocha(DarkRoast())  
	60:  print(b.get_desc(), "Cost is", b.get_cost())    
	61:    
	62:  b = Mocha(Espresso())  
	63:  print(b.get_desc(), "Cost is", b.get_cost())    
	64:    
	65:  b = Vanilla(DarkRoast())  
	66:  print(b.get_desc(), "Cost is", b.get_cost())   
	67:    
	68:  b = Vanilla(Mocha(DarkRoast()))  
	69:  print(b.get_desc(), "Cost is", b.get_cost())   
	70:    
	71:  b = WhipCream(Mocha(DarkRoast()))  
	72:  print(b.get_desc(), "Cost is", b.get_cost())   
	73:    
	74:    
	75:  b = Vanilla(WhipCream(Mocha(DarkRoast())))  
	76:  print(b.get_desc(), "Cost is", b.get_cost())   