import sys, argparse

def main():
  parser = argparse.ArgumentParser(description="This is a program with parsed arguments")
  parser.add_argument('POSITIONAL', help="Positional argument")
  parser.add_argument('-a', '--anoption', help="Here's an optional argument")
  somechoices = ['1','2','3','5','8']
  parser.add_argument('-b', '--anotheroption', choices=somechoices, nargs='*', help="argument with choices and arbitrary number of inputs")

  parsed = parser.parse_args(sys.argv[1:])

  positional = parsed.POSITIONAL
  anoption = parsed.anoption
  anotheroption = parsed.anotheroption

if __name__=="__main__":
  main()
