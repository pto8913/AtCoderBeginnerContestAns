def main():
  N = int(input())
  A = list(map(int,input().split()))

  tmp = 0
  for a in A:
    tmp += 1/a
  print(1/tmp)

main()
