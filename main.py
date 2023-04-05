from time import sleep


print("здравствуй новый пользователь")
name=input("как тебя зовут? ")
print("приятно познакомиться, "+name)
sleep(2)
age=input("сколько тебе лет? ")
print("прикольно что тебе "+age+" лет") 
age_old=int(age)
age_old+=10
sleep(2)
print("через 10 лет тебе будет ", age_old)
sleep(2)
hobby=input("чем ты увлекаешься? пиши в Именительном падеже: ")
print("мне тоже нравится "+hobby)
sleep(2)
zodiak=input("какой у тебя знак зодиака? ")
print("круто что ты "+zodiak+" а я дракон")
sleep(2)
print("сегодня я узнала о тебе: тебя зовут "+name+" тебе "+age+" лет. ты любишь "+hobby+" а по знаку зодиака ты "+zodiak)   
sleep(2)    
right=input("все верно? ")
print("хех, я старалась")