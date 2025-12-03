def main():
  file_object = open("input1.txt", "r")
  invalid_ids_sum = 0
  ranges = file_object.read().split(",")
  
  for r in ranges:
    start = int(r.split("-")[0])
    end = int(r.split("-")[1])

    for id in range(start, end):
      if(isInvalid(str(id))): 
        print(id)
        invalid_ids_sum += int(id)

  print(invalid_ids_sum)
def isInvalid(id : str) -> bool:
  if (id[0] == "0"): return True
  mid = len(id)//2

  if (len(id) % 2 == 0 and id[mid:] == id[:mid]): return True

  return False

if __name__ == "__main__":
  main()