
import sys

#end= in the print statements helps add on the '! Welcome' at the end of the Hello phrase. 
name = input('What is your name?')

print('Hello,', end='')
sys.stdout.write(sys.argv[1])
sys.stdout.write(sys.argv[2])
print('and')
sys.stdout.write(sys.argv[3])
print('! Welcome.')

# To run this code: cd /Users/Benjamin/Documents/CS550 
# python3 Helloworld.py Ben, Alex, Sam
