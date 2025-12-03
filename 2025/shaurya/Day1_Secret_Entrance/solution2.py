def main():
  file_object = open("input2.txt", "r")
  password = 0
  pos = 50

  for line in file_object:
    move = getMove(line.strip())
    baseMove = move % 100 if move >= 0 else -(-move % 100)
    # print(f"move : {move} | baseMove : {baseMove}")

    password += (abs(move)//100)
    if(baseMove <= -(pos) or baseMove >= (100 - pos)):
      if(pos != 0): password += 1

    # print(f"password : {password}")

    pos = pos + move
    pos = (pos + 100) % 100
    # print(f"pos : {pos}")
  print(password)

    
def getMove(stringMove : str) -> int:
  direction = stringMove[0]
  moves = int(stringMove[1:])

  # print(moves)
  return moves if (direction == "R") else -moves

if __name__ == "__main__":
  main()