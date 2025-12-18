# Database Final Exam Study Guide
## NYU Intro to Databases - Fall 2025
### Exam: December 18, 2025 | 3:30 PM - 5:30 PM | Room 215, 6 MetroTech

---

## 📋 EXAM LOGISTICS
- **Bring**: NYU ID, Pen (no pencil!), One A4 page of notes (both sides OK), Water bottle
- **Write your Name and NetID** on the top right of your notes page
- **No**: Eating, Pencil, Late arrivals

---

## 📚 TOPIC 1: Introduction to Databases (Slides 1-22)

### What is a Database?
- **Database**: A collection of interrelated data
- **DBMS (Database Management System)**: Software to manage databases
- **Database System** = Database + DBMS + Applications

### Purpose of Database Systems
- **Data redundancy and inconsistency**: Multiple copies of data in different formats
- **Difficulty in accessing data**: Need new programs for each query
- **Data isolation**: Data scattered in various files
- **Integrity problems**: Constraints buried in code
- **Atomicity problems**: Partial updates if system fails
- **Concurrent access anomalies**: Multiple users updating simultaneously
- **Security problems**: Hard to restrict access

### Data Abstraction (Three Levels)
1. **Physical Level**: How data is actually stored
2. **Logical Level**: What data is stored and relationships (schema)
3. **View Level**: Application-specific views for users

### Schema vs Instance
- **Schema**: The logical structure of the database (doesn't change often)
- **Instance**: The actual content/data at a particular time (changes frequently)

### Data Independence
- **Physical Data Independence**: Can change physical storage without changing logical schema
- **Logical Data Independence**: Can change logical schema without changing views

### Data Models
- **Relational Model**: Data stored in tables (relations)
- **Entity-Relationship Model**: Conceptual design tool
- **Object-based Models**: Combine OOP with databases
- **Semi-structured Models**: XML, JSON

### Database Languages
- **DDL (Data Definition Language)**: CREATE, ALTER, DROP
- **DML (Data Manipulation Language)**: SELECT, INSERT, UPDATE, DELETE

---

## 📚 TOPIC 2: Entity-Relationship Model Part 1 (ALL Slides)

### Basic Concepts
- **Entity**: A "thing" distinguishable from other objects
- **Entity Set**: Collection of similar entities
- **Attributes**: Properties that describe entities
- **Relationship**: Association among entities
- **Relationship Set**: Collection of similar relationships

### Attribute Types
- **Simple vs Composite**: Single value vs multiple components (e.g., name → first, last)
- **Single-valued vs Multivalued**: One value vs many (e.g., phone numbers)
- **Derived**: Computed from other attributes (e.g., age from DOB)
- **Null**: Unknown or does not exist

### Keys
- **Super Key**: Set of attributes that uniquely identifies an entity
- **Candidate Key**: Minimal super key
- **Primary Key**: Chosen candidate key (underlined in ER diagrams)

### Mapping Cardinalities
- **One-to-One (1:1)**: Each entity relates to at most one other
- **One-to-Many (1:N)**: One entity relates to many others
- **Many-to-One (N:1)**: Many entities relate to one
- **Many-to-Many (M:N)**: Many relate to many

### Participation Constraints
- **Total Participation** (double line): Every entity must participate
- **Partial Participation** (single line): Some entities may not participate

### ER Diagram Notation
- **Rectangle**: Entity set
- **Diamond**: Relationship set
- **Ellipse**: Attribute
- **Double Ellipse**: Multivalued attribute
- **Dashed Ellipse**: Derived attribute
- **Underline**: Primary key attribute

---

## 📚 TOPIC 3: Relational Model & Relational Algebra (ALL Slides)

### Relational Model Structure
- **Relation**: A table with rows and columns
- **Tuple**: A row in the table
- **Attribute**: A column header
- **Domain**: Set of allowed values for each attribute
- **Relation Schema**: R(A1, A2, ..., An) - describes structure
- **Relation Instance**: Actual rows at a given time

### Keys in Relational Model
- **Superkey**: Set of attributes that uniquely identifies a tuple
- **Candidate Key**: Minimal superkey
- **Primary Key**: Chosen candidate key
- **Foreign Key**: Attribute referencing another table's primary key

### Integrity Constraints
- **Domain Constraints**: Values must be from attribute's domain
- **Referential Integrity**: Foreign keys must reference existing tuples
- **Entity Integrity**: Primary key cannot be NULL

### Relational Algebra Operations (CONCEPTS ONLY - No drawing required)

| Operation | Symbol | Description |
|-----------|--------|-------------|
| Select | σ | Selects rows satisfying condition |
| Project | π | Selects columns |
| Union | ∪ | Combines tuples from two relations |
| Set Difference | - | Tuples in R1 but not R2 |
| Cartesian Product | × | All combinations of tuples |
| Rename | ρ | Renames relation/attributes |
| Natural Join | ⋈ | Combines on common attributes |
| Intersection | ∩ | Tuples in both relations |
| Division | ÷ | "For all" queries |

---

## 📚 TOPIC 4: ER Model Part 2 (Slides 1-8, 19-26, 31-32, 35-36)

### Weak Entity Sets
- Cannot be uniquely identified by own attributes alone
- Must be associated with **identifying/owner entity** (strong entity)
- Uses **discriminator** (partial key) - dashed underline
- **Double rectangle** for weak entity
- **Double diamond** for identifying relationship
- Always has **total participation** in identifying relationship

### Specialization (Top-Down)
- Subclass inherits attributes from superclass
- **Overlapping**: Entity can belong to multiple subclasses
- **Disjoint**: Entity belongs to only one subclass
- **Total**: Every entity must be in some subclass
- **Partial**: Not all entities are in subclasses

### Generalization (Bottom-Up)
- Combine similar entity sets into a higher-level entity set
- Opposite direction of specialization

### Aggregation
- Treating a relationship as a higher-level entity
- Used when we need relationships with relationships

---

## 📚 TOPIC 5: Basic SQL Part 1 (ALL Slides) ⭐ HIGH PRIORITY

### SQL Data Types
```sql
CHAR(n)       -- Fixed-length string
VARCHAR(n)    -- Variable-length string  
INT / INTEGER -- Integer
NUMERIC(p,d)  -- Fixed-point (p digits, d after decimal)
REAL, DOUBLE  -- Floating point
DATE          -- 'YYYY-MM-DD'
TIME          -- 'HH:MM:SS'
TIMESTAMP     -- Date + Time
```

### DDL Commands
```sql
-- Create Table
CREATE TABLE student (
    ID          VARCHAR(5),
    name        VARCHAR(20) NOT NULL,
    dept_name   VARCHAR(20),
    tot_cred    NUMERIC(3,0) DEFAULT 0,
    PRIMARY KEY (ID),
    FOREIGN KEY (dept_name) REFERENCES department(dept_name)
);

-- Drop Table
DROP TABLE student;

-- Alter Table
ALTER TABLE student ADD email VARCHAR(50);
ALTER TABLE student DROP COLUMN email;
```

### Basic SELECT Structure
```sql
SELECT [DISTINCT] attribute(s)
FROM table(s)
WHERE condition(s)
GROUP BY attribute(s)
HAVING group_condition(s)
ORDER BY attribute(s) [ASC|DESC];
```

### String Operations
```sql
-- LIKE pattern matching
WHERE name LIKE 'K%'        -- Starts with K
WHERE name LIKE '%son'      -- Ends with son
WHERE name LIKE '%amp%'     -- Contains amp
WHERE name LIKE '___'       -- Exactly 3 characters
WHERE name LIKE 'C_m%'      -- C, any char, m, then anything

-- % matches any substring, _ matches any single character
-- Use ESCAPE for literal % or _
WHERE name LIKE '100\%' ESCAPE '\'
```

### ORDER BY
```sql
SELECT name, salary
FROM instructor
ORDER BY salary DESC, name ASC;
```

### Set Operations
```sql
-- UNION (removes duplicates)
(SELECT course_id FROM section WHERE year = 2018)
UNION
(SELECT course_id FROM section WHERE year = 2019);

-- UNION ALL (keeps duplicates)
-- INTERSECT, INTERSECT ALL
-- EXCEPT, EXCEPT ALL
```

### NULL Values
```sql
-- NULL comparisons use IS NULL / IS NOT NULL
WHERE salary IS NULL
WHERE salary IS NOT NULL

-- Arithmetic with NULL = NULL
-- Comparisons with NULL = UNKNOWN
-- WHERE clause treats UNKNOWN as FALSE
```

### Aggregate Functions
```sql
AVG(column)    -- Average value
MIN(column)    -- Minimum value
MAX(column)    -- Maximum value
SUM(column)    -- Sum of values
COUNT(column)  -- Number of non-null values
COUNT(*)       -- Number of rows
COUNT(DISTINCT column)  -- Number of distinct values
```

---

## 📚 TOPIC 6: Basic SQL Part 2 (ALL Slides) ⭐ HIGH PRIORITY

### GROUP BY and HAVING
```sql
-- Find average salary by department
SELECT dept_name, AVG(salary) as avg_salary
FROM instructor
GROUP BY dept_name
HAVING AVG(salary) > 50000;
```

**Rules:**
- Attributes in SELECT must be in GROUP BY or aggregate functions
- HAVING filters groups (after grouping)
- WHERE filters rows (before grouping)

### Subqueries

#### Scalar Subquery (returns single value)
```sql
SELECT name
FROM instructor
WHERE salary > (SELECT AVG(salary) FROM instructor);
```

#### IN / NOT IN
```sql
SELECT name
FROM instructor
WHERE dept_name IN ('Physics', 'Music');

SELECT name
FROM instructor
WHERE dept_name IN (SELECT dept_name FROM department WHERE budget > 100000);
```

#### EXISTS / NOT EXISTS
```sql
-- Find students who have taken at least one course
SELECT name
FROM student S
WHERE EXISTS (SELECT * FROM takes T WHERE T.ID = S.ID);
```

#### ALL / SOME (ANY)
```sql
-- Salary greater than all instructors in Biology
SELECT name
FROM instructor
WHERE salary > ALL (SELECT salary FROM instructor WHERE dept_name = 'Biology');

-- Salary greater than some instructor in Biology
SELECT name
FROM instructor
WHERE salary > SOME (SELECT salary FROM instructor WHERE dept_name = 'Biology');
```

### Joins
```sql
-- Cartesian Product (Cross Join)
SELECT * FROM student, takes;
SELECT * FROM student CROSS JOIN takes;

-- Natural Join (automatic on common columns)
SELECT * FROM student NATURAL JOIN takes;

-- Inner Join (explicit condition)
SELECT * FROM student 
INNER JOIN takes ON student.ID = takes.ID;

-- Left Outer Join (all from left, NULL for unmatched right)
SELECT * FROM student 
LEFT OUTER JOIN takes ON student.ID = takes.ID;

-- Right Outer Join
SELECT * FROM student 
RIGHT OUTER JOIN takes ON student.ID = takes.ID;

-- Full Outer Join
SELECT * FROM student 
FULL OUTER JOIN takes ON student.ID = takes.ID;
```

### WITH Clause (Common Table Expression)
```sql
WITH dept_total(dept_name, value) AS (
    SELECT dept_name, SUM(salary)
    FROM instructor
    GROUP BY dept_name
),
dept_avg(avg_value) AS (
    SELECT AVG(value) FROM dept_total
)
SELECT dept_name
FROM dept_total, dept_avg
WHERE dept_total.value > dept_avg.avg_value;
```

---

## 📚 TOPIC 7: Intermediate SQL (Slides 1-25, 27-32, 35) ⭐ HIGH PRIORITY

### Views
```sql
-- Create a view
CREATE VIEW faculty AS
    SELECT ID, name, dept_name
    FROM instructor;

-- Use a view like a table
SELECT name FROM faculty WHERE dept_name = 'Music';

-- Updatable views (simple single-table views)
-- Views with joins, aggregates, DISTINCT, GROUP BY are NOT updatable

-- Materialized Views (stores actual data, needs refresh)
```

### Integrity Constraints
```sql
-- NOT NULL
name VARCHAR(20) NOT NULL

-- UNIQUE
UNIQUE(email)

-- CHECK
salary NUMERIC(10,2) CHECK (salary > 0)
CHECK (semester IN ('Fall', 'Winter', 'Spring', 'Summer'))

-- PRIMARY KEY (implies NOT NULL + UNIQUE)
PRIMARY KEY(ID)

-- FOREIGN KEY with actions
FOREIGN KEY (dept_name) REFERENCES department(dept_name)
    ON DELETE CASCADE    -- Delete referencing rows
    ON UPDATE CASCADE    -- Update referencing rows
    -- Other options: SET NULL, SET DEFAULT, NO ACTION
```

### Assertions (Database-wide constraints)
```sql
CREATE ASSERTION credits_earned_constraint CHECK (
    NOT EXISTS (
        SELECT * FROM student
        WHERE tot_cred <> (
            SELECT COALESCE(SUM(credits), 0)
            FROM takes NATURAL JOIN course
            WHERE takes.ID = student.ID AND grade IS NOT NULL
        )
    )
);
```

### Authorization
```sql
-- Grant privileges
GRANT SELECT ON instructor TO user1;
GRANT INSERT, UPDATE ON instructor TO user1, user2;
GRANT ALL PRIVILEGES ON instructor TO admin;

-- Grant with ability to pass on
GRANT SELECT ON instructor TO user1 WITH GRANT OPTION;

-- Revoke privileges
REVOKE SELECT ON instructor FROM user1;
REVOKE SELECT ON instructor FROM user1 CASCADE; -- Revoke from grantees too

-- Roles
CREATE ROLE instructor_role;
GRANT SELECT ON student TO instructor_role;
GRANT instructor_role TO user1;
```

### SQL Data Types (Additional)
```sql
-- Large Objects
BLOB  -- Binary Large Object (images, videos)
CLOB  -- Character Large Object (text documents)

-- User-Defined Types
CREATE TYPE Dollars AS NUMERIC(12,2) FINAL;
CREATE DOMAIN degree_level VARCHAR(10)
    CONSTRAINT degree_level_test
    CHECK (value IN ('Bachelors', 'Masters', 'Doctorate'));
```

---

## 📚 TOPIC 8: Procedural SQL & Triggers (ALL Slides)

### SQL Functions
```sql
CREATE FUNCTION dept_count(dept_name VARCHAR(20))
RETURNS INTEGER
BEGIN
    DECLARE d_count INTEGER;
    SELECT COUNT(*) INTO d_count
    FROM instructor
    WHERE instructor.dept_name = dept_count.dept_name;
    RETURN d_count;
END;

-- Table-valued function
CREATE FUNCTION instructors_of(dept_name VARCHAR(20))
RETURNS TABLE (ID VARCHAR(5), name VARCHAR(20), salary NUMERIC(8,2))
RETURN TABLE (
    SELECT ID, name, salary
    FROM instructor
    WHERE instructor.dept_name = instructors_of.dept_name
);
```

### SQL Procedures
```sql
CREATE PROCEDURE dept_count_proc(IN dept_name VARCHAR(20), OUT d_count INTEGER)
BEGIN
    SELECT COUNT(*) INTO d_count
    FROM instructor
    WHERE instructor.dept_name = dept_count_proc.dept_name;
END;

-- Call procedure
DECLARE d_count INTEGER;
CALL dept_count_proc('Physics', d_count);
```

### Control Flow in SQL
```sql
-- IF-THEN-ELSE
IF condition THEN
    statements;
ELSEIF condition THEN
    statements;
ELSE
    statements;
END IF;

-- WHILE loop
WHILE condition DO
    statements;
END WHILE;

-- FOR loop (over query results)
FOR r AS
    SELECT budget FROM department WHERE dept_name = 'Music'
DO
    SET total = total + r.budget;
END FOR;

-- CASE expression
CASE
    WHEN score >= 90 THEN 'A'
    WHEN score >= 80 THEN 'B'
    WHEN score >= 70 THEN 'C'
    ELSE 'F'
END
```

### Triggers
```sql
CREATE TRIGGER credits_earned
AFTER UPDATE OF grade ON takes
REFERENCING NEW ROW AS nrow
            OLD ROW AS orow
FOR EACH ROW
WHEN (nrow.grade <> 'F' AND nrow.grade IS NOT NULL
      AND (orow.grade = 'F' OR orow.grade IS NULL))
BEGIN ATOMIC
    UPDATE student
    SET tot_cred = tot_cred + (
        SELECT credits FROM course
        WHERE course.course_id = nrow.course_id
    )
    WHERE student.ID = nrow.ID;
END;

-- Trigger timing: BEFORE, AFTER, INSTEAD OF
-- Trigger events: INSERT, DELETE, UPDATE [OF column]
-- Granularity: FOR EACH ROW, FOR EACH STATEMENT
```

---

## 📚 TOPIC 9: Normal Forms (Slides 1-23, 30-33) ⭐ HIGH PRIORITY

### Functional Dependencies
**Notation**: X → Y means X functionally determines Y
- If two tuples have same X values, they must have same Y values
- **Trivial FD**: X → Y where Y ⊆ X

### Armstrong's Axioms
1. **Reflexivity**: If Y ⊆ X, then X → Y
2. **Augmentation**: If X → Y, then XZ → YZ
3. **Transitivity**: If X → Y and Y → Z, then X → Z

### Derived Rules
4. **Union**: If X → Y and X → Z, then X → YZ
5. **Decomposition**: If X → YZ, then X → Y and X → Z
6. **Pseudotransitivity**: If X → Y and WY → Z, then WX → Z

### Closure of Attributes (X⁺)
Algorithm to find all attributes functionally determined by X:
1. Start with X⁺ = X
2. For each FD Y → Z, if Y ⊆ X⁺, add Z to X⁺
3. Repeat until no change

### Candidate Keys
- X is a **superkey** if X⁺ contains all attributes
- X is a **candidate key** if X is a minimal superkey

### Normal Forms

#### First Normal Form (1NF)
- All attributes have atomic (indivisible) values
- No repeating groups or arrays

#### Second Normal Form (2NF)
- Is in 1NF
- No partial dependencies (non-prime attribute depends on part of candidate key)

#### Third Normal Form (3NF)
- Is in 2NF
- No transitive dependencies
- For every FD X → Y: either X is a superkey OR Y is prime (part of candidate key)

#### Boyce-Codd Normal Form (BCNF)
- For every non-trivial FD X → Y: X must be a superkey
- Stricter than 3NF

### BCNF Decomposition Algorithm
1. Find FD X → Y that violates BCNF
2. Decompose R into: R1(X, Y) and R2(R - Y)
3. Repeat for each relation until all are in BCNF

### Lossless Decomposition Test
Decomposition of R into R1 and R2 is lossless if:
- R1 ∩ R2 → R1, OR
- R1 ∩ R2 → R2

### Dependency Preservation
- After decomposition, we should be able to enforce all original FDs
- Check if (F1 ∪ F2 ∪ ...)⁺ = F⁺

---

## 📚 TOPIC 11: Storage (Slides 5, 12-13, 16)

### Storage Hierarchy
- **Primary Storage**: Cache, Main Memory (volatile, fast)
- **Secondary Storage**: Flash/SSD, Magnetic Disk (non-volatile, slower)
- **Tertiary Storage**: Tape (archival, slowest)

### Disk Structure
- **Platter**: Circular disk surface
- **Track**: Concentric circles on platter
- **Sector**: Arc of track (smallest unit of read/write)
- **Block/Page**: Multiple sectors (unit of data transfer)

### Disk Access Time
- **Seek Time**: Move arm to correct track (slowest)
- **Rotational Latency**: Wait for sector to rotate under head
- **Transfer Time**: Actually read/write data

### File Organization
- **Heap File**: Records stored in any order
- **Sequential File**: Records sorted by search key
- **Hashing**: Records stored based on hash function

---

## 📚 TOPIC 12: Transactions (Slides 1-32, 35-36) ⭐ HIGH PRIORITY

### ACID Properties
- **Atomicity**: All or nothing - transaction completes fully or not at all
- **Consistency**: Database stays in valid state
- **Isolation**: Concurrent transactions don't interfere
- **Durability**: Committed changes persist even after crashes

### Transaction States
1. **Active**: Initial state, executing
2. **Partially Committed**: After last statement
3. **Failed**: Normal execution cannot proceed
4. **Aborted**: Rolled back, database restored
5. **Committed**: Successfully completed

### Schedules
- **Serial Schedule**: Transactions execute one after another
- **Serializable Schedule**: Equivalent to some serial schedule

### Conflict Serializability
Two operations **conflict** if:
1. They belong to different transactions
2. They access the same data item
3. At least one is a write

**Conflict Equivalent**: Same set of operations, same order of conflicting pairs

### Precedence Graph (Conflict Serializability Test)
1. Create node for each transaction
2. Add edge Ti → Tj if Ti has operation that conflicts with and precedes Tj's operation
3. Schedule is conflict serializable iff graph has **no cycles**

### Recoverable Schedules
- If Tj reads data written by Ti, Ti must commit before Tj commits
- **Cascading Rollback**: One abort causes chain of aborts

### Cascadeless Schedules
- Transactions only read committed data
- Avoids cascading rollbacks

---

## 📚 TOPIC 13: Concurrency Control (Slides 1-7, 9-11, 13-21) ⭐ HIGH PRIORITY

### Lock-Based Protocols

#### Lock Types
- **Shared Lock (S)**: For reading, multiple can hold
- **Exclusive Lock (X)**: For writing, only one can hold

#### Lock Compatibility
|     | S   | X   |
|-----|-----|-----|
| S   | ✓   | ✗   |
| X   | ✗   | ✗   |

### Two-Phase Locking (2PL)
1. **Growing Phase**: Transaction can acquire locks but cannot release any
2. **Shrinking Phase**: Transaction can release locks but cannot acquire any

**Guarantees conflict serializability but NOT deadlock-free**

### Strict Two-Phase Locking
- Hold all exclusive locks until commit/abort
- Avoids cascading rollbacks

### Rigorous Two-Phase Locking
- Hold ALL locks until commit/abort
- Transactions can be serialized in commit order

### Deadlock
- Cycle of transactions waiting for each other's locks

#### Deadlock Handling
1. **Prevention**: 
   - Wait-Die: Older waits, younger dies (rolls back)
   - Wound-Wait: Older wounds (forces rollback), younger waits
   
2. **Detection**: 
   - Build wait-for graph
   - Cycle = deadlock
   - Select victim and rollback

3. **Timeout**: 
   - Rollback if waiting too long

### Lock Granularity
- **Fine granularity** (row-level): More concurrency, more overhead
- **Coarse granularity** (table-level): Less concurrency, less overhead

### Intention Locks
- **IS (Intention Shared)**: Will request S on descendant
- **IX (Intention Exclusive)**: Will request X on descendant  
- **SIX (Shared + Intention Exclusive)**: S on node + IX for descendants

---

## 📚 TOPIC 14a: Indexing & Hashing (Slides 1-19, 47-49, 61-65)

### Index Concepts
- **Search Key**: Attribute(s) used to look up records
- **Index File**: Pairs of (search-key, pointer)
- Much smaller than data file

### Types of Indices
1. **Primary Index** (Clustering Index)
   - Index on the ordering key of a sequential file
   - One entry per block

2. **Secondary Index** (Non-Clustering Index)
   - Index on non-ordering attribute
   - One entry per record (denser)

### Dense vs Sparse Index
- **Dense Index**: Entry for every search-key value
- **Sparse Index**: Entry for only some values (file must be sorted)

### Multilevel Index
- Index on index (index too large for memory)
- Inner index sparse, outer can be sparse

### B+ Tree Index
- **Balanced**: All leaf nodes at same depth
- **Fan-out**: Number of children (typically large, 50-200)
- All data pointers in leaf nodes
- Leaf nodes linked for range queries

### Hashing
- **Static Hashing**: Fixed number of buckets
  - Overflow chains when bucket is full
  
- **Hash Function**: Maps search key to bucket address
  - Should distribute evenly

---

## 📚 TOPIC 14b: B+ Trees (ALL Slides except deletion)

### B+ Tree Properties
For a B+ tree of order n:
- Each non-root node has between ⌈n/2⌉ and n children
- Root has at least 2 children (if not a leaf)
- Leaf nodes have between ⌈(n-1)/2⌉ and n-1 values
- All leaves at same level

### B+ Tree Structure
- **Internal Nodes**: Keys + pointers to children
- **Leaf Nodes**: Keys + pointers to data + pointer to next leaf

### B+ Tree Search
1. Start at root
2. Find appropriate child pointer based on key comparison
3. Follow pointer, repeat until leaf
4. Search leaf for key

### B+ Tree Insertion
1. Find correct leaf
2. If space available, insert key in sorted order
3. If leaf full, **split**:
   - Create new leaf
   - Distribute keys: first ⌈n/2⌉ stay, rest go to new
   - Copy up middle key to parent
4. If parent full, split parent (propagate up)
5. If root splits, create new root (tree grows taller)

### B+ Tree Height
- Height h, fan-out n: can store up to n^h entries
- Typically 3-4 levels for millions of records

---

## 📚 TOPIC 15: Query Processing (Slides 3-5, 13-15, 19)

### Query Processing Steps
1. **Parsing**: Check syntax, validate tables/columns
2. **Translation**: Convert to relational algebra
3. **Optimization**: Find efficient execution plan
4. **Evaluation**: Execute the plan

### Cost Measures
- **Disk I/O**: Number of block transfers
- **CPU**: Processing time
- **Network**: Communication cost (distributed)

Disk I/O typically dominates cost

### Selection Operation Costs

| Method | Cost |
|--------|------|
| Linear Search (no index) | br blocks (entire file) |
| Binary Search (sorted) | ⌈log2(br)⌉ + records/block |
| Primary Index (equality) | hi + 1 (height + 1 block) |
| Secondary Index (equality) | hi + 1 (or + n for non-key) |
| Primary Index (range) | hi + #matching blocks |

### Join Operations

#### Nested Loop Join
```
for each tuple r in R:
    for each tuple s in S:
        if match(r, s):
            output(r, s)
```
Cost: nr × bs + br (or br × ns + bs using block nested loop)

#### Block Nested Loop Join
- For each block of R, load into memory
- Scan all blocks of S
- Cost: br × bs + br (or br + (br/M-2) × bs with M buffer blocks)

#### Indexed Nested Loop Join
- Use index on inner relation
- For each outer tuple, use index to find matches
- Cost: br + nr × c (where c = index lookup cost)

#### Sort-Merge Join
1. Sort both relations on join attribute
2. Merge sorted relations
- Cost: Sort costs + br + bs (linear merge)
- Good when one or both already sorted

### Query Optimization
- **Equivalence Rules**: Transform queries to equivalent forms
- **Cost Estimation**: Estimate cost of different plans
- **Heuristics**: 
  - Push selections down (reduce tuple count early)
  - Push projections down (reduce column count)
  - Use indices when available

---

## 🎯 KEY SQL QUERY PATTERNS FOR EXAM

### Finding MAX/MIN without using MAX/MIN
```sql
-- Find instructor with highest salary
SELECT name FROM instructor I1
WHERE NOT EXISTS (
    SELECT * FROM instructor I2 
    WHERE I2.salary > I1.salary
);

-- Alternative using ALL
SELECT name FROM instructor
WHERE salary >= ALL (SELECT salary FROM instructor);
```

### Counting with Conditions
```sql
-- Departments with more than 5 instructors
SELECT dept_name, COUNT(*) as cnt
FROM instructor
GROUP BY dept_name
HAVING COUNT(*) > 5;
```

### Correlated Subqueries
```sql
-- Students who have taken all courses offered by their department
SELECT S.name
FROM student S
WHERE NOT EXISTS (
    SELECT C.course_id 
    FROM course C 
    WHERE C.dept_name = S.dept_name
    AND NOT EXISTS (
        SELECT * FROM takes T
        WHERE T.ID = S.ID AND T.course_id = C.course_id
    )
);
```

### Self-Joins
```sql
-- Find pairs of instructors in same department
SELECT I1.name, I2.name
FROM instructor I1, instructor I2
WHERE I1.dept_name = I2.dept_name
AND I1.ID < I2.ID;
```

### Division Query (For All)
```sql
-- Students who have taken ALL CS courses
SELECT S.name
FROM student S
WHERE NOT EXISTS (
    SELECT course_id FROM course WHERE dept_name = 'CS'
    EXCEPT
    SELECT course_id FROM takes WHERE ID = S.ID
);
```

---

## ⚠️ COMMON EXAM MISTAKES TO AVOID

1. **GROUP BY errors**: Include all non-aggregated SELECT columns in GROUP BY
2. **NULL handling**: Remember NULL comparisons need IS NULL/IS NOT NULL
3. **HAVING vs WHERE**: HAVING filters groups, WHERE filters rows
4. **Join conditions**: Don't forget ON clause in explicit joins
5. **Subquery correlation**: Make sure correlated subqueries reference outer query correctly
6. **DISTINCT overuse**: Use only when you actually have duplicates to remove
7. **Order of operations**: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY

---

# 🎓 PRACTICE QUESTIONS SECTION

---

## 📝 MANY-TO-MANY JOIN PRACTICE (MCQ Focus)

### Understanding Many-to-Many Relationships
In a M:N relationship, you need an **intermediate/junction table**.

**Example Tables:**
```
student(ID, name, dept_name)
course(course_id, title, credits)
takes(ID, course_id, grade)  -- Junction table!
```

### Practice Questions - Multiple Choice Style

**Q1: What does this query return?**
```sql
SELECT s.name, c.title
FROM student s
NATURAL JOIN takes t
NATURAL JOIN course c;
```
A) All students and all courses
B) Only students who have taken courses, with course names
C) Cartesian product of students and courses
D) Students with NULL courses

**Answer: B** - Natural join only returns matching rows

**Q2: Which query finds students who have taken MORE THAN 3 courses?**
```sql
-- Option A
SELECT name FROM student WHERE ID IN 
  (SELECT ID FROM takes GROUP BY ID HAVING COUNT(*) > 3);

-- Option B  
SELECT name FROM student s, takes t 
WHERE s.ID = t.ID GROUP BY name HAVING COUNT(*) > 3;

-- Option C
SELECT name FROM student NATURAL JOIN takes 
GROUP BY ID, name HAVING COUNT(course_id) > 3;
```
**Answer: A and C are correct** (B is missing ID in GROUP BY)

**Q3: What's wrong with this query?**
```sql
SELECT s.name, COUNT(t.course_id)
FROM student s LEFT JOIN takes t ON s.ID = t.ID;
```
**Answer:** Missing GROUP BY s.ID, s.name

### Many-to-Many Join Patterns
```sql
-- Students with their courses (M:N via takes)
SELECT s.name, c.title
FROM student s
JOIN takes t ON s.ID = t.ID
JOIN course c ON t.course_id = c.course_id;

-- Count courses per student (including 0)
SELECT s.name, COUNT(t.course_id) as num_courses
FROM student s
LEFT JOIN takes t ON s.ID = t.ID
GROUP BY s.ID, s.name;

-- Students who have taken a specific course
SELECT DISTINCT s.name
FROM student s
JOIN takes t ON s.ID = t.ID
WHERE t.course_id = 'CS101';
```

---

## 📝 PROCEDURES - Writing and Calling

### Procedure Syntax Template
```sql
CREATE PROCEDURE procedure_name (
    IN input_param TYPE,
    OUT output_param TYPE,
    INOUT both_param TYPE
)
BEGIN
    -- Declare local variables
    DECLARE local_var TYPE;
    
    -- SQL statements
    SELECT column INTO output_param
    FROM table
    WHERE condition;
    
    -- Can use IF, WHILE, etc.
END;
```

### Practice: Write a Procedure
**Task:** Create a procedure that takes a department name and returns the count of instructors.

```sql
CREATE PROCEDURE get_instructor_count(
    IN dept VARCHAR(20),
    OUT instructor_count INTEGER
)
BEGIN
    SELECT COUNT(*) INTO instructor_count
    FROM instructor
    WHERE dept_name = dept;
END;
```

### Calling a Procedure
```sql
-- Declare variable to hold output
DECLARE @count INTEGER;

-- Call the procedure
CALL get_instructor_count('Physics', @count);

-- Or in some systems:
EXECUTE get_instructor_count('Physics', @count);
```

### Practice Question
**Q: Write a procedure that transfers an amount from one account to another.**
```sql
CREATE PROCEDURE transfer(
    IN from_account VARCHAR(10),
    IN to_account VARCHAR(10),
    IN amount NUMERIC(10,2)
)
BEGIN
    UPDATE account SET balance = balance - amount
    WHERE account_number = from_account;
    
    UPDATE account SET balance = balance + amount
    WHERE account_number = to_account;
END;

-- Call it:
CALL transfer('A-101', 'A-102', 500.00);
```

---

## 📝 FUNCTIONS - Writing and Calling

### Function Syntax Template
```sql
CREATE FUNCTION function_name(param1 TYPE, param2 TYPE)
RETURNS return_type
BEGIN
    DECLARE result return_type;
    
    -- Calculate result
    SELECT expression INTO result
    FROM table
    WHERE condition;
    
    RETURN result;
END;
```

### Practice: Write a Function
**Task:** Create a function that returns the average salary for a department.

```sql
CREATE FUNCTION avg_dept_salary(dept VARCHAR(20))
RETURNS NUMERIC(10,2)
BEGIN
    DECLARE avg_sal NUMERIC(10,2);
    
    SELECT AVG(salary) INTO avg_sal
    FROM instructor
    WHERE dept_name = dept;
    
    RETURN avg_sal;
END;
```

### Calling a Function
```sql
-- Functions are called within SQL statements
SELECT name, salary, avg_dept_salary(dept_name) as dept_avg
FROM instructor
WHERE salary > avg_dept_salary(dept_name);

-- Or standalone
SELECT avg_dept_salary('Physics');
```

### Function vs Procedure

| Feature | Function | Procedure |
|---------|----------|-----------|
| Returns | Must return a value | Optional (OUT params) |
| Call from SELECT | Yes | No |
| CALL statement | No | Yes |
| Return type | Single value or table | N/A |

---

## 📝 TRIGGERS - Writing Practice

### Trigger Syntax Template
```sql
CREATE TRIGGER trigger_name
{BEFORE | AFTER} {INSERT | UPDATE | DELETE} [OF column]
ON table_name
REFERENCING {NEW | OLD} ROW AS alias
FOR EACH {ROW | STATEMENT}
[WHEN (condition)]
BEGIN [ATOMIC]
    -- trigger body
END;
```

### Practice: Write These Triggers

**Task 1:** Prevent salary from being decreased
```sql
CREATE TRIGGER salary_check
BEFORE UPDATE OF salary ON instructor
REFERENCING NEW ROW AS nrow
            OLD ROW AS orow
FOR EACH ROW
WHEN (nrow.salary < orow.salary)
BEGIN
    SET nrow.salary = orow.salary;
END;
```

**Task 2:** Log all deletions from instructor table
```sql
CREATE TRIGGER log_instructor_delete
AFTER DELETE ON instructor
REFERENCING OLD ROW AS orow
FOR EACH ROW
BEGIN
    INSERT INTO instructor_log(ID, name, deleted_date)
    VALUES (orow.ID, orow.name, CURRENT_DATE);
END;
```

**Task 3:** Auto-update student credits when grade is assigned
```sql
CREATE TRIGGER update_credits
AFTER UPDATE OF grade ON takes
REFERENCING NEW ROW AS nrow
            OLD ROW AS orow
FOR EACH ROW
WHEN (nrow.grade IS NOT NULL AND orow.grade IS NULL)
BEGIN ATOMIC
    UPDATE student
    SET tot_cred = tot_cred + (
        SELECT credits FROM course
        WHERE course_id = nrow.course_id
    )
    WHERE ID = nrow.ID;
END;
```

---

## 📝 GRANT/REVOKE PRACTICE (MCQ Focus)

### Quick Reference
```sql
GRANT {privilege} ON {object} TO {user/role} [WITH GRANT OPTION];
REVOKE {privilege} ON {object} FROM {user/role} [CASCADE | RESTRICT];
```

### Practice Multiple Choice

**Q1: User A grants SELECT to User B WITH GRANT OPTION. User B grants SELECT to User C. If User A revokes from User B with CASCADE, what happens?**
A) Only B loses privilege
B) Both B and C lose privilege
C) Neither loses privilege
D) Only C loses privilege

**Answer: B** - CASCADE revokes from all grantees

**Q2: Which statement allows User X to grant SELECT privilege to others?**
A) `GRANT SELECT ON table TO X;`
B) `GRANT SELECT ON table TO X WITH GRANT OPTION;`
C) `GRANT ALL ON table TO X;`
D) `GRANT SELECT, GRANT ON table TO X;`

**Answer: B**

**Q3: What does this do?**
```sql
CREATE ROLE faculty;
GRANT SELECT, INSERT ON student TO faculty;
GRANT faculty TO prof_smith;
```
A) Creates a role and gives prof_smith those privileges
B) Error - cannot grant role to user
C) Only creates the role, nothing else
D) Gives all privileges to prof_smith

**Answer: A**

---

## 📝 WRITING TRANSACTIONS

### Transaction Syntax
```sql
BEGIN TRANSACTION;
    -- SQL statements
    UPDATE account SET balance = balance - 100 WHERE id = 1;
    UPDATE account SET balance = balance + 100 WHERE id = 2;
    
    -- Check conditions
    IF (SELECT balance FROM account WHERE id = 1) < 0 THEN
        ROLLBACK;
    ELSE
        COMMIT;
    END IF;
END;
```

### Practice: Write a Transaction
**Task:** Transfer $500 from account A to account B, but rollback if A's balance would go negative.

```sql
BEGIN TRANSACTION;
    -- Deduct from account A
    UPDATE account 
    SET balance = balance - 500 
    WHERE account_id = 'A';
    
    -- Add to account B
    UPDATE account 
    SET balance = balance + 500 
    WHERE account_id = 'B';
    
    -- Check constraint
    IF EXISTS (SELECT * FROM account WHERE account_id = 'A' AND balance < 0)
    THEN
        ROLLBACK;
    ELSE
        COMMIT;
    END IF;
END;
```

### Transaction Keywords
- `BEGIN TRANSACTION` or `START TRANSACTION`
- `COMMIT` - Make changes permanent
- `ROLLBACK` - Undo all changes
- `SAVEPOINT name` - Create restore point
- `ROLLBACK TO name` - Rollback to savepoint

---

## 📝 TRUE/FALSE PRACTICE - Transactions

| Statement | T/F |
|-----------|-----|
| A transaction must have either COMMIT or ROLLBACK at the end | **T** |
| Atomicity means transactions are indivisible | **T** |
| Durability means committed data survives system crashes | **T** |
| Isolation means transactions run one at a time | **F** (they can run concurrently but appear isolated) |
| A serial schedule is always conflict serializable | **T** |
| Every conflict serializable schedule is serial | **F** (it's equivalent to some serial schedule) |
| Cascadeless schedules allow reading uncommitted data | **F** (they only read committed data) |
| 2PL guarantees no deadlocks | **F** (it guarantees serializability, not deadlock-free) |
| Strict 2PL prevents cascading rollbacks | **T** |
| If precedence graph has no cycle, schedule is serializable | **T** |

---

## 📝 TRUE/FALSE PRACTICE - Indexes

| Statement | T/F |
|-----------|-----|
| A primary index is always dense | **F** (can be sparse since file is sorted) |
| A secondary index must be dense | **T** |
| B+ trees are always balanced | **T** |
| All data pointers in B+ tree are in leaf nodes | **T** |
| B+ tree height increases with every insertion | **F** (only when root splits) |
| Hash index is good for range queries | **F** (only equality) |
| Clustered index determines physical order of data | **T** |
| You can have multiple clustered indexes on a table | **F** (only one) |
| B+ tree leaves are linked for range queries | **T** |
| Sparse index requires sorted file | **T** |

---

## 📝 TRUE/FALSE PRACTICE - B+ Trees

| Statement | T/F |
|-----------|-----|
| In a B+ tree of order n, each leaf has at most n-1 keys | **T** |
| Internal nodes contain data pointers | **F** (only leaf nodes) |
| When a leaf splits, a key is copied up to parent | **T** |
| When an internal node splits, a key is pushed up | **T** |
| All leaves are at the same level | **T** |
| Root must have at least n/2 children | **F** (root has at least 2) |
| B+ tree search is O(log n) | **T** |
| Deleting a key may cause tree height to decrease | **T** |

---

## 📝 PRECEDENCE GRAPH PRACTICE ⭐ IMPORTANT

### How to Build a Precedence Graph
1. Create a node for each transaction
2. For each pair of conflicting operations where Ti's op comes before Tj's:
   - Add edge Ti → Tj
3. Conflicts: R-W, W-R, W-W on same data item

### Example 1
**Schedule:** R1(A), R2(A), W1(A), W2(A)

**Conflicts:**
- R1(A) before W2(A): T1 → T2
- R2(A) before W1(A): T2 → T1
- W1(A) before W2(A): T1 → T2

**Graph:** T1 ↔ T2 (cycle!)

**Result:** NOT conflict serializable ❌

### Example 2
**Schedule:** R1(A), W1(A), R2(A), W2(A), R1(B), W1(B), R2(B), W2(B)

**Conflicts on A:**
- W1(A) before R2(A): T1 → T2
- W1(A) before W2(A): T1 → T2

**Conflicts on B:**
- W1(B) before R2(B): T1 → T2
- W1(B) before W2(B): T1 → T2

**Graph:** T1 → T2 (no cycle)

**Result:** Conflict serializable ✓ (equivalent to T1, T2)

### Example 3
**Schedule:** R1(A), R2(B), W2(A), W1(B)

**Conflicts:**
- R1(A) before W2(A): T1 → T2
- R2(B) before W1(B): T2 → T1

**Graph:** T1 ↔ T2 (cycle!)

**Result:** NOT conflict serializable ❌

### Practice Problem
**Given Schedule:** R3(X), R1(X), W3(X), W2(X), R2(Y), W1(Y)

Draw the precedence graph and determine if serializable.

**Solution:**
- R1(X) before W3(X): T1 → T3
- R1(X) before W2(X): T1 → T2
- W3(X) before W2(X): T3 → T2
- R2(Y) before W1(Y): T2 → T1

**Graph:** 
```
T1 → T3 → T2
 ↑         |
 └─────────┘
```
**Cycle exists!** NOT serializable ❌

---

## 📝 B+ TREE INSERTION PRACTICE ⭐ IMPORTANT

### B+ Tree of Order 3 (max 2 keys per node)

**Insert sequence: 5, 8, 1, 7, 3, 12, 9, 6**

**Step 1: Insert 5**
```
[5]
```

**Step 2: Insert 8**
```
[5, 8]
```

**Step 3: Insert 1** (leaf full, split!)
```
      [5]
     /   \
  [1]    [5, 8]
```

**Step 4: Insert 7**
```
      [5]
     /   \
  [1]    [5, 7, 8] → Split!

      [5, 7]
     /   |   \
  [1]  [5]  [7, 8]
```

**Continue practice on your own!**

### Key Rules to Remember:
1. **Leaf split:** Copy middle key up
2. **Internal split:** Push middle key up
3. **Root split:** Create new root (tree grows taller)
4. Leaves stay linked (left to right)

### Practice Question
**Q: In a B+ tree of order 4 (max 3 keys), after inserting 10, 20, 5, 15, 25, 30, what is the root?**

Insert 10: [10]
Insert 20: [10, 20]
Insert 5: [5, 10, 20]
Insert 15: Full! Split → Root becomes [10], leaves [5] and [10, 15, 20]
Insert 25: [10, 15, 20, 25] → Split! → Root becomes [10, 20], leaves...

**Answer: [10, 20]** with three leaf nodes

---

## 📝 ACID PROPERTIES - DETAILED DEFINITIONS ⭐ MEMORIZE

| Property | Definition | Example |
|----------|------------|---------|
| **Atomicity** | A transaction is an indivisible unit - either ALL operations complete or NONE do. If any part fails, the entire transaction is rolled back. | Bank transfer: both debit AND credit happen, or neither happens. |
| **Consistency** | A transaction brings the database from one valid state to another valid state. All integrity constraints are maintained. | Total money in system stays constant after transfer. |
| **Isolation** | Concurrent transactions execute as if they were running alone. Intermediate states are not visible to other transactions. | While T1 is transferring money, T2 sees either the "before" or "after" state, never partial. |
| **Durability** | Once a transaction commits, its changes are permanent and survive any subsequent system failures (crashes, power loss). | After COMMIT, the transfer is saved even if system crashes 1 second later. |

### Common Exam Questions on ACID

**Q: Which property ensures that a committed transaction survives a power failure?**
A) Atomicity  B) Consistency  C) Isolation  D) **Durability**

**Q: Which property is violated if T1 reads data that T2 has written but not yet committed?**
A) Atomicity  B) Consistency  C) **Isolation**  D) Durability

**Q: A transaction that debits one account and credits another ensures total balance unchanged. Which property?**
A) Atomicity  B) **Consistency**  C) Isolation  D) Durability

**Q: If a system crash occurs mid-transaction and changes are undone, which property is demonstrated?**
A) **Atomicity**  B) Consistency  C) Isolation  D) Durability

---

## 📝 COMPREHENSIVE PRACTICE EXAM

### Section A: Multiple Choice (Similar to exam format)

**1.** What is returned by: `SELECT COUNT(*) FROM student WHERE dept IS NULL;`
- A) 0
- B) Number of students with NULL dept
- C) Error
- D) Number of all students

**Answer: B**

**2.** In 2PL, when can a transaction release a lock?
- A) Immediately after using the data
- B) Only during shrinking phase
- C) Only at commit
- D) Any time

**Answer: B** (Strict 2PL would be C)

**3.** A B+ tree of order 5 can have at most how many keys in a leaf?
- A) 4
- B) 5
- C) 3
- D) 2

**Answer: A** (order n = max n-1 keys)

**4.** Which is NOT a valid join type?
- A) NATURAL JOIN
- B) INNER JOIN
- C) OUTER JOIN
- D) MIDDLE JOIN

**Answer: D**

**5.** What does `REVOKE ... CASCADE` do?
- A) Only removes privilege from named user
- B) Removes from user and all who got it through them
- C) Removes all privileges from user
- D) Error - CASCADE not valid for REVOKE

**Answer: B**

### Section B: Write SQL Queries

**1.** Find all instructors who earn more than the average salary in their department.
```sql
SELECT I.name
FROM instructor I
WHERE I.salary > (
    SELECT AVG(I2.salary)
    FROM instructor I2
    WHERE I2.dept_name = I.dept_name
);
```

**2.** Find departments that have no instructors.
```sql
SELECT dept_name FROM department
WHERE dept_name NOT IN (SELECT dept_name FROM instructor);

-- OR using LEFT JOIN
SELECT d.dept_name
FROM department d
LEFT JOIN instructor i ON d.dept_name = i.dept_name
WHERE i.ID IS NULL;
```

**3.** Find students who have taken ALL courses in the 'CS' department.
```sql
SELECT s.name
FROM student s
WHERE NOT EXISTS (
    SELECT c.course_id FROM course c WHERE c.dept_name = 'CS'
    EXCEPT
    SELECT t.course_id FROM takes t WHERE t.ID = s.ID
);
```

### Section C: True/False
(See sections above for practice)

### Section D: Precedence Graphs
(See section above for practice)

### Section E: B+ Trees
(See section above for practice)

---

## ⚠️ FINAL EXAM TIPS

1. **Read questions carefully** - SQL MCQs often have subtle differences
2. **For precedence graphs**: List all conflicts first, then draw edges
3. **For B+ trees**: Remember order n means max n-1 keys in leaves
4. **For ACID**: Know specific definitions and examples
5. **For transactions**: Practice writing BEGIN/COMMIT/ROLLBACK
6. **For normalization**: Know how to compute closure and find candidate keys
7. **Time management**: Don't spend too long on one question

---

## 📝 PRACTICE QUESTIONS CHECKLIST
- [ ] Review all homework problems
- [ ] Review all worksheets
- [ ] Review practice problems
- [ ] Review project SQL queries
- [ ] Practice precedence graphs
- [ ] Practice B+ tree insertions
- [ ] Practice writing procedures, functions, triggers
- [ ] Review ACID properties
- [ ] Practice many-to-many join queries

Good luck on your exam! 🍀

