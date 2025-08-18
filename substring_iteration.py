def count_substring(string, sub_string):
    num = 0
    length = len(string)


    for i in range(0,length + 1):
        for j in range(0,length + 1):
            if string[i:j] == sub_string:
                num += 1
           


    return num
 



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)