from vpython import *

class Projectile:

  def __init__(self, v0, θ, dt) -> None:
    self.__m = 1
    self.__g = vector(0, -9.8, 0)
    self.__θ = θ * pi/180
    self.__v = v0 * vector(cos(self.__θ), sin(self.__θ), 0)
    self.__F = self.__m * self.__g
    self.__p = self.__m * self.__v
    self.__r = vector(0, 0, 0)
    self.__dt = dt
    self.__t = 0
    self.__trajectory = []

  def simulate(self) -> None:
      while self.__r.y >= 0:
        self.__F = self.__m * self.__g
        self.__p += self.__F * self.__dt
        self.__r += self.__p * self.__dt / self.__m
        self.__t += self.__dt 
        self.__trajectory.append((self.__r, self.__t))
  

  def plot(self) -> None:
    plot_curve = gcurve(color=color.blue)
    for (positionVector, time) in self.__trajectory:
      plot_curve.plot(positionVector.x, positionVector.y)
  
  # Numerical x range
  def nxrange(self) -> float:
    if self.__trajectory:
      return self.__trajectory[-1][0].x
    
    return 0
  
  # Theoretical x range
  def txrange(self) -> float:
    return (mag(self.__v)**2) * sin(2 * self.__θ) / mag(self.__g)

  # Numerical maximum height
  def nmaxH(self) -> float:
    maxH = 0
    for (positionVector, time) in self.__trajectory:
      if (positionVector.y > maxH):
        maxH = positionVector.y
    
    return maxH
  
  # Theoretical maximum height
  def tmaxH(self) -> float:
    return (mag(self.__v) * sin(self.__θ))**(2) / (2 * mag(self.__g))
  
  # Numerical flight time
  def nflightT(self) -> float:
    if self.__trajectory:
      return self.__trajectory[-1][1]
    
    return 0
  
  # Theoretical flight time
  def tflightT(self) -> float:
    return 2 * mag(self.__v) * sin(self.__θ) / mag(self.__g)


if __name__ == "__main__":
  proj = Projectile(
    v0 = 25, # in m/s
    θ = 45, # in degrees
    dt = 0.001  # in seconds
  )
  proj.simulate()
  proj.plot()
  print("numerical x range=", proj.nxrange())
  print("theoretical x range=", proj.txrange())
  print("numerical maximum height=", proj.nmaxH())
  print("theoretical maximum height=", proj.tmaxH())
  print("numerical flight time=", proj.nflightT())
  print("theoretical flight time=", proj.tflightT())