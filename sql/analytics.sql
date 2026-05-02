-- Receita por produto
SELECT product_name, SUM(revenue) AS total_revenue
FROM sales
GROUP BY product_name
ORDER BY total_revenue DESC;

-- Receita por categoria
SELECT category, SUM(revenue) AS total_revenue
FROM sales
GROUP BY category
ORDER BY total_revenue DESC;

-- Vendas por dia
SELECT date, SUM(revenue) AS total_revenue
FROM sales
GROUP BY date
ORDER BY date;