datas = {'A001':['小熊軟糖', 20],'A002':['冰棒',25],
          'A004':['王子麵',10],'A006':['汽水',30]}
while True:
    ans=int(input("1.查詢貨號 or 2.結束查詢系統"))
    
    if ans==1:
            
            num=input("請輸入貨號：")
            if num not in datas:
                print("此貨號不存在")
                new=input("請問是否新增此貨號(yes or no)")
                
                if new=="yes":
                    name=input("請輸入品項名稱:")
                    price=int(input("請輸入價錢:"))
                    datas[num]=[name,price]
                    
                    print(f"貨號：{num}","品項：{} 價格：{}元".format(datas[num][0],datas[num][1]))                        
                else:
                    pass
                
            else:
                print('品項：{} 價格：{}元'.format(datas[num][0],datas[num][1]))
                


    elif ans==2:
            break
    else:
            print('輸入錯誤，請重新輸入! 1.繼續查詢下筆貨號 or 2.結束查詢系統')
