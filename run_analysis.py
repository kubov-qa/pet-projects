import housing_math as hm

avg_salary_gross = 129_000

median_salary_net = hm.convert_avg_to_median(hm.apply_tax(avg_salary_gross))

print(median_salary_net)