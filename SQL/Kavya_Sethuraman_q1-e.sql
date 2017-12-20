select concat(a.first_name," ",a.last_name) as name from actor_info a where a.actor_id in ( select actor_id from film_actor  group by actor_id having count(actor_id) >1) order by a.first_name asc;
