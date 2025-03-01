create or replace view "public"."outdated_bid_datetime" as  SELECT DISTINCT ba."BID",
    to_timestamp((ba."InsertTime")::double precision) AS last_updated
   FROM books_avail ba
  WHERE (to_timestamp((ba."InsertTime")::double precision) < (now() - '12:00:00'::interval))
  ORDER BY (to_timestamp((ba."InsertTime")::double precision));



