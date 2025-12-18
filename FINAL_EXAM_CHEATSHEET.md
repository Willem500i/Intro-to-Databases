# DATABASE FINAL EXAM CHEATSHEET - Willem (NetID: wdn2012)
## A4 Paper - Both Sides | Dec 18, 2025

---
# SIDE 1: SQL & QUERIES
---

## SQL SELECT STRUCTURE
```sql
SELECT [DISTINCT] cols FROM tables
[WHERE row_conditions]
[GROUP BY cols] [HAVING group_conditions]
[ORDER BY cols [ASC|DESC]];
```
**Order of Execution**: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY

## DATA TYPES
`VARCHAR(n)` `CHAR(n)` `INT` `NUMERIC(p,d)` `DATE` `TIME` `TIMESTAMP` `BLOB` `CLOB`

## DDL
```sql
CREATE TABLE t (col TYPE [NOT NULL] [DEFAULT val], PRIMARY KEY(col), 
  FOREIGN KEY(col) REFERENCES t2(col) [ON DELETE/UPDATE CASCADE|SET NULL]);
DROP TABLE t; ALTER TABLE t ADD/DROP col TYPE;
```

## AGGREGATES
`COUNT(*)` `COUNT(col)` `COUNT(DISTINCT col)` `SUM()` `AVG()` `MIN()` `MAX()`
- NULL values ignored in aggregates (except COUNT(*))
- Must GROUP BY all non-aggregate columns in SELECT

## STRING OPERATIONS
```sql
LIKE '%text%'  -- % = any string, _ = any char
'100\%' ESCAPE '\'  -- literal %
UPPER() LOWER() TRIM() SUBSTRING() LENGTH() CONCAT()||
```

## NULL HANDLING
```sql
IS NULL / IS NOT NULL  -- NOT: = NULL
COALESCE(val1, val2, ...)  -- first non-null
NULLIF(a, b)  -- NULL if a=b, else a
```

## JOINS
```sql
NATURAL JOIN        -- auto on common cols
INNER JOIN t ON     -- explicit condition  
LEFT OUTER JOIN     -- all left + matching right (NULL if none)
RIGHT OUTER JOIN    -- all right + matching left
FULL OUTER JOIN     -- all from both
CROSS JOIN          -- cartesian product
```
**M:N Join**: Use junction table! `student ⟶ takes ⟶ course`
```sql
SELECT s.name, c.title FROM student s
JOIN takes t ON s.ID = t.ID JOIN course c ON t.course_id = c.course_id;
```

## SUBQUERIES
```sql
-- Scalar (returns 1 value)
WHERE salary > (SELECT AVG(salary) FROM instructor)

-- IN/NOT IN
WHERE dept IN ('CS', 'Math')
WHERE dept IN (SELECT dept FROM ... )

-- EXISTS/NOT EXISTS  
WHERE EXISTS (SELECT * FROM takes WHERE takes.ID = student.ID)

-- ALL/SOME(ANY)
WHERE salary > ALL (SELECT salary FROM ...)  -- greater than all
WHERE salary > SOME (SELECT salary FROM ...) -- greater than at least one
```

## DIVISION - "FOR ALL" QUERIES
```sql
-- Students who took ALL CS courses
SELECT name FROM student S
WHERE NOT EXISTS (
  SELECT course_id FROM course WHERE dept='CS'
  EXCEPT
  SELECT course_id FROM takes WHERE ID = S.ID);
```

## WITH CLAUSE (CTE)
```sql
WITH temp_table(col1, col2) AS (SELECT ...)
SELECT * FROM temp_table WHERE ...;
```

## SET OPERATIONS
`UNION` `UNION ALL` `INTERSECT` `INTERSECT ALL` `EXCEPT` `EXCEPT ALL`

## VIEWS
```sql
CREATE VIEW v AS SELECT ...; 
-- Not updatable if: JOIN, aggregate, DISTINCT, GROUP BY, derived cols
```

## AUTHORIZATION
```sql
GRANT priv ON table TO user [WITH GRANT OPTION];
REVOKE priv ON table FROM user [CASCADE];
-- Privs: SELECT, INSERT, UPDATE, DELETE, ALL PRIVILEGES
CREATE ROLE r; GRANT role TO user;
```

## CONSTRAINTS
```sql
NOT NULL | UNIQUE | PRIMARY KEY | CHECK(condition)
FOREIGN KEY(col) REFERENCES t(col) ON DELETE/UPDATE CASCADE|SET NULL|NO ACTION
CREATE ASSERTION name CHECK (condition);
```

## PROCEDURES ⭐
```sql
CREATE PROCEDURE proc_name(IN p1 TYPE, OUT p2 TYPE)
BEGIN
  DECLARE var TYPE;
  SELECT col INTO p2 FROM t WHERE col = p1;
END;
-- CALL procedure
DECLARE @result TYPE;
CALL proc_name('input', @result);
```

## FUNCTIONS ⭐
```sql
CREATE FUNCTION func_name(p1 TYPE) RETURNS TYPE
BEGIN
  DECLARE result TYPE;
  SELECT col INTO result FROM t WHERE col = p1;
  RETURN result;
END;
-- USE in SELECT
SELECT func_name(col) FROM table;
```

## TRIGGERS ⭐
```sql
CREATE TRIGGER trig_name 
BEFORE|AFTER INSERT|UPDATE|DELETE [OF col] ON table
REFERENCING NEW ROW AS nrow OLD ROW AS orow
FOR EACH ROW
WHEN (condition)
BEGIN ATOMIC
  -- SQL statements using nrow.col, orow.col
END;
```

## TRANSACTIONS ⭐
```sql
BEGIN TRANSACTION;
  UPDATE account SET bal = bal - 100 WHERE id = 1;
  UPDATE account SET bal = bal + 100 WHERE id = 2;
  IF (condition) THEN ROLLBACK; ELSE COMMIT; END IF;
END;
```
Keywords: `COMMIT` `ROLLBACK` `SAVEPOINT x` `ROLLBACK TO x`

## CONTROL FLOW
```sql
IF cond THEN ... ELSEIF ... ELSE ... END IF;
WHILE cond DO ... END WHILE;
CASE WHEN cond THEN val ... ELSE val END
```

---
# SIDE 2: THEORY & CONCEPTS
---

## ACID PROPERTIES ⭐ MEMORIZE
- **A**tomicity: ALL ops complete or NONE do (rollback on failure)
- **C**onsistency: DB valid state → valid state (constraints maintained)
- **I**solation: Concurrent txns appear to run alone (no partial visibility)
- **D**urability: Committed changes SURVIVE crashes (persisted to disk)

## TRANSACTION STATES
Active → Partially Committed → Committed
Active → Failed → Aborted

## CONFLICT SERIALIZABILITY
Operations conflict if: diff txns + same item + at least one write
**Precedence Graph**: Ti→Tj if Ti op conflicts & precedes Tj op
**Serializable iff NO CYCLES**

## SCHEDULES
- **Recoverable**: If Tj reads Ti's write, Ti commits before Tj
- **Cascadeless**: Only read committed data
- **Serial**: One txn at a time

## TWO-PHASE LOCKING (2PL)
1. **Growing**: Acquire locks, no release
2. **Shrinking**: Release locks, no acquire
- Guarantees conflict serializability
- **Strict 2PL**: Hold X-locks until commit (no cascading)
- **Rigorous 2PL**: Hold all locks until commit

## LOCK COMPATIBILITY
|   | S | X |
|---|---|---|
| S | ✓ | ✗ |
| X | ✗ | ✗ |

## INTENTION LOCKS (Hierarchy)
IS (intention shared), IX (intention exclusive), SIX (S + IX)
Request from root down, release from leaf up

## DEADLOCK
- **Wait-Die**: Old waits, young dies (rollback)
- **Wound-Wait**: Old wounds (rollback young), young waits
- **Detection**: Wait-for graph cycle = deadlock

## FUNCTIONAL DEPENDENCIES
X → Y: Same X values ⟹ same Y values

**Armstrong's Axioms:**
1. Reflexivity: Y ⊆ X ⟹ X → Y
2. Augmentation: X → Y ⟹ XZ → YZ
3. Transitivity: X → Y, Y → Z ⟹ X → Z

**Derived**: Union, Decomposition, Pseudotransitivity

## ATTRIBUTE CLOSURE (X⁺)
1. X⁺ = X
2. For each Y → Z: if Y ⊆ X⁺, add Z to X⁺
3. Repeat until no change
X is superkey if X⁺ = all attributes

## NORMAL FORMS
| NF | Rule |
|----|------|
| 1NF | Atomic values only |
| 2NF | 1NF + no partial dependencies |
| 3NF | 2NF + no transitive deps (X→Y: X superkey OR Y prime) |
| BCNF | All X→Y: X is superkey |

**BCNF Decomposition**: Find violation X→Y, split into (X,Y) and (R-Y)
**Lossless Test**: R1∩R2 → R1 OR R1∩R2 → R2

## B+ TREE (Order n) ⭐
- Non-root internal: ⌈n/2⌉ to n children, ⌈n/2⌉-1 to n-1 keys
- Leaf: ⌈(n-1)/2⌉ to **n-1 keys** (NOT n!)
- Root: at least 2 children (if not leaf)
- All leaves same level, linked left→right

**INSERT**: Find leaf → insert sorted → if full: SPLIT
- Leaf split: **COPY** middle key up, first ⌈n/2⌉ stay, rest go new
- Internal split: **PUSH** middle key up
- Root split: new root created (tree grows taller)

**DELETE**: Remove key → if underflow: redistribute or merge

## INDEX TYPES
- **Primary/Clustering**: On ordering key, sparse OK
- **Secondary/Non-clustering**: Dense required
- **Dense**: Entry per key value
- **Sparse**: Entry per block

## QUERY COST
- **Linear scan**: br blocks
- **Binary search**: ⌈log₂(br)⌉
- **Primary index**: h + 1
- **Secondary index**: h + 1 (+ n for non-key)

## JOIN COSTS
- **Nested Loop**: nr × bs + br
- **Block Nested Loop**: br × bs + br
- **Index Nested Loop**: br + nr × (index cost)
- **Sort-Merge**: Sort + br + bs

## OPTIMIZATION HEURISTICS
1. Push selections down (early filtering)
2. Push projections down (fewer columns)
3. Use indices when available

## ER MODEL QUICK REF
| Symbol | Meaning |
|--------|---------|
| □ Rectangle | Entity |
| ◇ Diamond | Relationship |
| ○ Ellipse | Attribute |
| Double line | Total participation |
| Double rect | Weak entity |
| Dashed ellipse | Derived attr |

## KEYS
- **Superkey**: Uniquely identifies tuple
- **Candidate Key**: Minimal superkey
- **Primary Key**: Chosen candidate key
- **Foreign Key**: References another PK

## CARDINALITIES
1:1, 1:N, N:1, M:N (min,max notation also possible)

## QUICK SQL PATTERNS
```sql
-- Max without MAX
SELECT * FROM t WHERE col >= ALL(SELECT col FROM t);
-- NOT EXISTS version
SELECT * FROM t1 WHERE NOT EXISTS(SELECT * FROM t2 WHERE t2.col > t1.col);

-- Find duplicates
SELECT col, COUNT(*) FROM t GROUP BY col HAVING COUNT(*) > 1;

-- Self-join pairs
SELECT a.col, b.col FROM t a, t b WHERE a.id < b.id;
```

## STORAGE LEVELS
Cache → RAM (volatile) → SSD/Disk → Tape (archival)
Disk: Seek time + Rotational latency + Transfer time

## PRECEDENCE GRAPH RULES ⭐
1. Node for each transaction
2. Edge Ti→Tj if: (R-W, W-R, or W-W conflict) AND Ti's op before Tj's
3. **NO CYCLE = Serializable** | **CYCLE = NOT Serializable**

## T/F QUICK FACTS
- Serial schedule = always serializable ✓
- 2PL guarantees serializability ✓ (NOT deadlock-free!)
- Strict 2PL prevents cascading rollbacks ✓
- B+ tree always balanced ✓
- Secondary index must be dense ✓
- Hash index bad for range queries ✓

---
**YOUR PROF SAID**: No RA drawing, no ER drawing, no writing procs/funcs/triggers
**BUT KNOW**: Proc/func/trigger syntax (read), SQL queries, ACID, precedence graphs, B+ trees

