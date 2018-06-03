def read_sanguo_file():
    with open("sanguo.txt", encoding="gb18030") as f:
        data = f.read()
    return data.replace('\n','')

def make_chinese_plot_ready():
    from matplotlib import rcParams
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']
    rcParams['axes.unicode_minus'] = False
    
def draw_dict(mydict, figsize=(8, 5)):
    import pandas as pd
    import matplotlib.pyplot as plt
    make_chinese_plot_ready()
    df = pd.DataFrame(list(mydict.items()), columns=['name', 'times'])
    df.set_index('name')['times'].sort_values(ascending=False).plot(kind='bar', figsize=figsize)
    plt.tight_layout()
