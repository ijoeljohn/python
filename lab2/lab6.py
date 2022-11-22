color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}
print("the original dictionary is :" +str(color_dict))
res = {key:val for key,val in sorted(color_dict.items(),key = lambda ele: ele[0])}
print(str(res))