weight = 41.5
#ground shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping:", cost_ground)

cost_ground_premium = 125.00
 
print("Ground Shipping Premium: ", cost_ground_premium)
# drone shipping
if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

print("Drone Shipping: ", cost_drone )

#What is the cheapest method of shipping a 4.8 pound package and how much would it cost?
#answer: ground shipping

#What is the cheapest method of shipping a 41.5 pound package and how much would it cost?
#answer: ground shipping premium