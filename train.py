import pandas as pd  #处理表格数据
import mlflow        #记录每次实验成绩
import mlflow.sklearn
import joblib       #把训练好的模型打包成 .pkl文件的
from sklearn.model_selection import train_test_split  #做机器学习的工具箱
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

print("1. 正在读取刚才自己创造的数据...")
# 把咱们刚才造的表格读进来
my_data = pd.read_csv('robotaxi_data.csv')

# 把前四列作为特征（题目），最后一列作为预测目标（答案）
features = ['distance_km', 'traffic_index', 'weather', 'is_peak']
X = my_data[features]
y = my_data['eta_min']

# 把数据切分成两份：80条用来当模型学习，20条留着用来测试
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 设定 MLflow 实验的名字
mlflow.set_experiment("Lobo_ETA_Experiment")

# 准备好两个模型来PK：一个是简单版的线性回归，一个是高级版的随机森林
model_dict = {
    "Baseline_Linear": LinearRegression(),
    "Improved_RandomForest": RandomForestRegressor(n_estimators=10, random_state=42)
}

best_error = 99999  # 先设定一个很大的误差，用来找最小的
best_model_name = None

print("2. 开始对比两个模型...")
for name, model in model_dict.items():
    print(f"正在训练模型：{name} ...")
    
    with mlflow.start_run(run_name=name):
        # 让模型学习
        model.fit(X_train, y_train)
        
        # 拿测试题考考它，看它预测得准不准
        preds = model.predict(X_test) 
        
        #算一下误差（MAE：平均绝对误差，越小越好）
        error = mean_absolute_error(y_test, preds)
        print(f"--> {name} 的平均误差是: {error:.2f} 分钟")
        
        # 把这次训练的参数、成绩记到 MLflow 上：它会在本地 mlruns 文件夹里帮我们建立一个数据库。记录了每次实验的参数（模型类型）、指标（MAE 误差）以及模型本体。在 UI 界面里，我可以直观地看出哪个模型误差更小，从而决定最终上线哪个模型
        mlflow.log_param("model_type", name)
        mlflow.log_metric("MAE_error", error)
        # 为了保存模型，需要加信任参数才跑通
        mlflow.sklearn.log_model(model, "model", skops_trusted_types=["sklearn.tree._tree.Tree"])
        
        # 如果这个模型误差比之前的小，就把它留下来当成功模型
        if error < best_error:
            best_error = error
            best_model_name = name

# 把训练好的成功模型，存到本地，以后给 App 用
joblib.dump(model_dict[best_model_name], 'model.pkl')
print(f"【3】结束,成功模型是:{best_model_name}，误差只有 {best_error:.2f} 分钟。已保存为 model.pkl")