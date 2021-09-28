HLine=['KimNamjoon',"KimSeokjin",'MinYoongi','JungHoseok']
Sname=['RM','Jin','Suga','JHope']
BD=['12-09-1994','05-12-1992','09-03-1993','18-02-1994']
BTS=zip(HLine,Sname,BD)
for rn,sn,bd in BTS:
    print("%s's stage name is %s,and Birtdate is %s."%(rn,sn,bd))
