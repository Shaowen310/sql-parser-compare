# %%
import sqlparse
from sqlparse.filters import StripWhitespaceFilter, ReindentFilter
from sqlparsehelperextract import RemoveEmptyWhitespaceFilter

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

query = join_query

query = query.upper()
stmts = sqlparse.parse(query)
stmt = stmts[0]
# rif = ReindentFilter(width=0)
# rif.process(stmt)
swsf = StripWhitespaceFilter()
swsf.process(stmt)
rewsf = RemoveEmptyWhitespaceFilter()
rewsf.process(stmt)
stmt._pprint_tree()

# %%
