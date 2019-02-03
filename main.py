import career_value as CV
values = CV.values

Always_valued_list = []
Often_valued_list = []
Sometimes_valued_list = []
Seldom_valued_list = []
Never_valued_list = []
for key in values:
    print("----------------------------------------------------------------")
    print(key, ":\n", values[key])
    print("----------------------------------------------------------------")
    
    num_value = input("Please enter how often you value it (in number):"
          "\n"
          "Always(1), Often(2), Sometimes(3), Seldom(4), Never(5) valued \n")
#    importance_value = float(input("Please enter the importance within its category (1~10) (1 is the most important) \n"))
    if num_value == "1":
#        Always_valued_list.append((importance_value, key))
        Always_valued_list.append(key)
    elif num_value == "2":
#        Often_valued_list.append((importance_value, key))
        Often_valued_list.append(key)
    elif num_value == "3":
       # Sometimes_valued_list.append((importance_value, key))
        Sometimes_valued_list.append(key)
    elif num_value == "4":
#        Seldom_valued_list.append((importance_value, key))
        Seldom_valued_list.append(key)
    elif num_value == "5":
#        Never_valued_list.append((importance_value, key))
        Never_valued_list.append(key)

    Always_valued_list.sort()
    Often_valued_list.sort()
    Sometimes_valued_list.sort()
    Seldom_valued_list.sort()
    Never_valued_list.sort()

    outfile = open("values_results.txt","w")
    print("-------------------------------------------------------------", file=outfile)
    print("Always Valued", file=outfile)
    print("-------------------------------------------------------------", file=outfile)
    for line_str in Always_valued_list:
        print(line_str, file=outfile)

    print("-------------------------------------------------------------", file=outfile)
    print("Often Valued", file=outfile)
    print("-------------------------------------------------------------", file=outfile)
    for line_str in Often_valued_list:
        print(line_str, file=outfile)

    print("-------------------------------------------------------------", file=outfile)
    print("Sometimes Valued", file=outfile)
    print("-------------------------------------------------------------", file=outfile)
    for line_str in Sometimes_valued_list:
        print(line_str, file=outfile)

    print("-------------------------------------------------------------", file=outfile)
    print("Seldom Valued", file=outfile)
    print("-------------------------------------------------------------", file=outfile)
    for line_str in Seldom_valued_list:
        print(line_str, file=outfile)

    print("-------------------------------------------------------------", file=outfile)
    print("Never Valued", file=outfile)
    print("-------------------------------------------------------------", file=outfile)
    for line_str in Never_valued_list:
        print(line_str, file=outfile)

    
