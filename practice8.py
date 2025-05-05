def swap_case(s):
    return s.swapcase()
s=input()
result=swap_case(s)
print(result)

def split_and_join(line):
    return "-".join(line.split())
line=input()
result=split_and_join(line)
print(result)

def print_full_name(a,b):
    print(f"Hello {a} {b}! You just delved into python.")
a=input()
b=input()
print_full_name(a,b)   

def mutate_string(string, position, character):
    return string[:position]+character+string[position+1:]   
s=input()
i,c=input().split()
result=mutate_string(s,int(i),c)
print(result)

def count_substring(string,sub_string):
    count=0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count+=1
    return count
string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)

if __name__=='__main__':
    s=input()
    if any(c.isalnum() for c in s):
        print(True)