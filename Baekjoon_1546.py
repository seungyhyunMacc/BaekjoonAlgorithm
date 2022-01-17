n=input() # 과목 개수 입력
score_list=list(map(int, input().split())) # 과목 원점수 입력
max_score=max(score_list)

modified_score=[]   # 조작된 점수 리스트
for i in score_list:
    score= i/max_score*100 # 조작을 위한 공식
    modified_score.append(score) # 조작된 점수를 리스트에 추가

print(sum(modified_score)/int(n)) # 평균구함