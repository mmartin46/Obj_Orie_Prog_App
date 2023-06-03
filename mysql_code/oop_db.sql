/*
Mitchell Brian Martin
06/01/2023

Design Patterns

The follwing database shows the Java
Deisgn Patterns which are seperated
by the type of pattern.

*/


DROP DATABASE oop_methods;
CREATE DATABASE oop_methods;
USE oop_methods;

CREATE TABLE design_patterns(
	m_name			VARCHAR(30) PRIMARY KEY,
	m_type			VARCHAR(20) UNIQUE
);

INSERT INTO design_patterns VALUES
	('Creational Design Pattern', 'CREATIONAL'),
	('Structural Design Pattern', 'STRUCTURAL'),
	('Behavioral Design Pattern', 'BEHAVIORAL');
	
CREATE TABLE all_patterns(
	p_name			VARCHAR(40) PRIMARY KEY,
	p_desc			VARCHAR(1000),
	m_type			VARCHAR(20),
	FOREIGN KEY(m_type) REFERENCES design_patterns(m_type)
);

INSERT INTO all_patterns VALUES
	('Singleton Design Pattern', 'The Singleton Pattern defines a class that has only one instance a provides a global point of access to it.', 'CREATIONAL'),
	('Prototype Pattern', 'The Prototype Pattern consists of cloning an existing object instead of creating a new class anc customized with the requirement', 'CREATIONAL'),
	('Builder Pattern', 'The Builder Design Pattern consists of constructing a complex object from simple objects using an incremental approach.', 'CREATIONAL'),
	('Object Pool Pattern', "The Object Pool Pattern says to reuse the object that's expensive to create", 'CREATIONAL');
	
INSERT INTO all_patterns VALUES
	('Adapter Pattern', 'The Adapter Pattern consists of converting the interface of a class to another interface a client wants', 'STRUCTURAL'),
	('Bridge Pattern', 'The Bridge Pattern says to decouple he functional abstraction from the implementation so that they may vary independently', 'STRUCTURAL'),
	('Composite Pattern', 'The Composie Pattern consists of allowing clients to operate in a general manner on objects. (May/may not represent a hierachy of objects)', 'STRUCTURAL'),
	('Decorator Pattern', 'The Decorator Pattern consists of attach a flexible additional responsibilities to an object dynamically.', 'STRUCTURAL'),
	('Facade Pattern', 'The Facade Pattern consists of providing a simplified interface to a set of interfaces in a subsystem, therefore it abstracts the subsystem from the client.', 'STRUCTURAL'),
	('Flyweight Pattern', "The Flyweight Pattern consists of reusing existing related objects by storing them and create a new object when a matching object doesn't exist", 'STRUCTURAL'),
	('Proxy Pattern', 'The Proxy Pattern consists of providing the control for accessing the original object.', 'STRUCTURAL');

INSERT INTO all_patterns VALUES
	('Chain Of Responsibility Pattern', 'The Chain of Responsibility Pattern suggests to avoid coupling the sender of a request to its receiver by giving multiple objects a chance to handle the request', 'BEHAVIORAL'),
	('Command Pattern', 'The Command Pattern consists of encapsulating a request under an object as a command and pass it to an invoker object', 'BEHAVIORAL'),
	('Interpreter Pattern', 'The Inerpreter Pattern consists of a representation of grammar of a given language, along with an interpreter to interpre sentences in the language', 'BEHAVIORAL'),
	('Iterator Pattern', 'The Iterator Pattern is used to access elements of an aggregate object sequentially without exposiing its implementation', 'BEHAVIORAL'),
	('Mediator Pattern', 'The Mediator Pattern consists of defining how a set of objects interact with each other', 'BEHAVIORAL'),
	('Memento Pattern', 'The Memento Pattern says to restore he state of an object to is previous state and avoid Encapsulation.', 'BEHAVIORAL'),
	('Observer Pattern', 'The Observer Pattern consists of defining a one-to-one dependency so that if an object changes state, all the depndents are updated and notified automatically.', 'BEHAVIORAL'),
	('State Pattern', 'The State Pattern claims the class behavior changes based on its state.', 'BEHAVIORAL'),
	('Strategy Pattern', 'The State Pattern consists of a family of functionality, encapsulating each one and making them interchangable', 'BEHAVIORAL'),
	('Template Pattern', 'The Template Pattern says to define the skeleion of a function in an operation, deferring some subclasses.', 'BEHAVIORAL');

/* Returns the description. */
CREATE PROCEDURE getDescription(IN descr VARCHAR(60))
BEGIN
	SELECT p_desc FROM all_patterns
	WHERE p_name LIKE descr;
END;

CALL getDescription('Singleton Design Pattern');

/* Returns all patterns based on the type. */
CREATE PROCEDURE designPattern(IN patt VARCHAR(60))
BEGIN
	SELECT all_patterns.* FROM design_patterns
	INNER JOIN all_patterns ON design_patterns.m_type = all_patterns.m_type
	WHERE design_patterns.m_type = 'STRUCTURAL';
END;



