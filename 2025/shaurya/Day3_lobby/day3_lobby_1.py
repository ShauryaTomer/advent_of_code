def main():
  input = open("input1.txt", "r")
  maxPower = 0

  for line in input:
    j = maxJolt(line)
    maxPower += j

  print(maxPower)

def maxJolt(batteries: str) -> int:
  f = batteries[0]
  s = batteries[1]
  maxJolt = int(f + s)
  for i in range(2, len(batteries)):
    battery = batteries[i]
    jolt1 = int(f + battery)
    jolt2 = int(s + battery)

    if(jolt1 > maxJolt):
      maxJolt = jolt1
      s = battery

    if(jolt2 > maxJolt):
      maxJolt = jolt2
      f = s
      s = battery
  
  return maxJolt

if __name__ == "__main__":
  main()