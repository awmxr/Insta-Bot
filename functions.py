def text_to_dec(x):
    if("," in x):
        x = x.replace("," , '')
    if('k' in x):
        x = x.replace('k','')
        x = int(float(x)*1000)
    elif('m' in x):
        x = x.replace('m','')
        x = int(float(x)*1000000)
    return x
    
    # print(x)


text_to_dec('27.2k')
text_to_dec('420m')