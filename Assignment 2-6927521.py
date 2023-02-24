#Code for a car business
carsAvailable={
    'Acura Integra':'380,000',
    'Acura Tlx':'825,000',
    'Audi A6':'730,000',
    'Audi TT':'650,000',
    'Bentley Bentayga':'900,000',
    'Bentley Continental Gt':'920,000',
    'Bugatti Chiron':'35,000,000',
    'Bugatti Veyron':'20,000,000',
    'Bugatti La Voiture Noire':'100,000,000',
    'BMW i8':'1,900,000',
    'Dodge Challenger':'400,000',
    'Dodge Charger':'420,000',
    'Honda Civic':'120,000',
    'Hyundai Elantra':'130,000',
    'lamborghini Aventador':'10,800,000',
    'lamborghini Huracan':'8,600,000',
    'lamborghini Urus':'1,850,000',
    'czz':'950000',
    'Mclaren Speedtail':'900,000',
    'Mercedes Benz AMG':'900,000',
    'Mercedes Benz S':'1,900,000',
    'Nissan Supra':'700,000',
    'Pagani Zonda':'11,000,000',
    'Pagani Huayra':'17,000,000',
    'Toyota Corrola':'150,000',
    'Toyota Camry':'200,000',
    'Toyota Prius':'130,000',
    'Toyota Highlander':'680,000',
    'Toyota Landcruiser Prado':'700,000',
    'Toyota Vitz':'90,000'}
customer=(input('Hello!!! Welcome to CarWorld. \nWhat car do you wish to purchase;'))
if customer in carsAvailable:
    print('The price of a ' + str(customer)+' is GHS'+str(carsAvailable[customer]))
else: print('Sorry, This car is not available at the moment.')

#https://github.com/Henryadj3