def main():
  input = open("input2.txt", "r")
  ranges = input.read().split(",")
  invalid_id_sum = 0

  for r in ranges:
    start = int(r.split("-")[0])
    end = int(r.split("-")[1])

    for id in range(start, end + 1): #range skips the last number
      if(isInvalid(str(id))):  
        # print(id)
        invalid_id_sum += id
  
  print(invalid_id_sum)

def isInvalid(id: str) -> bool:
  if(id[0] == "0"): return True
  size = len(id)

  #id[:i] takes first i elements of the string and range goes till upperlimit - 1 (upper limit not included) we start from 1 because starting from 0 will lead to taking empty substr (useless and gives error)
  for i in range(1, size//2 + 1): 
    if size % i != 0: continue
    repetation = size//i
    substr = id[:i]
    if(substr * repetation == id): return True

  return False

if __name__ == "__main__":
  main()