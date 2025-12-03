def main():
  file_object = open("input1.txt", "r")
  password = 0
  currPos = 50

  for line in file_object:
    currMove = getMove(line.strip())
    currPos = (currPos + currMove) % 100
    if(currPos == 0): password += 1
  
  print(password)

    
def getMove(stringMove : str) -> int:
  direction = stringMove[0]
  moves = int(stringMove[1:])

  print(direction)
  return moves if (direction == "R") else -moves

if __name__ == "__main__":
  main()