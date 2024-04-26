import pandas as pd
import random as r
import math as m
import os as os

# Specify the folder path
output_folder = 'D:/Desktop/AI/Cluster_Output/'

# Create the folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

df1 = pd.read_csv('D:/Desktop/AI/CC GENERAL.csv')
df1.drop('CUST_ID', inplace=True, axis=1)

c1 = r.randint(0, 8949)
c2 = r.randint(0, 8949)
c3 = r.randint(0, 8949)
centroid1 = df1.iloc[c1]
centroid2 = df1.iloc[c2]
centroid3 = df1.iloc[c3]

for iteration in range(1, 100):  # Iterate 100 times
    cluster1 = []
    cluster2 = []
    cluster3 = []
    
    for j in range(0, 8949):
        if j == c1 or j == c2 or j == c3:
            continue
        
        point = df1.iloc[j]
        temp1=0
        temp2=0
        temp3=0
        #euclidian distance
        for i in range(0,17):
            temp1=temp1+(point.iloc[i]-centroid1.iloc[i])**2
            temp2=temp2+(point.iloc[i]-centroid2.iloc[i])**2
            temp3=temp3+(point.iloc[i]-centroid3.iloc[i])**2
        temp1=m.sqrt(temp1)
        temp2=m.sqrt(temp2)
        temp3=m.sqrt(temp3)
        
        #Manhattab distance
        # for i in range(0,17):
        #     temp1=temp1 + abs(point.iloc[i]-centroid1.iloc[i])
        #     temp2=temp2 + abs(point.iloc[i]-centroid2.iloc[i])
        #     temp3=temp3 + abs(point.iloc[i]-centroid3.iloc[i])
         
        if temp1 <= temp2 and temp1 <= temp3:
            cluster1.append(j)
        elif temp2 <= temp1 and temp2 <= temp3:
            cluster2.append(j)
        else:
            cluster3.append(j)

    new_centroid1 = df1.iloc[cluster1].mean()
    new_centroid2 = df1.iloc[cluster2].mean()
    new_centroid3 = df1.iloc[cluster3].mean()
    print('Iteration:',iteration)
    print('Size of cluster 1:',len(cluster1))
    print('Size of cluster 2:',len(cluster2))
    print('Size of cluster 3:',len(cluster3))
    print()
    

    # Create DataFrames for each cluster
    cluster1_df = df1.iloc[cluster1]
    cluster2_df = df1.iloc[cluster2]
    cluster3_df = df1.iloc[cluster3]

    # Write each DataFrame to a CSV file for this iteration
    cluster1_df.to_csv(os.path.join(output_folder, f'iteration_{iteration}_cluster1.csv'), index=False)
    cluster2_df.to_csv(os.path.join(output_folder, f'iteration_{iteration}_cluster2.csv'), index=False)
    cluster3_df.to_csv(os.path.join(output_folder, f'iteration_{iteration}_cluster3.csv'), index=False)

    if (centroid1.equals(new_centroid1) and centroid2.equals(new_centroid2) and centroid3.equals(new_centroid3)):
        break

    centroid1, centroid2, centroid3 = new_centroid1, new_centroid2, new_centroid3        

    
    
    
   