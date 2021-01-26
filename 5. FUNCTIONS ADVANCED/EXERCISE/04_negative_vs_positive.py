nums = list(map(int, input().split()))
positives = list(filter(lambda x: x > 0, nums))
negatives = list(filter(lambda x: x < 0, nums))
sum_negatives = sum(negatives)
sum_positives = sum(positives)
print(sum_negatives)
print(sum_positives)
if sum_positives > abs(sum_negatives):
    print('The positives are stronger than the negatives')
else:
    print('The negatives are stronger than the positives')
