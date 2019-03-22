from matplotlib import pyplot as plt

class LineBuilder:
	def __init__(self, line):
		self.line = line
		self.xs = list(line.get_xdata())
		self.ys = list(line.get_ydata())
		self.cid = line.figure.canvas.mpl_connect('button_press_event', self)

	def __call__(self, event):
		print('click', event)
		print(self.line.axes)
		if event.inaxes!=self.line.axes: return
		if event.dblclick:
			labels = ['A','B','C','D','E','F']
			sizes = [23, 10, 67, 83,19,7]
			colors = ['#d3d19e','#d29daa','#d3d19e','#d29daa','#d3d19e','#d29daa']
			fig1,ax1 = plt.subplots()
			ax1.pie(sizes,labels=labels,colors=colors, autopct='%1.1f%%', startangle=90)
			ax1.axis('equal')
			plt.tight_layout()
			plt.show()

fig = plt.figure()
labels = ['Pie1','Pie2','Pie3','Pie4']
sizes = [15, 30, 45, 10]
ax = fig.add_subplot(111)
colors=['#eaebed','#edbbaf','#62adbc','#efc6ef']
ax.pie(sizes,labels=labels,colors=colors, autopct='%1.1f%%',startangle=90)
ax.set_title('Double-click to view details')
line, = ax.plot([0], [0])  # empty line
linebuilder = LineBuilder(line)

plt.show()