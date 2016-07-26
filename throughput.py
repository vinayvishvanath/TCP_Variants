
import matplotlib.pyplot as plt
def throughput():
        global thoughtput
        file='testnupoor.tr'
        #print 'FILE', file
        f=open(file)
        lines=f.readlines()
        #print lines
        f.close()
        received_packet1=0
        received_packet2=0
        start_received_time1=10.0
        start_received_time2=10.0
        end_time1=0.0
        end_time2=0.0
        through_list=[]
        through_list1=[]
        x=0.5
        y=0.5
	time_list=[]
        for k in lines:
                #print k
                n=k.split()
                if n[7]=="1":
                        if n[0]== "r" and  n[3]== "4" and n[4]=="tcp" :
                                        received_packet1=received_packet1+int(n[5])
                                        end_time1=float(n[1])
                                        #print end_time1,type(end_time1)
                        if  float(n[1])>=x:
				#print 'time', n[1]
				time_list.append(n[1])
                                through=received_packet1*8/(float(n[1])*1000000)
                                through_list.append(through)
                                x+=0.5

                if n[7]=="2":
                        if n[0]=="r" and n[2]=="1" and n[10]=="0":
                                        #if float(n[1])<received_time:
                                                start_received_time2=float(n[1])
                                                #print 'received_time', start_received_time2

                        if n[0]== "r" and  n[3]== "5" and n[4]== "cbr" :
                                        received_packet2=received_packet2+int(n[5])
                                        end_time2=float(n[1])
                                        #print 'end_time2',end_time2
                        if n[1]>=y:
                                through1=received_packet1*8/(float(n[1])*1000000)
                                through_list1.append(through1)
                                y+=0.5


        #print 'end_time1',end_time1
        #print 'received_time1',start_received_time1
        #print 'end_time2',end_time2
        #print 'received_time2',start_received_time2
        time1=(end_time1-start_received_time1)*1000000
        #print 'time',time1
        thoughput1=received_packet1*8/(float(time1))
        #print 'throughput',throughput1
        time2=(end_time2-start_received_time2)*1000000
        throughput2=received_packet2*8/(float(time2))
        print 'throughlist',through_list, len(through_list)
	print 'time1',time_list
        #print 'throughlist1',through_list1
        #return str(through_list) + '\t' + str(through_list1)

throughput()
plt.plot(time_list,through_list)
plt.show()
