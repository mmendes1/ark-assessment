/**
Find overpaid loan payments
**/
select 
	m.first_name, 
	m.last_name, 
	(l.starting_debt + sum(t.transaction_amount)) as current_debt
from dbo.loans l
left join dbo.transactions t on l.account_guid = t.account_guid
left join dbo.accounts a on l.account_guid = a.account_guid
left join dbo.members m on m.member_guid = a.member_guid
group by m.first_name, m.last_name, l.account_guid, l.starting_debt
order by current_debt asc;