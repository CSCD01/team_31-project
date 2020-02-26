import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mtick
import numpy as np

# original formatter
days = mdates.DayLocator()
days_fmt = mdates.DateFormatter('%D')
# for concise date formatter
date_locator = mdates.AutoDateLocator(minticks=6, maxticks=10)
cncs_fmt = mdates.ConciseDateFormatter(date_locator)
# for percent formatter
prcnt_locator = mtick.AutoLocator()
prcnt_fmt = mtick.PercentFormatter()

chinaDailyConfirmed = {"date":{"1":"2020-01-17","2":"2020-01-18","3":"2020-01-19","4":"2020-01-20","5":"2020-01-21","6":"2020-01-22","7":"2020-01-23","8":"2020-01-24","9":"2020-01-25","10":"2020-01-26","11":"2020-01-27","12":"2020-01-28","13":"2020-01-29","14":"2020-01-30","15":"2020-01-31","16":"2020-02-01","17":"2020-02-02","18":"2020-02-03","19":"2020-02-04","20":"2020-02-05","21":"2020-02-06","22":"2020-02-07","23":"2020-02-08","24":"2020-02-09","25":"2020-02-10","26":"2020-02-11","27":"2020-02-12"},"confirmed":{"1":62,"2":121,"3":198,"4":291,"5":440,"6":571,"7":830,"8":1287,"9":1975,"10":2744,"11":4515,"12":5974,"13":7711,"14":9692,"15":11791,"16":14380,"17":17205,"18":20438,"19":24324,"20":28018,"21":31161,"22":34546,"23":37198,"24":40171,"25":42638,"26":44653,"27":46472},"new cases":{"1":17,"2":59,"3":77,"4":93,"5":149,"6":131,"7":259,"8":457,"9":688,"10":769,"11":1771,"12":1459,"13":1737,"14":1981,"15":2099,"16":2589,"17":2825,"18":3233,"19":3886,"20":3694,"21":3143,"22":3385,"23":2652,"24":2973,"25":2467,"26":2015,"27":1819},"delta":{"1":"38","2":"95","3":"64","4":"47","5":"51","6":"30","7":"45","8":"55","9":"53","10":"39","11":"64","12":"32","13":"29","14":"26","15":"22","16":"22","17":"20","18":"19","19":"19","20":"15","21":"11","22":"11","23":"7.7","24":"8.0","25":"6.1","26":"4.7","27":"\/"}}

# fun style change
# plt.xkcd()

# automatically format the layout
plt.rcParams.update({'figure.autolayout': True})

# exatract data
dates = np.array(list(chinaDailyConfirmed['date'].values()), dtype='datetime64')
cases = list(chinaDailyConfirmed['new cases'].values())
deltas = list(chinaDailyConfirmed['delta'].values())

# setup plot
fig, axs = plt.subplots(figsize=(10, 6), nrows=2, ncols=1)

# plot first axes
axs[0].plot(dates, cases)

# format ticks
axs[0].xaxis.set_major_locator(date_locator)
axs[0].xaxis.set_major_formatter(cncs_fmt)

# set labels
axs[0].set(ylabel='Number of New Cases', title='Reported Cases of Coronavirus Over Time')

# plot second axes
axs[1].bar(dates, deltas)

# format ticks
axs[1].xaxis.set_major_locator(date_locator)
axs[1].xaxis.set_major_formatter(cncs_fmt)
axs[1].yaxis.set_major_locator(prcnt_locator)
axs[1].yaxis.set_major_formatter(prcnt_fmt)

# set labels
axs[1].set(ylabel='Delta of Reported Cases', title='Change In Reported Cases of Coronavirus Over Time')

plt.show()
