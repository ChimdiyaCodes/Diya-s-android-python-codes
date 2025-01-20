heart_rate= int (input("Enter your heart rate: ")) #taking the user's heart rate'
if heart_rate < 60: 
  print("LOW HEART RATE, SEE YOUR DOCTOR!")
elif heart_rate >= 100: 
  print("HIGH HEART RATE, SEE YOUR DOCTOR!")
else:
  print("CONGRATULATIONS, YOUR HEART RATE IS NORMAL!")