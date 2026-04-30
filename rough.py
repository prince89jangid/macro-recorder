with open("test.txt", "r") as file:
    content = file.read().strip().split('\n')
    print(content[0])


    # for i in content:

    #     if i.split()[0].isdigit() == True and i.split()[1].isdigit() == True:
    #         x = int(i.split()[0])
    #         y = int(i.split()[1])

    #     else:
    #         print(i)
