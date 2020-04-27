from matplotlib import pyplot

pyplot.rcParams['font.family'] = 'Malgun Gothic'
pyplot.rcParams['font.size'] = 16
pyplot.rcParams['figure.figsize'] = (20, 10)

fig = pyplot.figure()
fig.suptitle('서브플롯 영역 나누기', fontsize=28, color='#006600')
fig.subplots_adjust(wspace=0.5, hspace=0.5)
ax1 = fig.add_subplot(2,3,1)
ax2 = fig.add_subplot(2,3,2)
ax3 = fig.add_subplot(2,3,3)
ax4 = fig.add_subplot(2,3,4)
ax5 = fig.add_subplot(2,3,5)
ax6 = fig.add_subplot(2,3,6)
                      
pyplot.show()



