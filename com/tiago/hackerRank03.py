def split_and_join(line):
    # write your code here
    
    new_line ="-".join(line)
    return new_line
if __name__ == '__main__':
    line = tuple (map(str,input()))
    line
    result = split_and_join(line)
    print(result)
    