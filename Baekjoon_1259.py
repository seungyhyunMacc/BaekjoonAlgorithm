while True:
    n = input()
    if n == '0':
        break;
    elif n==n[::-1]:
        print('yes')
    else:
        print('no')    

#### 굳이 정답을 이어 붙이지 않아도 되는구나,,,,,,,,
#### 하나 풀고 정답이 나오게 해도됨

#### 펠린드롬의 특징은 예제를 왼쪽에서 오른쪽으로 배치하던 오른쪽에서 왼쪽으로 배치하던 항상 같다