import functools



def main():
    rules = []
    jobs = []
    with open('input') as f:
        for line in f.readlines():
            if '|' in line:
                left, right = line.split('|')
                rules.append((int(left), int(right)))
            elif ',' in line:
                numbers = [int(num.strip()) for num in line.split(',')]
                jobs.append(numbers)

    def sat(job, rule):
        for i in range(len(job)):
            if job[i] == rule[1]:
                for j in range(i, len(job)):
                    if job[j] == rule[0]:
                        return False
        return True

    def job_good(job):
        return all(sat(job, rule) for rule in rules)

    def middle_page(job):
        return job[len(job) // 2]

    total = 0
    for job in jobs:
        if job_good(job):
            total += middle_page(job)

    print(total)


    total = 0
    def pg_cmp(left, right):
        if (left, right) in rules:
            return -1
        else:
            return 1

    for job in jobs:
        if not job_good(job):
            fixed_job = sorted(job, key=functools.cmp_to_key(pg_cmp))
            total += middle_page(fixed_job)


    print(total)



if __name__ == '__main__':
    main()