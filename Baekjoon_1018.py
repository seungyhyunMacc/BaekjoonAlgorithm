n, m=map(int, input().split())

chess=[input()for _ in range(n)]


WChessBoard=[       ## 백흑백흑,,,,
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]

BChessBoard=[       ## 흑백흑백,,,,
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]

def CheckMin(i, j):
    WResult=0
    BResult=0    
    for ChessI in range(8):
        for ChessJ in range(8):
            ci, cj= i+ChessI, j+ChessJ
            if(chess[ci][cj]!=BChessBoard[ChessI][ChessJ]): ## chess판은 10 * 13이 될수도 9*23이 될수도있음, 흑백보드는 8 * 8
                BResult += 1    ## 틀렸으면 값을 추가 
            if(chess[ci][cj]!=WChessBoard[ChessI][ChessJ]): ## 백흑보드는 8 * 8
                WResult += 1
    return min(BResult, WResult)   ## 최소를 구해야됨

Result=100000000
for a in range(n-7):    ## 전체 체스판에서 8 * 8이 움직일 수 있는 가용범위
    for b in range(m-7):
        Result=min(Result, CheckMin(a, b)) ## 최신화를 계속 시켜줘야함
print(Result)