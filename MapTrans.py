import numpy as np

border = {"lon": [118.8, 122.0], "lat": [25.4, 25.7]} #每升高一個lat單位要手動加一lat單位給第一筆資料
#ex:最一開始是21.44拉完第一排後就要改成21.44+0.44=21.88
per_lon = 0.48
per_lat = 0.44
for i in range(7):
    square = []
    if i!=0:
        border['lon'][0]=round(border['lon'][0]+per_lon,2)
    square.append([border['lon'][0],border['lat'][0]])
    for j in range(4):
        if j == 0:
            border['lon'][0]+=per_lon
        elif j == 1:
            border['lat'][0]+=per_lat
        elif j == 2:
            border['lon'][0]-=per_lon
        elif j == 3:
            border['lat'][0]-=per_lat

        border['lon'][0]=round(border['lon'][0],2)
        border['lat'][0]=round(border['lat'][0],2)
        square.append([border['lon'][0],border['lat'][0]])

    print(i,square)

