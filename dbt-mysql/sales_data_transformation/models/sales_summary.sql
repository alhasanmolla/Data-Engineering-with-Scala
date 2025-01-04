-- models/sales_summary.sql

SELECT
    product_id,
    SUM(sale_amount) AS total_sales
FROM
    ecommerce.sales  -- Ensure this table exists
GROUP BY
    product_id;