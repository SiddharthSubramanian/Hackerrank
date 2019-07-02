#!/usr/bin/py

def nextQuestion(n, plurality, lies, color, exact_lies, query, query_size):
    # Create separate buckets for each ball
    # Create a dictionary for recording bucket sizes
    buckets = {i:[i] for i in range(n)}
    bucket_sizes = {i:1 for i in range(n)}
    dump = []

    for i,j,ans in query:
        # If color is different, dump both the buckets
        if ans==0:
            dump.append(i)
            dump.append(j)
            buckets.pop(i, None)
            buckets.pop(j, None)
            bucket_sizes.pop(i, None)
            bucket_sizes.pop(j, None)
        # If color is same, merge the buckets and update sizes
        else:
            buckets[i] = buckets[i] + buckets[j]
            bucket_sizes[i] = bucket_sizes[i] + bucket_sizes[j]
            buckets.pop(j, None)
            bucket_sizes.pop(j, None)

    # Check if all the buckets are of different sizes
    if len(set(list(bucket_sizes.values()))) == len(buckets):
        # Bucket with the biggest size is the majority color bucket
        biggest_bucket_idx = max(bucket_sizes, key=bucket_sizes.get)
        print(buckets[biggest_bucket_idx][0])
    else:
        # Group buckets by size
        sizes = set(bucket_sizes.values())
        buckets_eq_size = {}
        for i in sizes:
            buckets_eq_size[i] = [k for k in bucket_sizes.keys() if bucket_sizes[k] == i]

        # Next query will be between elements of any two buckets with equal sizes
        query_size = [k for k,v in buckets_eq_size.items() if len(v)>=2][0]
        print(str(buckets_eq_size[query_size][0]) + 
            ' ' + str(buckets_eq_size[query_size][1]))


if __name__ == '__main__':
    vals = [int(i) for i in input().strip().split()]
    query_size = int(input())
    query = []

    for i in range(query_size):
        temp = [j for j in input().strip().split()]
        if temp[2] == "YES":
            query.append([int(temp[0]), int(temp[1]), 1])
        else:
            query.append([int(temp[0]), int(temp[1]), 0])

    nextQuestion(vals[0], vals[1], vals[2], vals[3], vals[4], query, query_size)