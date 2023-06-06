import mysql.connector
from mysql.connector.locales.eng import client_error
from mysql.connector import Error

import os
db_pass = os.environ.get('db_pass')


class Database():
   def __init__(self):
      self.mydb = mysql.connector.connect(
         host = "127.0.0.1",
         user = "root",
         passwd = db_pass,
         database = "oop_methods"
      )
      
      self.c = self.mydb.cursor()
      
   def get_query(self, query):
      self.c.execute(query)
      query = self.c.fetchall()
      query = str(query).replace("(", "").replace(")", "")
      query = query.replace("[", "").replace("]", "").replace("'", "")
      return query.rstrip(query[-1])










class Java_Descriptions(object):
   """Handles the Java Main Design Descriptions"""
   def __init__(self):
      self.design_patterns = ['Creational Design Pattern', 'Structural Design Pattern', 'Behavioral Design Pattern']

   def java_design_desc(self):
      """Returns a description of Java Design Patterns"""
      desc = "In Core Java, there are three types of Java"
      desc += "design patterns."
      return desc
      
   def get_design_patterns(self):
      return self.design_patterns
   
class Creational_Design_Patterns(Java_Descriptions):
   """Handles the Creational Design Patterns"""
   def __init__(self):
      super(Java_Descriptions, self).__init__()
      self.name = 'Creational Design Patterns\n'
   
   def java_design_desc(self):
      """Returns the description of the Creational Design Patterns"""
      desc = "Creational Design Patterns are focused with"
      desc += " the way of creating objects. The design patterns are used when"
      desc += " a decision needs to be made at the time of the instantiation of a class."
      desc += "\nCreation Design Patterns can be further broken into the following patterns."
      return desc
   
   def types_of_patterns(self):
      """Returns the patterns"""
      types='• Factory Method Pattern\n'
      types+='• Abstract Factory Pattern\n'
      types+='• Singleton Pattern\n'
      types+='• Prototype Pattern\n'
      types+='• Builder Pattern\n'
      types+='• Object Pool Pattern\n'
      return types
   
   
   def get_name(self):
      return self.name
   

class Structural_Design_Patterns(Java_Descriptions):
   """Handles the Structural Design Patterns"""
   def __init__(self):
      super(Java_Descriptions, self).__init__()
      self.name = 'Structural Design Patterns'
   
   def java_design_desc(self):
      """Returns the description of the Structural Design Patterns"""
      desc = "Structural design patterns are focused on how"
      desc += " classes and objects can be composed, to form"
      desc += " larger structures. (Simplifies the structure by"
      desc += " identifying the relationships."
      return desc
   
   def types_of_patterns(self):
      """Returns the patterns"""
      types='• Adapter Pattern\n'
      types+='• Bridge Pattern\n'
      types+='• Composite Pattern\n'
      types+='• Decorator Pattern\n'
      types+='• Facade Pattern\n'
      types+='• Flyweight Pattern\n'
      types+='• proxy Pattern'
      return types
   
   def get_name(self):
      return self.name
   
   
   
class Behavioral_Design_Patterns(Java_Descriptions):
   """Handles the Behavioral Design Patterns"""
   def __init__(self):
      super(Java_Descriptions, self).__init__()
      self.name = 'Behavioral Design Patterns'
      
   def java_design_desc(self):
      """Returns the description of Behavioral Design Patterns"""
      desc = "Behavioral design patterns are concerned with the "
      desc += "interaction and responsibility of objects."
      desc += "With structural design patterns, the interaction "
      desc += " between the objects should be in a way they can easily "
      desc += " communicate with each other and be loosely coupled."
      return desc
   
   def types_of_patterns(self):
      """Returns the patterns"""
      types='• Chain of Responsibility Pattern\n'
      types+='• Command Pattern\n'
      types+='• Interpreter Pattern\n'
      types+='• Iterator Pattern\n'
      types+='• Mediator Pattern\n'
      types+='• Memento Pattern\n'
      types+='• Observer Pattern\n'
      types+='• State Pattern\n'
      types+='• Strategy Pattern\n'
      types+='• Template Pattern\n'
      types+='• Visitor Pattern\n'
      types+='• Null Object'      
      return types
   
   def get_name(self):
      return self.name      
      
      
class FactoryDesc(Java_Descriptions):
   """Handles the Factory Method Pattern"""
   def __init__(self):
      super(Java_Descriptions, self).__init__()
      self.name = 'Factory Method Design'
      
   def java_design_desc(self):
      """Returns the description of Factory Design Pattern"""
      desc = "The Factory Method Pattern consists of"
      desc += " an interface or abstract class for "
      desc += "creating an object but the subclasses decide" 
      desc += " decide which class to instantiate."
      return desc
      
class AbstractDesc(Java_Descriptions):
   """Handles the Factory Method Pattern"""
   def __init__(self):
      super(Java_Descriptions, self).__init__()
      self.name = 'Factory Method Design'
      
   def java_design_desc(self):
      """Returns the description of Abstract Factory Pattern"""
      desc = "The Abstract Factory Pattern says that "
      desc += "jus define an interface or abstract class for "
      desc += "creating families or related (or dependent) objects "
      desc += "alhough not specifying their sub-classes."
      return desc
      
class SingletonDesc(Java_Descriptions):
   """Handles the Singleton Pattern"""
   def __init__(self):
      super(Java_Descriptions, self).__init__()
      self.early_instantiation = "Creation of Instance at Load Time"
      self.lazy_instantiation = "Creation of Instance when Required" 
      self.db = Database()
      self.name = self.db.get_query("""SELECT p_name FROM all_patterns WHERE p_name LIKE 'Singleton%'""")
      
   def java_design_desc(self):
      """Returns the description of Singleton Factory Pattern"""
      desc = self.db.get_query("""SELECT p_desc FROM all_patterns WHERE p_name LIKE 'Singleton%'""")
      return desc
   
class PrototypeDesc(Java_Descriptions):
   """Handles the Prototype Design Pattern"""
   def __init__(self):
      super(Java_Descriptions, self).__init__()
      self.db = Database()
      self.name = self.db.get_query("""SELECT p_name FROM all_patterns WHERE p_name LIKE 'Prototype%'""")

   def java_design_desc(self):
      """Returns the description of Prototype Factory Pattern"""
      desc = self.db.get_query("""SELECT p_desc FROM all_patterns WHERE p_name LIKE 'Prototype%'""")
      return desc
   
class BuilderDesc(Java_Descriptions):
   """Handles the Builder Design Pattern"""
   def __init__(self):
      super(Java_Descriptions, self).__init__()
      self.db = Database()
      self.name = self.db.get_query("""SELECT p_name FROM all_patterns WHERE p_name LIKE 'Builder%'""")

   def java_design_desc(self):
      """Returns the description of Builder Factory Pattern"""
      desc = self.db.get_query("""SELECT p_desc FROM all_patterns WHERE p_name LIKE 'Builder%'""")
      return desc
   
class ObjectPoolDesc(Java_Descriptions):
   """Handles the Builder Design Pattern"""
   def __init__(self):
      super(Java_Descriptions, self).__init__()
      self.db = Database()
      self.name = self.db.get_query("""SELECT p_name FROM all_patterns WHERE p_name LIKE 'Object%'""")

   def java_design_desc(self):
      """Returns the description of Builder Factory Pattern"""
      desc = self.db.get_query("""SELECT p_desc FROM all_patterns WHERE p_name LIKE 'Object%'""")
      return desc
   
class GetDesignDesc:
   def __init__(self, typepattern):
      self.db = Database()
      self.tp = typepattern
      s = "SELECT p_name FROM all_patterns WHERE p_name LIKE" + self.tp + ""
      self.name = self.db.get_query(s)

   def java_design_desc(self):
      """Returns the description of Builder Factory Pattern"""
      d = "SELECT p_nae FROM all_patterns WHERE p_name LIKE" + self.tp + ""
      desc = self.db.get_query(d)
      return desc
   
