from CTCIT.util import ctcdbUtil
from CTCIT.cfg import get_ctcdb

# db = ctcdbUtil.execute("select available_balance,reserved_balance from trade_account WHERE customer_id = 5 and coin_symbol = 'BTC'")
# print(db)
#
# db1 = ctcdbUtil.execute("select id from trade_order where customer_id in (5,6) and status = 1000")
# print(db1[0][0])

data = ctcdbUtil.execute(get_ctcdb.get_rate[0])
print(data[0][0],data[0][1])
