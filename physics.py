# PHYSICS FORMULAS IN PYTHON
# 1. Acceleration =Change in  velocity/Time
  def acceleration(final_velocity-initial_velocity,time):
      return(final_velocity-initial_velocity)/time
# 2. Speed = Distance/Time
  def speed(distance.time):
      return(distance/time)
# 3. Force = Mass * Acceleration
  def force(mass,acceleration):
      return(mass*acceleration)
# 4. Potential Energy = Mass * Gravity * Height
  def potential_energy(mass,gravity,height):
      return(mass*gravity*height)
# 5. Kinetic Energy = 1/2 * Mass * Velocity^2
  def kinetic_energy(mass,velocity):
      return(0.5*mass*velocity**2)
# DISPLAY RESULTS
  print("PHYSICS FORMULAS")
  print("Acceleration:",acceleration(25,15,5),"m/s^2")
  print("Speed:",speed(200,40),"m/s")
  print("Force:",force(20,10),"N")
  print("Potiential Energy:",potiential_energy(10,9.8,20),"J")
  print("Kinetic Energy:",kinetic_energy(4,20)"J")
