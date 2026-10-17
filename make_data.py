#pandas：是Excel处理工具，random随机生成数。为了生成CSV文件
import pandas as pd
import random

# 我们自己假设一个公式，模拟萝卜快跑的时间
# 假设：1公里大概3分钟，堵车加时间，下雨下雪加时间，高峰期加时间
data_list = []

print("开始创建自己的数据...")

for i in range(100):
    # 随机生成特征
    dist = round(random.uniform(1.0, 20.0), 1)   # 距离1到20公里，保留一位小数
    traffic = random.randint(0, 10)              # 拥堵指数0-10
    weather = random.choice([0, 1, 2])           # 0晴天, 1下雨, 2下雪
    peak = random.choice([0, 1])                 # 0平时, 1早晚高峰
    
    # 自己设计的计算公式，加入随机误差更贴合实际
    base_time = dist * 3              #基础时间=距离*3min
    traffic_delay = traffic * 1.5     #堵塞时间，指数多1则多花1,5min
    weather_delay = weather * 2       #天气时间：下雨多2min，下雪多4min
    peak_delay = peak * 5             #高峰期，则额外多五分钟
    
    # 加上随机波动（比如遇到红绿灯多等了一会）
    noise = random.uniform(-1.5, 1.5) 
    
    final_time = base_time + traffic_delay + weather_delay + peak_delay + noise
    
    # 处理一下负数，保证时间最少了也有1分钟，如果小于1分钟，强制改为1分钟
    if final_time < 1.0:
        final_time = 1.0
    else:
        final_time = round(final_time, 1)
        
    data_list.append([dist, traffic, weather, peak, final_time])

# 组装成DataFrame格式
df = pd.DataFrame(data_list, columns=['distance_km', 'traffic_index', 'weather', 'is_peak', 'eta_min'])

# 存进csv文件
df.to_csv('robotaxi_data.csv', index=False)

print(f"成功！一共生成了 {len(df)} 条数据，文件名叫 robotaxi_data.csv")