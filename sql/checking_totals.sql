/**
All current balances
**/
select
	c.starting_balance + sum(t.transaction_amount) as current_balance 
from dbo.checking c
left join dbo.transactions t on c.account_guid = t.account_guid
group by c.account_guid, c.starting_balance