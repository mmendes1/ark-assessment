/**
Sum of transactions, should this be grouped by member or account guid, I think member to accounts are one to many
This is a bit of a mess, might need to find better way to do this.
**/
select 
	m.first_name, 
	m.last_name, 
	sum(t.transaction_amount) + c.starting_balance as current_balance,
	CASE
	WHEN (sum(t.transaction_amount) + c.starting_balance) < 0
		THEN 1
	ELSE 0
	END as overdrawn
from dbo.transactions t
left join dbo.accounts a on t.account_guid = a.account_guid
left join dbo.members m on a.member_guid = m.member_guid
left join dbo.checking c on c.account_guid = a.account_guid
where c.starting_balance IS NOT NULL 
group by m.first_name, m.last_name, m.member_guid, c.starting_balance
order by overdrawn desc;