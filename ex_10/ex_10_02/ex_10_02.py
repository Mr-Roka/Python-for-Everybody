time_count={}
file=open('mbox-short.txt')

for f in file:
    if f.startswith('From '):
        sp=f.split()
        #print(sp)
        full_time=sp[5]
        #print(full_time)
        sptime=full_time.split(':')
        hour=sptime[0]
        #print(hour)

        if hour in time_count:
            time_count[hour]+=1
        else:
            time_count[hour]=1


for hour in sorted(time_count.keys()):
    print(hour, time_count[hour])