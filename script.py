import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
xTenth = []


xAxis = list(range(-20,20))
for x in xAxis:

  xTenth.append(x*0.1)

xAxis = xTenth

def parabola(xValues):

  yValues = []

  for x in xValues:

    y = x*x

    yValues.append(y)

  return yValues


yAxis = parabola(xAxis)

sliceXAxis  = xAxis[:]
sliceYAxis  = yAxis[:]

style = 'ro'

plt.plot(sliceXAxis , sliceYAxis , style)

plt.axis([-2, 2, 0, 4])

filename = 'graph.png'

plt.savefig(filename)