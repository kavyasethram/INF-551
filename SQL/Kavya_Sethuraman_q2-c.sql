select count(a.customer_id) as customerCount from action_view a where a.customer_id not in (select customer_id from horror_view);
