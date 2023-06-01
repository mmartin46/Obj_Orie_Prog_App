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
	p_name			VARCHAR(30) PRIMARY KEY,
	p_desc			VARCHAR(1000),
	m_type			VARCHAR(20),
	FOREIGN KEY(m_type) REFERENCES design_patterns(m_type)
);

INSERT INTO all_patterns VALUES
	('Singleton Design Patterm', 'The Singleton Pattern defines a class that has only one instance a provides a global point of access to it.', 'CREATIONAL'),
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

INSERT INTO all_patterna VALUES
	('Chain Of Responsibility Pattern', 'The Chain of Responsibility Pattern suggests to avoid coupling the sender of a request to its receiver by giving multiple objects a chance to handle the request', 'BEHAVIORAL'),
	('Command Pattern', 'The Command Pattern consists of encapsulating a request under an object as a command and pass it to an invoker object', 'BEHAVIORAL');


/*
SELECT all_patterns.* FROM design_patterns
INNER JOIN all_patterns ON design_patterns.m_type = all_patterns.m_type
WHERE design_patterns.m_type = 'STRUCTURAL';
*/

