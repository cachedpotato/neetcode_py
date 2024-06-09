def encode(strs):
  out = ""
  delim = "#"
  #we need two things: delimiter and the length of string
  #just the delimiter isn't enough - what if there's delimiter character inside word?
  #adding num+delim in front of EVERY word will solve this issue
  for s in strs:
    l = len(s)
    out += str(l) + delim + s

  return out

def encode_o_n_time(strs):
  #string concat copies the entire string apparantly?
  #the f'' syntax might be useful
  return "".join(
    f'{len(s)}#{s}' for s in strs
  )

def decode(s):
  out = []
  #every encoded word looks like (len)#(word)
  i = 0
  while i < len(s):
    j = i #the length of word can exceed single digit!
    while s[j] != "#":
      j += 1
    
    len_word = int(s[i:j]) #j lands on # after exiting loop
    out.append(s[j + 1 : j + 1 + len_word])

    i = j + 1 + len_word

  return out

def main():
  strs = ["hello", "world", "test", "412#12129312"]
  print("before:\t\t{}".format(strs))
  e = encode_o_n_time(strs)
  d = decode(e)
  print("after decoding:\t{}".format(d))

if __name__ == "__main__":
  main()
  
