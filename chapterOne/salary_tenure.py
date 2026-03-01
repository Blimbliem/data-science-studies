# anonymous data with salary(USD) and tenure

salaries_tenure = [(83000, 8.7),(88000,8.1),(48000,0.7),(76000, 6), (69000, 6.5),(76000, 7.5),(60000, 2.5),(83000, 10), (48000, 1.9), (63000, 4.2)]



from collections import defaultdict

# keys are years and values it a list about salary by tenure
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_tenure:
    salary_by_tenure[tenure].append(salary)

print(salary_by_tenure)

# keys are years and values its a average salary by tenure

average_salary_by_tenure = {tenure: sum(salaries)/len(salaries) for tenure, salaries in salary_by_tenure.items()}

print(average_salary_by_tenure)



# function to bucketize tenure
def tenure_bukect(tenure):
    if tenure <2:
        return "less than two"
    elif tenure <5:
        return "between two and five"
    else:
        return "more than five"
 
# keys are tenure buckets and values are list of salaries by tenure bucket   
salary_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_tenure:
    buckect = tenure_bukect(tenure)
    salary_tenure_bucket[buckect].append(salary)

print(salary_tenure_bucket)


# keys are years and values its a list of salaries by tenure bucket

average_salary_bucket = {tenure_bucket: sum(salaries)/ len(salaries) for tenure_bucket, salaries in salary_tenure_bucket.items()}

print(average_salary_bucket)