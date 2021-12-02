#연극 종류 선택
play = ['파수꾼', '리투아니아', '춤추며 간다', '고도를 기다리며', '햄릿']
print()
print('========== 연극 목록 ==========')
for i in play:
    print(i)
print('===============================')
print()

title = input('예매하실 연극을 입력해주세요: ')
while title not in play:
    print('예매할 수 없는 연극입니다.')
    title = input('예매하실 연극을 입력해주세요: ')

print('관람할 연극은 %s입니다.' %title)
print()
print()


#연극 날짜 선택
파수d = ['12/1', '12/2', '12/3', '12/4', '12/5']
리투d = ['11/29', '11/30', '12/1', '12/2', '12/3']
춤추d = ['12/16', '12/17', '12/18', '12/19', '12/20']
고도d = ['12/26', '12/27', '12/28', '12/29', '12/30']
햄릿d = ['12/7', '12/8', '12/9', '12/10', '12/11']
days = {'파수꾼':파수d, '리투아니아':리투d, '춤추며 간다':춤추d, '고도를 기다리며':고도d, '햄릿':햄릿d}

print()
print('========== 연극 날짜 ==========')
for i in days.get(title):
    print(i)
print('===============================')
print()

days2 = days.get(title)
date = input('관람하실 날짜를 입력해주세요: ')
while date not in days2:
    print('관람할 수 없는 날짜입니다.')
    date = input('관람하실 날짜를 입력해주세요: ')

print('관람할 날짜는 %s입니다.' %date)
print()
print()


#연극 시간 선택
파수t = ['13시', '18시']
리투t = ['15시', '20시']
춤추t = ['11시', '16시']
고도t = ['12시', '17시']
햄릿t = ['13시', '20시']
timetale = {'파수꾼':파수t, '리투아니아':리투t, '춤추며 간다':춤추t, '고도를 기다리며':고도t, '햄릿':햄릿t}

print()
print('========== 연극 시간 ==========')
for i in timetale.get(title):
    print(i)
print('===============================')
print()
timetale2 = timetale.get(title)
time = input('관람하실 시간을 입력해주세요: ')
while time not in timetale2:
    print('관람할 수 없는 시간입니다.')
    time = input('관람하실 시간을 입력해주세요: ')

print('관람할 시간은 %s입니다.' %time)
print()
print()


#관람 인원 수
print()
people = int(input('관람 인원 수를 입력해주세요: '))
while people < 1:
    print('관람 인원 수는 양수만 입력가능합니다.')
    people = int(input('관람 인원 수를 입력해주세요: '))

print('관람할 인원수는 %d명 입니다.' %people)
print()
print()


#할인 여부
print()
coupon = {'1천원 할인 쿠폰':1000, '2천원 할인 쿠폰':2000, '3천원 할인 쿠폰':3000}
use = input('할인권을 이용하시려면 y, 금액 확인으로 넘어가시려면 n을 입력해주세요: ')
while True:
    if use=='y':
        print()
        print('할인권을 사용합니다.')
        print("=========== 할인권 ===========")
        for i in list(coupon.keys()):
            print(i)
        print("==============================")
        print()
        coupon_input = input("할인권을 입력해주세요: ")
        if coupon_input in coupon:
            print("%d원이 할인됩니다." %(coupon[coupon_input]))
            sale = coupon[coupon_input]
            del coupon[coupon_input]
            print('남은 할인권:', list(coupon))
            break

        else:
            print("존재하지 않는 할인권입니다.") 
        
    elif use=='n':
        sale = 0
        print("할인권을 사용하지 않습니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        use = input("할인권을 이용하시려면 y, 금액 확인으로 넘어가시려면 n을 입력해주세요: ")
print()
print()


#연극 가격 계산
price = {'파수꾼':20000, '리투아니아':25000, '춤추며 간다':15000, '고도를 기다리며':30000, '햄릿':35000}
or_price = int(price[title])
sale_price = sale
total_price = (or_price-sale_price)*people+1000
print()
print()

#연극 예매 상세 내역 출력
print('=============== 예매 상세 내역 ================')
print()
print('연극 제목 : %s' %title)
print('관람 일자 : %s' %date)
print('관람 시간 : %s' %time)
print('관람 인원 : %d 명' %people)
print('금액 : %d 원' %(or_price*people))
print('수수료 : 1000 원')
print('할인 금액 : %d 원' %(sale_price))
print()
print('-----------------------------------------------')
print()
print('총 결제 금액 : %d' %(total_price))
print()
print('===============================================')



   


        






        





