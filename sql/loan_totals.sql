/**
All current loans
**/
select 
	l.starting_debt + sum(t.transaction_amount) as current_loans
from dbo.loans l
left join dbo.transactions t on l.account_guid = t.account_guid
group by l.account_guid, l.starting_debt