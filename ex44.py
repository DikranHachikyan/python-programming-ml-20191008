# 2

def sortWithPriority(values,group):
    def helper(item):
        if item in group:
            return (0,item)
        return (1,item)
    values.sort(key=helper)

if __name__ == '__main__':
    nums = [3,2,4,7,5,9,8,1]
    group = {9,8,7} 

    sortWithPriority(nums,group)

    print(f'nums:{nums}')   