if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    def run_up(num,ar):
        if 2<=num<=10:
            scores = sorted(set(ar), reverse=True)
            print(scores[1])
        
run_up(n,arr)
