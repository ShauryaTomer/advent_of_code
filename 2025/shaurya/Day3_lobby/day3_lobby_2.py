def main():
  input = open("input2.txt", "r")
  totalMaxPower = 0
  digitsToPick = 12

  for line in input:
    lineMaxPower = maxPower(line.strip(), digitsToPick)
    print(lineMaxPower)
    totalMaxPower += int(lineMaxPower)
  print(totalMaxPower)

def maxPower(line: str, digitstoPick: int) -> int:
  n = len(line)
  l = 0
  
  powerFormed = ""
  
  for r in range(n - digitstoPick, n):
    maxIndex = findMaxIndexInRange(line, l, r)
    if len(powerFormed) == 12: break

    powerFormed = powerFormed + line[maxIndex]
    
    l = maxIndex + 1 # + 1 because maxIndex was picked right now, it cannot be picked again
  
  return powerFormed

def findMaxIndexInRange(line: str, l: int, r: int):
  maxIndex = l
  for i in range(l, r + 1):
    # print(f"${line[i]} : ${line[maxIndex]} : ${line[i] > line[maxIndex]}")
    if(line[i] > line[maxIndex]):
      maxIndex = i

  return maxIndex


if __name__ == "__main__":
  main()