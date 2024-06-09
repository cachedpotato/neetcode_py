def is_valid_palindrome(strs):
  concat_string = "".join(c.lower() for c in strs if c.isalpha())

  return concat_string

def main():
  strs = "Was it a car or a cat I saw?"
  print(is_valid_palindrome(strs))
  print(is_valid_palindrome("0P"))
  a = "12312312312"
  print(a[1:-1])

if __name__ == "__main__":
  main()
