N = int(input())
score_list = list(map(int, input().split()))

max_score = max(score_list)

#이 3줄짜리를
new_score = []
for i in score_list:
    new_score.append((i / max_score) * 100)
# 이렇게 한줄로 가능함(시도 해볼려다가 안됐음 ㅜ)
# adjusted_scores = [(score / max_score) * 100 for score in scores]

new_average = sum(new_score) / len(new_score)

print(new_average)