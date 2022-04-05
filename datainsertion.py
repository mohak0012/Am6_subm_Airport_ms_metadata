import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="airport_ms"
)

mycursor = mydb.cursor()

sql = " INSERT INTO airport_consists_of (air_id, a_name) VALUES (%s, %s) "
val = [
  # ('GF 872', 'Agra Airport'),
  # ('AI 328', 'Agra Airport'),
  # ('VS 378', 'Agra Airport')
  # ('AA 783', 'Sardar Vallabhbhai Patel International Airport'),
  # ('TJ 372', 'Sardar Vallabhbhai Patel International Airport'),
  # ('SD 272', 'Sardar Vallabhbhai Patel International Airport')
  # ('QA 327', 'Aktau Airport'),
  # ('EA 595', 'Aktau Airport'),
  # ('AA 457', 'Aktau Airport')
  # ('AA 567', 'Alaminos Airport'),
  # ('FA 367', 'Alaminos Airport'), 
  # ('QA 849', 'Alaminos Airport'), 
  # ('SC 748', 'Balqash Airport'),
  # ('ZA 787', 'Balqash Airport'),
  # ('CB 587', 'Balqash Airport'),
  # ('CP 547', 'Berlin Brandenburg Airport'), 
  # ('PE 032', 'Berlin Brandenburg Airport')	, 
  # ('PP 272', 'Berlin Brandenburg Airport'), 
  # ('PA 237', 'Brussels South Charleroi Airport'), 
  # ('PA 049', 'Brussels South Charleroi Airport'), 
  # ('SA 239', 'Brussels South Charleroi Airport'),
  # ('KA 348', 'Chongju International Airport'), 
  # ('AB 438', 'Chongju International Airport'), 
  # ('JA 161', 'Chongju International Airport'), 
  # ('JA 367', 'Enrique Adolfo Jiménez Airport'), 
  # ('AK 739', 'Enrique Adolfo Jiménez Airport'), 
  # ('KE 283', 'Enrique Adolfo Jiménez Airport'),
  # ('AC 873', 'Frankfurt Airport'), 
  # ('AG 230', 'Frankfurt Airport'),
  # ('BP 527', 'Frankfurt Airport'),
  # ('AN 249', 'Penang International Airport'),
  # ('SA 378', 'Penang International Airport'),
  # ('IA 234', 'Penang International Airport'),
  # ('SA 342', 'Gwalior Airport'), 
  # ('AC 837', 'Gwalior Airport'),
  # ('AI 123', 'Gwalior Airport'),
  # ('GA 478', 'Jose Marti International Airport'),
  # ('IG 213', 'Jose Marti International Airport'),
  # ('JA 344', 'Jose Marti International Airport'),
  # ('LA 987', 'Hyderabad Domestic Airport'),
  # ('SJ 434', 'Hyderabad Domestic Airport'),
  # ('GF 872', 'Hyderabad Domestic Airport'),
  # ('AI 328', 'Jaipur International Airport'),
  # ('VS 378', 'Jaipur International Airport'),
  # ('AA 783', 'Jaipur International Airport'),
  # ('TJ 372', 'Jodhpur Airport'),
  # ('SD 272', 'Jodhpur Airport'),
  # ('QA 327', 'Jodhpur Airport'),
  # ('EA 595', 'Senai International Airport'),
  # ('AA 457', 'Senai International Airport'),
  # ('AA 567', 'Senai International Airport'),
  # ('FA 367', 'Hamid Karzai International Airport'), 
  # ('QA 849', 'Hamid Karzai International Airport'), 
  # ('SC 748', 'Hamid Karzai International Airport'),
  # ('ZA 787', 'Jinnah International Airport'),
  # ('CB 587', 'Jinnah International Airport'),
  # ('CP 547', 'Jinnah International Airport'), 
  # ('PE 032', 'Tribhuvan International Airport')	, 
  # ('PP 272', 'Tribhuvan International Airport'), 
  # ('PA 237', 'Tribhuvan International Airport'), 
  # ('PA 049', 'Kota Airport'), 
  # ('SA 239', 'Kota Airport'),
  # ('KA 348', 'Kota Airport'), 
  # ('AB 438', 'Allama Iqbal International Airport'), 
  # ('JA 161', 'Allama Iqbal International Airport'), 
  # ('JA 367', 'Allama Iqbal International Airport'), 
  # ('AK 739', 'Los Angeles Intrnational Airport'), 
  # ('KE 283', 'Los Angeles Intrnational Airport'),
  # ('AC 873', 'Los Angeles Intrnational Airport'), 
  # ('AG 230', 'Chaudhary Charan Singh International Airport'),
  # ('BP 527', 'Chaudhary Charan Singh International Airport'),
  # ('AN 249', 'Chaudhary Charan Singh International Airport'),
  # ('SA 378', 'Manpo Airport'),
  # ('IA 234', 'Manpo Airport'),
  # ('SA 342', 'Manpo Airport'), 
  # ('AC 837', 'Mawlamyine Airport'),
  # ('AI 123', 'Mawlamyine Airport'),
  # ('GA 478', 'Mawlamyine Airport'),
  # ('IG 213', 'Melbourne Airport'),
  # ('JA 344', 'Melbourne Airport'),
  # ('LA 987', 'Melbourne Airport'),
  # ('SJ 434', 'Mexicali International Airport'),
  # ('AI 328', 'Mexicali International Airport'),
  # ('VS 378', 'Mexicali International Airport'),
  # ('AA 783', 'Mexico City International Airport'),
  # ('TJ 372', 'Mexico City International Airport'),
  # ('SD 272', 'Mexico City International Airport'),
  # ('QA 327', 'Monterrey International Airport'),
  # ('EA 595', 'Monterrey International Airport'),
  # ('AA 457', 'Monterrey International Airport'),
  # ('AA 567', 'Monterrey International Airport'),
  # ('FA 367', 'Chhatrapati Shivaji Maharaj International Airport'), 
  # ('QA 849', 'Chhatrapati Shivaji Maharaj International Airport'), 
  # ('SC 748', 'Chhatrapati Shivaji Maharaj International Airport'),
  # ('ZA 787', 'Indira Gandhi International Airport'),
  # ('CB 587', 'Indira Gandhi International Airport'),
  # ('CP 547', 'Indira Gandhi International Airport'), 
  # ('PE 032', 'John F. Kennedy International Airport'), 
  # ('PP 272', 'John F. Kennedy International Airport'), 
  # ('PA 237', 'John F. Kennedy International Airport'), 
  # ('PA 049', 'Paris-Le Bourget Airport'), 
  # ('SA 239', 'Paris-Le Bourget Airport'),
  # ('KA 348', 'Paris-Le Bourget Airport'), 
  # ('AB 438', 'Pokhara International Airport'), 
  # ('JA 161', 'Pokhara International Airport'), 
  # ('JA 367', 'Pokhara International Airport'), 
  # ('AK 739', 'Pyay Airport'), 
  # ('KE 283', 'Pyay Airport'),
  # ('AC 873', 'Pyay Airport'), 
  # ('AG 230', 'Pyongyang Sunan International Airport'),
  # ('BP 527', 'Pyongyang Sunan International Airport'),
  # ('AN 249', 'Pyongyang Sunan International Airport'),
  # ('SA 378', 'Quetta International Airport'),
  # ('IA 234', 'Quetta International Airport'),
  # ('SA 342', 'Quetta International Airport'), 
  # ('AC 837', 'Rome-Fiumicino International Airport'),
  # ('AI 123', 'Rome-Fiumicino International Airport'),
  # ('GA 478', 'Rome-Fiumicino International Airport'),
  # ('IG 213', 'St. Cloud Regional Airport'),
  # ('JA 344', 'St. Cloud Regional Airport'),
  # ('LA 987', 'St. Cloud Regional Airport'),
  # ('SJ 434', 'Sydney Airport'),
  # ('GF 872', 'Sydney Airport'),
  # ('AI 328', 'Sydney Airport'),
  # ('VS 378', 'Tijuana International Airport'),
  # ('AA 783', 'Tijuana International Airport'),
  # ('TJ 372', 'Tijuana International Airport'),
  # ('SD 272', 'Haneda Airport'),
  # ('QA 327', 'Haneda Airport'),
  # ('EA 595', 'Haneda Airport'),
  # ('AA 457', 'Vadodara Airport'),
  # ('AA 567', 'Vadodara Airport'),
  # ('FA 367', 'Vadodara Airport'), 
  # ('QA 849', 'El Lencero Airport'), 
  # ('SC 748', 'El Lencero Airport'),
  # ('ZA 787', 'El Lencero Airport')
]

# Agra Airport
#  Sardar Vallabhbhai Patel International Airport    
#  Aktau Airport                                     
#  Alaminos Airport                                  
#  Balqash Airport                                   
#  Berlin Brandenburg Airport                        
#  Brussels South Charleroi Airport                  
#  Chongju International Airport                     
#  Enrique Adolfo Jiménez Airport                    
#  Frankfurt Airport                                 
#  Penang International Airport                      
#  Gwalior Airport                                   
#  Jose Marti International Airport                  
#  Hyderabad Domestic Airport                        
#  Jaipur International Airport                      
#  Jodhpur Airport                                   
#  Senai International Airport                       
#  Hamid Karzai International Airport                
#  Jinnah International Airport                      
#  Tribhuvan International Airport                   
#  Kota Airport                                      
#  Allama Iqbal International Airport                
#  Los Angeles Intrnational Airport                  
#  Chaudhary Charan Singh International Airport      
#  Manpo Airport                                     
#  Mawlamyine Airport                                
#  Melbourne Airport         

#  Mexicali International Airport                    
#  Mexico City International Airport                 
#  Monterrey International Airport                   
#  Chhatrapati Shivaji Maharaj International Airport 
#  Indira Gandhi International Airport               
#  John F. Kennedy International Airport             
#  Paris-Le Bourget Airport                          
#  Pokhara International Airport                     
#  Pyay Airport                                      
#  Pyongyang Sunan International Airport             
#  Quetta International Airport                      
#  Rome-Fiumicino International Airport              
#  St. Cloud Regional Airport                        
#  Sydney Airport                                   
#  Tijuana International Airport                    
#  Haneda Airport                                   
#  Vadodara Airport                                  
#  El Lencero Airport

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")