from pyecharts.charts import Bar
from pyecharts import options as opts
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar()
bar.set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例",subtitle="我是副标题"))
bar.add_xaxis(attr)
bar.add_yaxis("商家B",v1,stack=True)
bar.add_yaxis("商家A",v2,stack=True)
bar.render()
