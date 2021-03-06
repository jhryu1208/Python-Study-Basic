# Chapter01
# 파이썬 기초
# print 사용법

# [기본 출력]
## 작은 따옴표 - 주로 사용하는 것은 작옴따옴표 한쌍
print('Python Start!')
print('''Python Start!''')

## 큰 따옴표
print("Python Start!")
print("""Python Start!""")

## 줄바꿈
print()

# [separator 옵션]
print('P','Y','T','H','O','N',sep=',')
print('P','Y','T','H','O','N',sep='_')
print('P','Y','T','H','O','N',sep='|')
print('P','Y','T','H','O','N',sep='')
print('010','1111','2222',sep='-')
print('jhryu1208','gmail.com',sep='@')

print()

# [end 옵션]
## print문은 자동 줄바꿈을 지원하지만, 뒤에 end옵션이 붙으면  반복된 print문을 하나의 라인으로 이어준다.
print('Welcome to',end=' ')
print('IT NEWS',end=' ')
print('Web Site')

print()

# [file 옵션]
import sys
print('Learn Python', file=sys.stdout)

print()

# [format 사용 (d, s, f)]
## d : 정수, s : 문자열, f : 실수

## s는 문자열 하나를 대체 할 수 있다.
## %는 오른쪽의 값을 s에 각각 대입해주는 다리 역할을 한다.
print('%s %s' %('one','two'))

## {}는 s와 마찬가지로 문자열 하나를 대체 할 수 있다.
## 이때 {}를 사용하면, format함수를 이용하여 mapping할 수 있다.
print('{} {}'.format('one','two'))

## {}사이에 숫자를 넣어주면 배열의 순서를 지정한 것과 같다.
## {}사이에 순서를 넣지않으면 암묵적으로 {0} {1} {2} ... 와 같이 지정된다.
## 결론적으로, 아래와 같은 방식으로 순서를 지정해서 출력할 수 있다.
## 따라서 다음과같이 {1} {0} 으로 할 경우, format함수에서 1번째 값이 먼저 출력되고 0번쨰값이 나중에 출력된다.
print('{1} {0}'.format('one','two'))

print()

# [%s]
## _ _ _ _ _ _ n i c e
print('%10s'%('nice'))
## 10자리를 확보하고 nice로 format
print('{:>10}'.format('nice'))

## n i c e _ _ _ _ _ _
print('%-10s'%('nice'))
print('{:10}'.format('nice'))

## >왼쪽의 기호를 문자열을 제외한 공백에 출력한다
## ______nice
print('{:_>10}'.format('nice'))

## :^는 중앙정렬
print('{:^10}'.format('nice'))

## %.숫자 : 원하는 자릿수만큼 출력
print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
print('%5s' % ('pythonstudy'))
## 공간은 10개가 있고, 왼쪽부터 5개만 출력한다.
print ("{:10.5}".format('pythonstudy'))

print()

## [%d]
print ('%d %d'%(1,2))
print ('{} {}'.format(1,2))

## _ _ 4 2
print ('%4d'%(42))
print ('{:4d}'.format(42))

print()

# [%f]
## %정수부.소수부f
## 전부다 있는 그대로 출력x
print('%f' % (3.141521341231412412))
## :f를 안쓸경우 모든 수가 출력된다.
print('{:f}'.format(3.141521341231412412))

## 정수부 한자리, 소수부 8자리
print('%1.8f' % (3.141521341231412412))
## 정수부 한자리, 소수부 18자리
print('%1.18f' % (3.141521341231412412))

## _ _ _ _ _ _
## 0 0 3 . 1 4 , 총 6자리 중에서 소숫점 2자리까지
print('%06.2f'%(3.141521341231412412))
print('{:06.2f}'.format(3.141521341231412412))

print()
