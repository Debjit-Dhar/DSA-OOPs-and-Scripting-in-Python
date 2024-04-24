
#!/usr/bin/env python
# coding: utf-8

# In[34]:


# import necessary packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics


# In[35]:


df1=pd.read_csv("person100.csv")


# In[36]:

beg=0
end=3600
data = df1['Lead 2'].iloc[beg:end]
length_dat=end-beg


# In[37]:


# normalized data between -1 to 1

ecg_signal = 2*((data-np.min(data))/(np.max(data)-np.min(data)))-1
print("Index\tData")
#for i in range(beg,end):
#    print(i,"\t",ecg_signal[i])





# In[38]:


positive_values = [diff for diff in ecg_signal if diff > 0]
negative_values = [diff for diff in ecg_signal if diff < 0]

average_positive = statistics.mean(positive_values)
std_dev_positive = statistics.stdev(positive_values)

average_negative = statistics.mean(negative_values)
std_dev_negative = statistics.stdev(negative_values)

print("Positive Values:")
print("Average:", average_positive)
print("Standard Deviation:", std_dev_positive)

print("\nNegative Values:")
print("Average:", average_negative)
print("Standard Deviation:", std_dev_negative)
#raw_filtered = [diff if not (average_negative-2*std_dev_negative <= diff <= average_positive+0.5*std_dev_positive) else 0 for diff in ecg_signal]
raw_filtered_rpeak = [diff if not (diff <= average_positive+0.5*std_dev_positive) else 0 for diff in ecg_signal]
#raw_filtered_ppeak = [diff if not (diff <= average_positive+0.2*std_dev_positive) else 0 for diff in ecg_signal]
#print(type(raw_filtered))
print("Row Filtered:",raw_filtered_rpeak)
#R_peak = [diff if not (diff => np.max(raw_filtered)) else 0 for diff in raw_filtered]
print(len(raw_filtered_rpeak))




# def rpeak(lst):
#     max_val = None
#     result = []

#     for value in lst:
#         if value != 0:
#             if max_val is None or value > max_val:
#                 max_val = value
#         elif max_val is not None:
#             result.append(max_val)
#             max_val = None
#             value = 0
#         result.append(0)

#     if max_val is not None:
#         result.append(max_val)

#     return result

def rpeak(lst):
    result = [0] * len(lst)
    i = 0

    while i < len(lst):
        # Skip consecutive zeros
        while i < len(lst) and lst[i] == 0:
            i += 1

        if i < len(lst):
            # Found the start of a non-zero sequence
            start = i
            max_val = lst[i]

            # Find the maximum value in the non-zero sequence
            while i < len(lst) and lst[i] != 0:
                max_val = max(max_val, lst[i])
                i += 1

            # Set all values in the sequence to zero except the maximum value
            for j in range(start, i):
                if lst[j] != max_val:
                    result[j] = 0
                else:
                    result[j] = max_val

    return result

# Example usage:
result = rpeak(raw_filtered_rpeak)
print("R_Peak:",result)
print(len(result))
# Filter and print non-zero values
non_zero_values = [value for value in result if value != 0]
print("R_Peak_points:", non_zero_values)
print(len(non_zero_values))


'''plt.plot(result)
plt.plot(raw_filtered_rpeak)
#plt.axhline(raw_filtered_rpeak)
#plt.axhline(average_positive+std_dev_positive)
#plt.axhline(average_positive+.5*std_dev_positive)
plt.axhline(average_negative-1.5*std_dev_positive)
plt.xlabel('Index')
plt.ylabel('Difference')
plt.title('Differences between Consecutive ECG Channel Data Points')
plt.grid(True)
plt.show()'''


# In[51]:

print("non_zero_values")
print(non_zero_values)
rdif=[0 for i in range(len(non_zero_values)-1)]


# In[61]:

print('R peak indexes')
k=0
rpeak_index=[0 for i in range(len(non_zero_values))]
for i in range(length_dat):
    if(result[i]!=0):
        rpeak_index[k]=beg+i+1
        k+=1
print(rpeak_index)
print('R peak index differences')
for i in range(len(non_zero_values)-1):
    rdif[i]=rpeak_index[i+1]-rpeak_index[i]
print(rdif)


# In[78]:

print("speak_indexes speaks")
#Find S
speak_index=[0 for i in range(len(non_zero_values))]
for i in range(len(non_zero_values)):
    speak_index[i]=rpeak_index[i]
for j in range(len(non_zero_values)):
    t=speak_index[j]
    for i in range(t,t+31):
        if(ecg_signal[i]<ecg_signal[speak_index[j]]):
            speak_index[j]=i
for i in range(len(non_zero_values)):
    print(speak_index[i],"\t\t",ecg_signal[speak_index[i]])
#append s peak with result list
t=0
for i in range(len(result)):
    if(beg+i==speak_index[t]):
        result[i]=ecg_signal[speak_index[t]]
        if(t==len(non_zero_values)-1):
            break
        t+=1
print("result after adding s peaks")
print(result)
print(len(result))


# In[79]:

print("qpeak_indexes qpeaks")
#Find Q
qpeak_index=[0 for i in range(len(non_zero_values))]
for i in range(len(non_zero_values)):
    qpeak_index[i]=rpeak_index[i]
for j in range(len(non_zero_values)):
    t=qpeak_index[j]
    for i in range(t-31,t):
        if(ecg_signal[i]<ecg_signal[qpeak_index[j]]):
            qpeak_index[j]=i
for i in range(len(non_zero_values)):
    print(qpeak_index[i],"\t",ecg_signal[qpeak_index[i]])
#append q peak with result list
print("Result after adding q peaks")
t=0
for i in range(len(result)):
    if(beg+i==qpeak_index[t]):
        result[i]=ecg_signal[qpeak_index[t]]
        if(t==len(non_zero_values)-1):
            break
        t+=1
print(result)
print(len(result))


# In[80]:

print("ppeak_indexes ppeaks")
#Find P
ppeak_index=[0 for i in range(len(non_zero_values))]
for i in range(len(non_zero_values)):
    ppeak_index[i]=qpeak_index[i]
for j in range(len(non_zero_values)):
    t=ppeak_index[j]
    for i in range(t-61,t):
        if(ecg_signal[i]>ecg_signal[ppeak_index[j]]):
            ppeak_index[j]=i
for i in range(len(non_zero_values)):
    print(ppeak_index[i],"\t",ecg_signal[ppeak_index[i]])
#append p peak with result list
t=0
for i in range(len(result)):
    if(beg+i==ppeak_index[t]):
        result[i]=ecg_signal[ppeak_index[t]]
        if(t==len(non_zero_values)-1):
            break
        t+=1
print('Result after adding p peaks')
print(result)
print(len(result))


# In[84]:

print("tpeak_indexes tpeaks")
#Find T
tpeak_index=[0 for i in range(len(non_zero_values))]
for i in range(len(non_zero_values)):
    tpeak_index[i]=speak_index[i]+10
for j in range(len(non_zero_values)-1):
    t=tpeak_index[j]
    for i in range(t,t+161):#window size 160
        if(abs(ecg_signal[i])>abs(ecg_signal[tpeak_index[j]])):
            tpeak_index[j]=i
for i in range(len(non_zero_values)):
    print(tpeak_index[i],"\t",abs(ecg_signal[tpeak_index[i]]))
#append t peak with result list
t=0
for i in range(len(result)):
    if(beg+i==tpeak_index[t]):
        result[i]=ecg_signal[tpeak_index[t]]
        if(t==len(non_zero_values)-1):
            break
        t+=1
print('Result after adding T peaks')
print(result)
print(len(result))


# In[85]:
for i in range(len(result)):
    if(result[i]!=0):
        result[i]+=0.7
plt.plot(ecg_signal[beg:end])
plt.grid(True)
plt.xlabel('Index')
plt.ylabel('Difference')
plt.show()
plt.plot(result,marker='.')
#plt.plot(ecg_signal[speak_index])
#plt.axhline(raw_filtered_rpeak)
#plt.axhline(average_positive+std_dev_positive)
#plt.axhline(average_positive+.5*std_dev_positive)

plt.xlabel('Index')
plt.ylabel('Difference')
plt.title('Differences between Consecutive ECG Channel Data Points')

plt.grid(True)
plt.show()


# In[ ]:


