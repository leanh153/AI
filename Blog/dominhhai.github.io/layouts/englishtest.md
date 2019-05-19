1 The Worlds of Database Systems
1.1 The Evolution of Database Systems
1.1.1 Early Database Management Systems
1.1.2 Relational Database Systems
1.1.3 Smaller and Smaller Systems
1.1.4 Bigger and Bigger Systems
1.1.5 Client-Server and Multi-Tier Architectures
1.1.6 Multimedia Data
1.1.7 Information Integration
1.2 Overview of a Database Management System
1.2.1 Data-Definition Language Commands
1.2.2 Overview of Query Processing
1.2.3 Storage and Buffer Management
1.2.4 Transaction Processing
1.2.5 The Query Processor
1.3 Outline of Database-System Studies
1.3.1 Database Design
1.3.2 Database Programming
1.3.3 Database System Implementation
1.3.4 Information Integration Overview
1.4 Summary of Chapter 1
1.5 References for Chapter
2 The Entity-Relationship Data Model
2.1 Elements of the E/R model
2.1.1 Entity Sets
2.1.10 Converting Multiway Relationships to Binary
2.1.11 Subclasses in the E/R, model
2.1.12 Exercises for Section 2
2.1.2 Attributes
2.1.3 Relationships
2.1.4 Entity-Relationship Diagrams
2.1.5 Instances of an E/R Diagram
2.1.6 multiplicity of Binary E/R Relations
2.1.7 multiple way Relationships
2.1.8 Roles in Relationships
2.1.9 Attributes on Relationships
2.2 Design Principles
2.2.1 Faithfulness
2.2.2 Avoiding Redundancy
2.2.3 Simplicity Counts
2.2.4 Choosing the Right Relationships
2.2.5 Picking the Right Kind of Element
2.2.6 Exercises for Section 2
2.3 The Modeling of Constraints
2.3.1 Classification of Constraints
2.3.2 Keys in the E/R Model
2.3.3 Representing Keys in the E/R Model
2.3.4 Single-Value Constraints
2.3.5 Referential Integrity
2.3.6 Referential Integrity in E/R Diagrams
2.3.7 Other Kinds of Constraints
2.3.8 Exercises for Section 2
2.4 Weak Entity Sets
2.4.1 Causes of Weak Entity Sets
2.4.2 Requirements for Weak Entity Sets
2.4.3 Weak Entity Set Notation
2.4.4 Exercises for Section 2
2.5 Summary of Chapter
2.6 References for Chapter
3 The Relational Data Model
3.1 Basics of the Relational Model
3.1.1 Attributes
3.1.2 Schemas
3.1.3 Tuples
3.1.4 Domains
3.1.5 Equivalent Representations of a Relation
3.1.6 Relation Instances
3.1.7 Exercises for Section 3
3.2 From E/R Diagrams to Relational Designs
3.2.1 Fro~nEntity Sets to Relations
3.2.2 From E/R Relationshipsto Relations
3.2.3 Combining Relations
3.2.4 Handling Weak Entity Sets
3.2.5 Exercises for Section 3
3.3 Converting Subclass Structures to Relations
3.3.1 E/R-Style Conversion
3.3.2 An Object-Oriented Approach
3.3.3 Using Null Values to Combine Relations
3.3.4 Comparison of Approaches
3.3.5 Exercises for Section 3
3.4 Functional Dependencies
3.4.1 Definition of Functional Dependency
3.4.2 Keys of Relations
3.4.3 Superkeys
3.4.4 Discovering Keys for Relations
3.4.5 Exercises for Section 3
3.5 Rules About Functional Dependencies
3.5.1 The Splitting/Combi~~ing Rule
3.5.2 Trivial Functional Dependencies
3.5.3 Computing the Closure of Attributes
3.5.4 Why the Closure Algorithm Works
3.5.5 The Transitive Rule
3.5.6 Closing Sets of Functional Dependencies
3.5.7 Projecting Functional Dependencies
3.5.8 Exercises for Section 3
3.6 Design of Relational Database Schemas
3.6.1 Anomalies
3.6.2 Decomposing Relations
3.6.3 Boyce-Codd Normal Form
3.6.4 Decomposition into BCNF
3.6.6 Third normal Form
3.6.7 Exercises for Section 3
3.63 Recovering Information from a Decomposition
3.7 multivalued Dependencies
3.7.1 Attribute Independence and Its Consequent Redundancy
3.7.2 Definition of multi valued Dependencies
3.7.3 Reasoning About multi valued Dependencies
3.7.4 Fourth normal Form
3.7.5 Decomposition into Fourth Normal Form
3.7.6 Relationships Among normal Forms
3.7.7 Exercises for Section 3
3.8 Summary of Chapter
3.9 References for Chapter
4 Other Data Mo
4.1 Review of Object-Oriented Concepts
4.1.2 Classes and Objects
4.1.3 Object Identity
4.1.4 Methods
4.1.5 Class Hierarchies
4.11 The Type System
4.2 Introduction to ODL
4.2.1 Object-Oriented Design
4.2.2 Class Declarations
4.2.3 Attributes in ODL
4.2.4 Relationships in ODL
4.2.5 Inverse Relationships
4.2.6 multiplicity of Relationships
4.2.7 Methods in ODL
4.2.8 Types in ODL
4.2.9 Exercises for Section 4
4.3 Additional ODL Concepts
4.3.1 Multiway Relationships in ODL
4.3.2 Subclasses in ODL
4.3.3 Multiple Inheritance in ODL
4.3.4 Extents
4.3.5 Declaring Keys in ODL
4.3.6 Exercises for Section 4
4.4 From ODL Designs to Relational Designs
4.4.1 From ODL Attributes to Relational Attributes
4.4.2 Nonatomic Attributes in Classes
4.4.3 Representing Set-Valued Attributes
4.4.4 Representing Other Type Constructors
4.4.5 Representing ODL Relationships
4.4.6 What If There Is No Key
4.4.7 Exercises for Section 4
4.5 The Object-Relational Model
4.5.1 From Relations to Object-Relations
4.5.2 Nested Relations
4.5.3 References
4.5.4 Object-Oriented Versus Object-Relational
4.5.5 From ODL Designs to Object-Relational Designs
4.5.6 Exercises for Section 4
4.6 Semi structured Data
4.6.1 Motivation for the Semis tructured-Data Model
4.6.2 Semistructured Data Representation
4.6.3 Information Integration Via Semistructured Data
4.6.4 Exercises for Section 4
4.7 XML and Its Data Model
4.7.1 Semantic Tags
4.7.2 Well-Formed X1.iL
4.7.3 Document Type Definitions
4.7.4 Using a DTD
4.7.5 attribute Lists
4.7.6 Exercises for Section 4
4.8 Summary of Chapter
4.9 References for Chapter
5 Relational Algebra
5.1 An Example Database Schema
5.2 .. An Algebra " of Relational Operations
5.2.1 Basics of Relational Algebra
5.2.10 Dependent and Independent Operations
5.2.11 A Linear Notation for Algebraic Expressions
5.2.12 Exercises for Section 5
5.2.2 Set Operations on Relations
5.2.3 Projection
5.2.4 Selection
5.2.5 Cartesian Product
5.2.6 Natural Joins
5.2.7 Theta-Joins
5.2.8 Combining Operations to Form Queries
5.2.9 Renaming
5.3 6 Joins of Bags
5.3 Relational Operations on Bags
5.3.1 Why Bags
5.3.2 Union, Intersection, and Difference of Bags
5.3.3 Projection of Bags
5.3.4 Selection on Bags
5.3.5 Product of Bags
5.3.7 Exercises for Section 5
5.4 Exercises for Section G
5.4 Extended Operators of Relational Algebra
5.4.1 Duplicate Elimination
5.4.2 Aggregation Operators
5.4.3 Grouping
5.4.4 The Grouping Operator
5.4.5 Extending the Projection Operator
5.4.6 The Sorting Operator
5.4.7 Outerjoins
5.4.8 Exercises for Section 5
5.5 Constraints on Relations
5.5.1 Relational .Algebra as a Constraint Language
5.5.2 Referential Integrity Constraints
5.5.3 Additional Constraint Examples
5.5.4 Exercises for Section 5
5.6 Summary of Chapter
5.7 References for Chapter
6 The Database Language
6.1 Simple Queries in SQL
6.1.1 Projection in SQL
6.1.2 Selection in SQL
6.1.3 Comparison of Strings
6.1.4 Dates and Times
6.1.5 Null Values and Comparisons Involving NULL
6.1.6 The Truth-Value UNKNOWN
6.1.7 Ordering the Output
6.1.8 Exercises for Section 6
6.2 Queries Involving More Than One Relation
6.2.1 Products and Joins in SQL
6.2.2 Disambiguating Attributes
6.2.3 Tuple Variables
6.2.4 Interpreting Multirelation Queries
6.2.5 Union, Intersection, and Difference of Queries
6.2.6 Exercises for Section 6
6.3 Subqueries
6.3.1 Subqueries that Produce Scalar Values
6.3.2 Conditions Involving Relations
6.3.3 Conditions Involving Tuples
6.3.4 Correlated Subqueries
6.3.5 Subqueries in FROM Clauses
6.3.6 SQL Join Expressions
6.3.7 Xatural Joins
6.3.8 Outerjoins
6.3.9 Exercises for Section 6
6.4 Full-Relation Operations
6.4.1 Eliminating Duplicates
6.4.2 Duplicates in Unions, Intersections, and Differences
6.4.3 Grouping and Aggregation in SQL
6.4.4 Aggregation Operators
6.4.5 Grouping
6.4.6 HAVING Clauses
6.4.7 Exercises for Section 6
6.5 Database modifications
6.5.1 Insertion
6.5.2 Deletion
6.5.3 Updates
6.6 Defining a Relation Schema in SQL
6.6.1 Data Types
6.6.2 Simple Table Declarations
6.6.3 Modifying Relation Schemas
6.6.4 Default Values
6.6.5 Indexes
6.6.6 Introduction to Selection of Indexes
6.6.7 Exercises for Section 6
6.7 View Definitions
6.7.1 Declaring Views
6.7.2 Querying Views
6.7.3 Renaming Attributes
6.7.4 Modifying Views
6.7.5 Interpreting Queries Involving Views
6.7.6 Exercises for Section 6
6.8 Summary of Chapter
6.9 References for Chapter
7 Constraints and Triggers
7.1 Keys and Foreign Keys
7.1.1 Declaring Primary Keys
7.1.2 Keys Declared with UNIQUE
7.1.3 Correct Execution of Transactions
7.1.3 Enforcing Key Constraints
7.1.4 Declaring Foreign-Key Constraints
7.1.5 Maintaining Referential Integrity
7.1.6 Deferring the Checking of Constraints
7.1.7 Exercises for Section 7
7.2 Constraints on Attributes and Tuples
7.2.1 Not-Null Constraints
7.2.2 Attribute-Based CHECK Constraints
7.2.3 Tuple-Based CHECK Constraints
7.2.4 Exercises for Section 7
7.3 modification of Constraints
7.3.1 Giving Names to Constraints
7.3.2 Altering Constraints on Tables
7.3.3 Exercises for Section 7
7.4 Schema-Level Constraints and Triggers
7.4.1 Assertions
7.4.2 Event-Condition- Action Rules
7.4.3 Triggers in SQL
7.4.4 Instead-Of Triggers
7.4.5 Exercises for Section 7
7.5 Summary of Chapter
7.6 References for Chapter
8 System Aspects of SQL
8-27 17.4.4 Exercises for Section 17
8.1 SQL in a Programming Environment
8.1.1 The Impedance Mismatch Problem
8.1.10 Dynamic SQL
8.1.11 Exercises for Section 8
8.1.2 The SQL/Host Language Interface
8.1.3 The DECLARE Section
8.1.4 Using Shared Variables
8.1.5 Single-Row Select Statements
8.1.6 Cursors
8.1.7 Modifications by Cursor
8.1.8 Protecting Against Concurrent Updates
8.1.9 Scrolling Cursors
8.2 Procedures Stored in the Schema
8.2.1 Creating PSM Functions and Procedures
8.2.2 Some Simple Statement Forms in PSM
8.2.3 Branching Statements
8.2.4 Queries in PSM
8.2.5 Loops in PSM
8.2.6 For-Loops
8.2.7 Exceptions in PSM
8.2.8 Using PSM Functions and Procedures
8.2.9 Exercises for Section 8
8.3 The SQL Environment
8.3.1 Environments
8.3.2 Schemas
8.3.3 Catalogs
8.3.3 Cursor Operations in JDBC
8.3.4 Clients and Servers in the SQL Environment
8.3.5 Connections
8.3.6 Sessions
8.3.7 Modules
8.4 Using a Call-Level Interface
8.4.1 Introduction to SQL/CLI
8.4.2 Processing Statements
8.4.3 Fetching Data F'rom a Query Result
8.4.4 Passing Parameters to Queries
8.4.5 Exercises for Section 8
8.5 Java Database Connectivity
8.5.1 Introduction to JDBC
8.5.2 Creating Statements in JDBC
8.5.4 Parameter Passing
8.5.5 Exercises for Section 8
8.6 Transactions in SQL
8.6.1 Serializability
8.6.2 Atomicity
8.6.3 Transactions
8.6.4 Read-only Transactions
8.6.5 Dirty Reads
8.6.6 Other Isolation Levels
8.6.7 Exercises for Section 8
8.7 Security and User Authorization in SQL
8.7.1 Privileges
8.7.2 Creating Privileges
8.7.3 The Privilege-Checking Process
8.7.4 Granting Privileges
8.7.5 Grant Diagrams
8.7.6 Revoking Privileges
8.7.7 Exercises for Section 8
8.8 Summary of Chapter
8.9 References for Chapter
9 Object-Orientation in Query Languages
9.1 Introduction to OQL
9.1.1 An Object-Oriented Movie Example
9.1.2 Path Expressions
9.1.3 Select-From-Where Expressions in OQL
9.1.4 Modifying the Type of the Result
9.1.5 Complex Output Types
9.1.6 Subqueries
9.1.7 Exercises for Section 9
9.2 Additional Forms of OQL Expressions
9.2.1 Quantifier Expressions
9.2.2 Aggregation Expressions
9.2.3 Group-By Expressions
9.2.4 HAVING Clauses
9.2.5 Union, Intersection, and Difference
9.2.6 Exercises for Section 9
9.3 Object Assignment and Creation in OQL
9.3.1 Assigning value to Host-Language variable
9.3.2 Extracting Elements of Collections
9.3.3 Obtaining Each Member of a Collection
9.3.4 Constants in OQL
9.3.5 Creating Sew Objects
9.3.6 Exercises for Section 9
9.4 4 References
9.4 User-Defined Types in SQL
9.4.1 Defining Types in SQL
9.4.2 methods in User-Defined Types
9.4.3 Declaring Relations with a UDT
9.4.5 Exercises for Section 9
9.5 Operations on Object-Relational Data
9.5.1 Following References
9.5.2 Accessing .Attributes of Tuples with a UDT
9.5.3 Generator and Mutator Functions
9.5.4 Ordering Relationships on UDT's
9.5.5 Exercises for Section 9
9.6 Summary of Chapter
9.7 References for Chapter
10 Logical Query Languages
10.1 A Logic for Relations
10.1.1 Predicates and Atoms
10.1.2 Arithmetic Atoms
10.1.3 Datalog Rules and Queries
10.1.4 Meaning of Datalog Rules
10.1.5 Extensional and Intensional Predicates
10.1.6 Datalog Rules Applied to Bags
10.1.7 Exercises for Section 10
10.2 From relational Algebra to Datalog
10.2.1 Intersection
10.2.2 Union
10.2.3 Difference
10.2.4 Projection
10.2.5 Selection
10.2.6 Product
10.2.7 Joins
10.2.8 Simulating multiple Operations with Datalog
10.2.9 Exercises for Section 10
10.3 Recursive Programming in Datalog
10.3.1 Recursive Rules
10.3.2 Evaluating Recursive Datalog Rules
10.3.3 Negation in Recursive Rules
10.3.4 Exercises for Section 10
10.4 Recursion in SQL
10.4.1 Defining IDB Relations in SQL
10.4.2 Stratified Negation
10.4.3 Problematic Expressions in Recursive SQL
10.4.4 Exercises for Section 10
10.5 Summary of Chapter
10.6 References for Chapter
11 Data Storage
11.1 The "Megatron 2OOZ" Database System
11.1.1 hlegatron 2002 Implenlentation Details
11.1.2 How LIegatron 2002 Executes Queries
11.1.3 What's Wrong With hiegatron 2002
11.2 The Memory Hierarchy
11.2.1 Cache
11.2.2 Lookup in a Grid File
11.2.2 Main memory
11.2.3 virtual Memory
11.2.4 Secondary Storage
11.2.5 Tertiary Storage
11.2.6 Volatile and Nonvolatile Storage
11.2.7 Exercises for Section 11
11.3 Disks
11.3.1 mechanics of Disks
11.3.2 The Disk Controller
11.3.3 Disk Storage Characteristics
11.3.4 Disk Access Characteristics
11.3.5 Writing Blocks
11.3.6 Modifying Blocks
11.3.7 Exercises for Section 11
11.4 Using Secondary Storage Effectively
11.4.1 The I f 0 Model of Computation
11.4.2 Sorting Data in Secondary Storage
11.4.3 Merge-Sort
11.4.4 Two-Phase, Multiway merge-Sort
11.4.5 multiway Merging of Larger Relations
11.4.6 Exercises for Section 11
11.5 Accelerating Access to Secondary Storage
11.5.1 Organizing Data by Cylinders
11.5.2 Using llultiple Disks
11.5.3 Mirroring Disks
11.5.4 Disk Scheduling and the Elevator Algorithm
11.5.5 Prefetching and Large-Scale Buffering
11.5.6 Summary of Strategies and Tradeoffs
11.5.7 Exercises for Section 11
11.6 Disk Failures
11.6.1 Intermittent Failures
11.6.2 Checksums
11.6.3 Stable Storage
11.6.4 Error-Handling Capabilities of Stable Storage
11.6.5 Exercises for Section 11
11.7 Recorery from Disk Crashes
11.7.1 The Failure Model for Disks
11.7.2 mirroring as a Redundancy Technique
11.7.3 Parity Blocks
11.7.4 An Improvement: RAID
11.7.5 Coping With Multiple Disk Crashes
11.7.6 Exercises for Section 11
11.8 Summary of Chapter
11.9 References for Chapter
12 Representing Data Elements
12.1 Data Elements and Fi
12.1.1 Representing Relational Database Elements
12.1.2 Representing Objects
12.1.3 Representing Data Elements
12.2 Records
12.2.1 Building Fixed-Length Records
12.2.2 Record Headers
12.2.3 Packing Fixed-Length Records into Blocks
12.2.4 Exercises for Section
12.3 Representing Block and Record Addresses
12.3.1 Client-Server Systems
12.3.2 Logical and Structured Addresses
12.3.3 Pointer Swizzling
12.3.4 Returning Blocks to Disk
12.3.5 Pinned Records and Blocks
12.3.6 Exercises for Section
12.4 Variable-Length Data and Records
12.4.1 Records With Variable-Length Fields
12.4.2 Records With Repeating Fields
12.4.3 Variable-Format Records
12.4.4 Records That Do Not Fit in a Block
12.4.5 BLOBS
12.4.6 Exercises for Section 12
12.5 Record Modifications
12.5.1 Insertion
12.5.2 Deletion
12.5.3 Update
12.5.4 Exercises for Section 12
12.6 Summary of Chapter
12.7 References for Chapter
13 Index Struct
13.1 Indexes on Sequential Files
13.1.1 Sequential Files
13.1.2 Dense Indexes
13.1.3 Sparse Indexes
13.1.4 Multiple Levels of Index
13.1.5 Indexes With Duplicate Search Keys
13.1.6 Managing Indexes During Data modifications
13.1.7 Exercises for Section
13.2 Secondary Indexes
13.2.1 Design of Secondary Indexes
13.2.2 .Applications of Secondary Indexes
13.2.3 Indirection in Secondary Indexes
13.2.4 Document Retrieval and Inverted Indexes
13.2.5 Exercises for Section 13
13.3 B-Trees
13.3.1 The Structure of B-trees
13.3.2 Applications of B-trees
13.3.3 Lookup in B-Trees
13.3.4 Range Queries
13.3.5 Insertion Into B-Trees
13.3.6 Deletion From B-Trees
13.3.7 Efficiency of B-Trees
13.3.8 Exercises for Section 13
13.4 Hash Tables
13.4.1 Secondary-Storage Hash Tables
13.4.2 Insertion Into a Hash Table
13.4.3 Hash-Table Deletion
13.4.4 Efficiency of Hash Table Indexes
13.4.5 Extensible Hash Tables
13.4.6 Insertion Into Extensible Hash Tables
13.4.7 Linear Hash Tables
13.4.8 Insertion Into Linear Hash Tables
13.4.9 Exercises for Section 13
13.5 Summary of Chapter
13.6 References for Chapter
14 Multidimensional and Bitmap Indexes
14.1 -4pplicationsXeeding klultiple Dimensio~ls
14.1.1 Geographic Information Systems
14.1.2 Data Cubes
14.1.3 I\lultidimensional Queries in SQL
14.1.4 Executing Range Queries Using Conventional Indexes
14.1.5 Executing Nearest-Xeighbor Queries Using Conventi
14.1.6 Other Limitations of Conventional Indexes
14.1.7 Overview of Multidimensional Index Structures
14.1.8 Exercises for Section 14
14.2 Hash-Like Structures for Multidimensional Data
14.2.1 Grid Files
14.2.3 Insertion Into Grid Files
14.2.4 Performance of Grid Files
14.2.5 Partitioned Hash Functions
14.2.6 Comparison of Grid Files and Partitioned Hashing
14.2.7 Exercises for Section 14
14.3 Tree-Like Structures for multidimensional Data
14.3.1 Multiple-Key Indexes
14.3.2 Performance of Multiple-Key Indexes
14.3.3 kd-Trees
14.3.4 Operations on kd-Trees
14.3.5 .adapting kd-Trees to Secondary Storage
14.3.6 Quad Trees
14.3.7 R-Trees
14.3.8 Operations on R-trees
14.3.9 Exercises for Section 14
14.4 Bitmap Indexes
14.4.1 Motivation for Bitmap Indexes
14.4.2 Compressed Bitmaps
14.4.3 Operating on Run-Length-Encoded Bit-Vectors
14.4.4 Managing Bitmap Indexes
14.4.5 Exercises for Section 14
14.5 Summary of Chapter
14.6 References for Chapter
15 Query Execution
15.1 Introduction to Physical-Query-Plan Operators
15.1.1 Scanning Tables
15.1.2 Sorting While Scanning Tables
15.1.3 The Model of Computation for Physical Operators
15.1.4 Parameters for Measuring Costs
15.1.5 I/O Cost for Scan Operators
15.1.6 Iterators for Implementation of Physical Operators
15.10 Summary of Chapter
15.11 References for Chapter
15.2 One-Pass Algorithms for Database Operations
15.2.1 One-Pass Algorithms for Tuple-at-a-Time Operations
15.2.2 One-Pass Algorithms for Unary, Full-Relation Operations
15.2.3 One-Pass Algorithms for Binary Operations
15.2.4 Exercises for Section 15
15.3 Nested-loop Joins
15.3.1 Tuple-Based Nested-Loop Join
15.3.2 An Iterator for Tuple-Based Nested-Loop Join
15.3.3 A Block-Based Nested-Loop Join Algorithm
15.3.4 Analysis of Nested-Loop Join
15.3.5 Summary of Algorithms so Far
15.3.6 Exercises for Section 15
15.4 Two-Pass Algorithms Based on Sorting
15.4.1 Duplicate Elimination Using Sorting
15.4.2 Grouping and -Aggregation Using Sorting
15.4.3 A Sort-Based Union .algorithm
15.4.4 Sort-Based Intersection and Difference
15.4.5 A Simple Sort-Based Join Algorithm
15.4.6 Analysis of Simple Sort-Join
15.4.7 A More Efficient Sort-Based Join
15.4.8 Summary of Sort-Based Algorithms
15.4.9 Exercises for Section 15
15.5 Two-Pass Algorithms Based on Hashing
15.5.1 Partitioning Relations by Hashing
15.5.2 A Hash-Based Algorithm for Duplicate Elimination
15.5.3 Hash-Based Grouping and Aggregation
15.5.4 Hash-Based Union, Intersection, and Difference
15.5.5 Exercises for Section 15
15.5.5 The Hash-Join Algorithm
15.5.6 Saving Some Disk I/O's
15.5.7 Summary of Hash-Based Algorithms
15.5.8 Exercises for Section 15
15.6 Index-Based Algorithms
15.6.1 Clustering and Non-clustering Indexes
15.6.2 Index-Based Selection
15.6.3 Joining by Using an Index
15.6.4 Joins Using a Sorted Index
15.6.5 Exercises for Section 15
15.7 Buffer Management
15.7.1 Buffer management Architecture
15.7.2 Buffer Management Strategies
15.7.3 The Relationship Between Physical Operator Selection and buffer management
15.7.4 Exercises for Section 15
15.8 Algorithms Using More Than Two Passes
15.8.1 Multipass Sort-Based Algorithms
15.8.2 Performance of multipass, Sort-Based Algorithms
15.8.3 Multipass Hash-Based Algorithms
15.8.4 Performance of Multipass Hash-Based Algorithms
15.9 Parallel Algorithms for Relational Operations
15.9.1 models of Parallelism
15.9.2 Tuple-at-a-Time Operations in Parallel
15.9.3 Parallel Algorithms for Full-Relation Operations
15.9.4 Performance of Parallel Algorithms
15.9.5 Exercises for Section 15
16 The Query Compiler
16.1 Parsing
16.1.1 Syntax .Analysis and Parse Trees
16.1.2 A Grammar for a Simple Subset of SQL
16.1.3 The Preprocessor
16.1.4 Exercises for Section 16.1
16.2 Algebraic Laws for Improving Query Plans
16.2.1 Commutative and Associative Laws
16.2.2 Laws Involving Selection
16.2.3 Pushing Selections
16.2.4 Laws Involving Projection
16.2.5 Laws About Joins and Products
16.2.6 Laws Involving Duplicate Elimination
16.2.7 Laws Involving Grouping and Aggregation
16.2.8 Exercises for Section 16
16.3 From Parse Bees to Logical Query Plans
16.3.1 Conversion to Relational Algebra
16.3.2 Removing Subqueries From Conditions
16.3.3 Improving the Logical Query Plan
16.3.4 Grouping Associative/Commutative Operators
16.3.5 Exercises for Section 16.3
16.4 Estimating the Cost of Operations
16.4.1 Estimating Sizes of Intermediate Relations
16.4.2 Estimating the Size of a Projection
16.4.3 Estimating the Size of a Selection
16.4.4 Estimating the Size of a Join
16.4.5 Natural Joins With Multiple Join Attributes
16.4.6 Joins of Many Relations
16.4.7 Estimating Sizes for Other Operations
16.4.8 Exercises for Section 16.4
16.5 Introduction to Cost-Based Plan Selection
16.5.1 Obtaining Estimates for Size Parameters
16.5.2 Computation of Statistics
16.5.3 Heuristics for Reducing the Cost of Logical Query Plans
16.5.4 Approaches to Enumerating Physical Plans
16.5.5 Exercises for Section 16
16.6 Choosing an Order for Joins
16.6.1 Significance of Left and Right Join Arguments
16.6.2 Join Trees
16.6.3 Left-Deep Join Trees
16.6.4 Dynamic Programming to Select a Join Order and Grouping
16.6.5 Dynamic Programming With More Detailed Cost Functions
16.6.6 A Greedy Algorithm for Selecting a Join Order
16.6.7 Exercises for Section 16.6
16.7 Completing the Physical-Query-Plan
16.7.1 Choosing a Selection Method
16.7.2 Choosing a Join Method
16.7.3 Pipelining Versus Materialization
16.7.4 Pipelining Unary Operations
16.7.5 Pipelining Binary Operations
16.7.6 Notation for Physical Query Plans
16.7.7 Ordering of Physical Operations
16.7.8 Exercises for Section 16
16.8 Summary of Chapter
16.9 References for Chapter
17 Coping W i t h System Failures
17..5 Protecting Against Media Failures
17.1. Issues and Models for Resilient Operation
17.1.1 Failure Modes
17.1.2 More About Transactions
17.1.4 The Primitive Operations of Transactions
17.1.5 Exercises for Section 17
17.2 Undo Logging
17.2.1 Log Records
17.2.2 The Undo-Logging Rules
17.2.3 Recovery Using Undo Logging
17.2.4 Checkpointing
17.2.5 Nonquiescent Checkpointing
17.2.6 Exercises for Section 17
17.3 Redo Logging
17.3.1 The Redo-Logging Rule
17.3.2 Recovery With Redo Logging
17.3.3 Checkpointing Redo Log
17.3.4 Recovery With a Checkpointed Redo Log
17.3.5 Exercises for Section 17
17.4 Undo/Redo Logging
17.4.1 The Undo/Redo Rules
17.4.2 Recovery With Undo/Redo Logging
17.4.3 Checkpointing an Undo/Redo Log
17.5.1 The Archive
17.5.2 Nonquiescent Archiving
17.5.3 Recovery Using an Archive and Log
17.5.4 Exercises for Section 17
17.6 Summary of Chapter
17.7 References for Chapter
18 Concurrency Control
18.1 Serial and Serializable Schedules
18.1.1 Schedules
18.1.2 Serial Schedules
18.1.3 Serializable Schedules
18.1.4 The Effect of Transaction Semantics
18.1.5 A Notation for Transactions and Schedules
18.1.6 Exercises for Section 18
18.10 Summary of Chapter
18.11 References for Chapter
18.2 Conflict-Seridiability
18.2.1 Conflicts
18.2.2 Precedence Graphs and a Test for Conflict-Serializability
18.2.3 Why the Precedence-Graph Test Works
18.2.4 Exercises for Section 18
18.3 Enforcing Serializability by Locks
18.3.1 Locks
18.3.2 The Locking Scheduler
18.3.3 Two-Phase Locking
18.3.4 Why Two-Phase Locking Works
18.3.5 Exercises for Section 18
18.4 Locking Systems With Several Lock hlodes
18.4.1 Shared and Exclusive Locks
18.4.2 Compatibility Matrices
18.4.3 Upgrading Locks
18.4.4 Update Locks
18.4.5 Increment Locks
18.4.6 Exercises for Section 18
18.5 An Architecture for a Locking Scheduler
18.5.1 A Scheduler That Inserts Lock Actions
18.5.2 The Lock Table
18.5.3 Exercises for Section 18
18.6 managing Hierarchies of Database Elements
18.6.1 Locks With Multiple Granularity
18.6.2 Warning Locks
18.6.3 Phantoms and Handling Insertions Correctly
18.6.4 Exercises for Section 18
18.7 The Tree Protocol
18.7.1 Motivation for Tree-Based Locking
18.7.2 Rules for Access to Tree-Structured Data
18.7.3 Why the Tree Protocol Works
18.7.4 Exercises for Section 18
18.8 Concurrency Control by Timestamps
18.8.1 Timestamps
18.8.2 Physically unrealizable Behaviors
18.8.3 Problems Kith Dirty Data
18.8.4 The Rules for Timestamp-Based Scheduling
18.8.5 multiversion Timestamps
18.8.6 Timestamps and Locking
18.8.7 Exercises for Section 18
18.9 Concurrency Control by Validation
18.9.1 Architecture of a Validation-Based Scheduler
18.9.2 The Validation Rules
18.9.3 Comparison of Three Concurrency-Control mechanisms
18.9.4 Exercises for Section 18
19 More About Transaction Management
19.1 Serializability and Recoverability
19.1.1 The Dirty-Data Problem
19.1.2 Cascading Rollback
19.1.3 Exercises for Section 19
19.1.3 Recoverable Schedules
19.1.4 Schedules That Avoid Cascading Rollback
19.1.5 managing Rollbacks Using Locking
19.1.6 Group Commit
19.1.7 Logical Logging
19.1.8 Recovery From Logical Logs
19.1.9 Exercises for Section 19
19.2 View Serializability
19.2.1 View Equivalence
19.2.2 Polygraphs and the Test for View-Serializability
19.2.3 Testing for View-Serializability
19.2.4 Exercises for Section 19
19.3 Resolving Deadlocks
19.3.1 Deadlock Detection by Timeout
19.3.2 The IVaits-For Graph
19.3.3 Deadlock Prevention by Ordering Elements
19.3.4 Detecting Deadlocks by Timestamps
19.3.5 Comparison of Deadlock-management Methods
19.3.6 Exercises for Section 19
19.4 Distributed Databases
19.4.1 Distribution of Data
19.4.2 Distributed Transactions
19.4.3 Data Replication
19.4.4 Distributed Query Optimization
19.5 Distributed Commit
19.5.1 Supporting Distributed Atomicity
19.5.2 Two-Phase Commit
19.5.3 Recovery of Distributed Transactions
19.5.4 Exercises for Section 19
19.6 Distributed Locking
19.6.1 Centralized Lock Systems
19.6.2 A Cost Model for Distributed Locking Algorithms
19.6.3 Locking Replicated Elements
19.6.4 Primary-Copy Locking
19.6.5 Global Locks From Local Locks
19.6.6 Exercises for Section 19
19.7 Long-Duration transactions
19.7.1 Problems of Long Transactions
19.7.2 Sagas
19.7.3 Compensating Transactions
19.7.4 Why Compensating Transactions Work
19.7.5 Exercises for Section 19
19.8 Summary of Chapter
19.9 References for Chapter
20 Information integration
20.1 Modes of Information Integration
20.1.1 Problems of Information Integration
20.1.2 Federated Database System
20.1.3 Data Warehouses
20.1.4 Mediators
20.1.5 Exercises for Section 20
20.2 Wrappers in Mediator-Based Systems
20.2.2 20.2.1 Templates for Query Wrapper Generators Patterns
20.2.3 Filters
20.2.4 Other Operations at the Wrapper
20.2.5 Exercises for Section 20
20.3 Capability-Based Optimization in Mediators
20.3.1 The Problem of Limited Source Capabilities
20.3.2 A Notation for Describing Source Capabilities
20.3.3 Capability-Based Query-Plan Selection
20.3.4 Adding Cost-Based Optimization
20.3.5 Exercises for Section 20
20.4 On-Line Analytic Processing
20.4.1 Exercises OLAP Applications for Section 20
20.4.2 a multidimensional View of OLAP Data
20.4.3 Star Schemas
20.4.4 Slicing and Dicing
20.4.5 Exercises for Section 20
20.5 Data Cubes
20.5.1 The Cube Operator
20.5.2 Cube Implementation by Materialized Views
20.5.3 The Lattice of Views
20.5.4 Exercises for Section 20
20.6 Data Mining
20.6.1 Data-Mining Applications
20.6.2 Finding Frequent Sets of Items
20.6.3 The -2-Priori Algorithm
20.6.4 Exercises for Section 20
20.7 Summary of Chapter
20.8 References for Chapter
