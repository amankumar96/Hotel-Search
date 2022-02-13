class Hotel5Stars:

    def __init__(self, name , area, price, rating):
        self.name = name
        self.area = area
        self.price = price
        self.rating = rating






# Hotel of Delhi
Radison = Hotel5Stars('Radison blu Plaza', 'Delhi airport', 5000, 5)
ibis = Hotel5Stars('ibis Hotel', 'South West ', 2894, 4)
Novotel = Hotel5Stars('Novotel Hotel', 'South West', 4200, 5)
Holiday_inn = Hotel5Stars('Holiday Inn', 'South West', 4099, 5)
Taj_hotel = Hotel5Stars('Taj HOtel', 'Chanakayapuri', 6750, 5)
Aira_xing = Hotel5Stars('Hotel Aira Xings', 'Paharganj', 699, 3)
Shangri_la= Hotel5Stars('Shangri la Hotel', 'Central Delhi', 6500, 5)
Eros = Hotel5Stars('Eros Hotel', 'Nehru Place', 4600, 5)
Viva_palace = Hotel5Stars('Hotel Viva Palace', 'Mahipalpur', 1036, 4)
park = Hotel5Stars('The Park', 'Central Delhi', 4199, 5)

#Hotel of Goa
Aaria = Hotel5Stars('Aaria Residency', 'Arambol beach', 2280, 3)
Surya_kiran = Hotel5Stars('Surya kiran Residency', 'Miramer beach', 4400, 4)
Tiracol = Hotel5Stars('Fort Tiracol', 'Arambol', 7450, 5)
Altrude = Hotel5Stars('Altrude by the sea', 'Candolim beach', 4275, 3)
Crescent = Hotel5Stars('The Crescent', 'Miramer Beach', 3550, 4)

list_hoteldelhi = [Radison.name ,
                   ibis.name,
                   Novotel.name,
                   Holiday_inn.name,
                   Taj_hotel.name,
                   Aira_xing.name,
                   Shangri_la.name,
                   Eros.name,
                   Viva_palace.name,
                   park.name]

list_hotelgoa = [Aaria.name,
                 Surya_kiran.name,
                 Tiracol.name,
                 Altrude.name,
                 Crescent.name]


location = input('location: ')


def Hotelname():

    if (location == 'Delhi'):
        print(list_hoteldelhi)
    elif (location == 'Goa'):
        print(list_hotelgoa)
    else:
        print('Hotel not available')



def Hotel_details():
    name = input('please tell your hotel name: ')
    if (name== Radison.name):
        print(f'{Radison.name}, is located near {Radison.area}, the price per day is Rs {Radison.price}, and is rated {Radison.rating} out of 5')

    elif (name == ibis.name):
        print((f'{ibis.name}, is located near {ibis.area}, the price per day is Rs {ibis.price}, and is rated {ibis.rating} out of 5'))

    elif (name == Novotel.name):
        print((f'{Novotel.name}, is located near {Novotel.area}, the price per day is Rs {Novotel.price}, and is rated {Novotel.rating} out of 5'))

    elif (name == Holiday_inn.name):
        print(((f'{Holiday_inn.name}, is located near {Holiday_inn.area}, the price per day is Rs {Holiday_inn.price}, and is rated {Holiday_inn.rating} out of 5')))

    elif (name == Taj_hotel.name):
        print((f'{Taj_hotel.name}, is located near {Taj_hotel.area}, the price per day is Rs {Taj_hotel.price}, and is rated {Taj_hotel.rating} out of 5'))
    elif (name == Aira_xing.name):
        print((f'{Aira_xing.name}, is located near {Aira_xing.area}, the price per day is Rs {Aira_xing.price}, and is rated {Aira_xing.rating} out of 5'))
    elif(name == Shangri_la.name):
        print((f'{Shangri_la.name}, is located near {Shangri_la.area}, the price per day is Rs {Shangri_la.price}, and is rated {Shangri_la.rating} out of 5'))
    elif (name == Eros.name):
        print((f'{Eros.name}, is located near {Eros.area}, the price per day is Rs {Eros.price}, and is rated {Eros.rating} out of 5'))
    elif (name == Viva_palace.name):
        print((f'{Viva_palace.name}, is located near {Viva_palace.area}, the price per day is Rs {Viva_palace.price}, and is rated {Viva_palace.rating} out of 5'))
    elif (name == Aaria.name ):
        print((f'{Aaria.name}, is located near {Aaria.area}, the price per day is Rs {Aaria.price}, and is rated {Aaria.rating} out of 5'))
    elif(name == Surya_kiran.name):
        print((f'{Surya_kiran.name}, is located near {Surya_kiran.area}, the price per day is Rs {Surya_kiran.price}, and is rated {Surya_kiran.rating} out of 5'))
    elif (name == Tiracol.name):
        print((f'{Tiracol.name}, is located near {Tiracol.area}, the price per day is Rs {Tiracol.price}, and is rated {Tiracol.rating} out of 5'))
    elif(name == Altrude.name):
        print((f'{Altrude.name}, is located near {Altrude.area}, the price per day is Rs {Altrude.price}, and is rated {Altrude.rating} out of 5'))
    elif(name == Crescent.name):
        print((f'{Crescent.name}, is located near {Crescent.area}, the price per day is Rs {Crescent.price}, and is rated {Crescent.rating} out of 5'))
    else:
        print('hotel not present')
