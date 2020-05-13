# %%
from pglast import Node, parse_sql
import json

# %%
join_query = """SELECT T1.country,
    T1.name,
    count(*)
FROM airlines AS T1
JOIN routes AS T2 ON T1.alid = T2.alid
GROUP BY T1.country,
    T1.name"""

subquery = """SELECT count(*)
FROM routes
WHERE dst_apid IN
        (SELECT apid
         FROM airports
         WHERE country = 'Canada')
    AND src_apid IN
        (SELECT apid
         FROM airports
         WHERE country = 'United States')"""

# %%
query = subquery

root = Node(parse_sql(query))
stmt = root[0]
stmt_json = json.dumps(stmt.parse_tree)
print(stmt_json)

# %%
root = Node(parse_sql('SELECT [T1].[country] FROM [airlines] AS [T1]'))

# %%