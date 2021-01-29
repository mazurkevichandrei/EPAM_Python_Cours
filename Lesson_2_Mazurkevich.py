##########Initial Data############
map1={'a':3,'b':1,'c':10,'f':18}
print(map1)
map1_keys=[]
map2={'a':5,'d':2,'c':9,'f':80}
print(map2)
map2_keys=[]
map_result = {}
########Unmap keys for map1#######
print('######Keys######')
for key,value in map1.items():
   keys1=key
   map1_keys.append(keys1)
print(map1_keys)
########Unmap keys for map2#######
for key,value in map2.items():
   keys2=key
   map2_keys.append(keys2)
print(map2_keys)
a=0
###Chesk key in map1 == key in map2
while a<len(map1_keys):
    if map1_keys[a] == map2_keys[a]:
    ####Found higest value for key in both maps:
        #for i in map1:
        for i in map1_keys[a]:
            if map1[i] > map2[i]:
                map_result[i]=map1[i] #Put higest value in result map from map1
                map_result['{}_1'.format(i)]=map_result.pop(i) #Change key format
            else:
                map_result[i] = map2[i] #Put higest value in result map from map2
                map_result['{}_2'.format(i)] = map_result.pop(i) #Change key format
        a=a+1
    ###If key from map1 not in map2 -> put both keys and values in result map:
    else:
        map_result[map1_keys[a]]=map1[map1_keys[a]]
        map_result[map2_keys[a]] = map2[map2_keys[a]]
        a=a+1
print('#####Result#####')
print(map_result)
###########################################################