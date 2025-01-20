# Usage Walkthrough Markdown created by usage-vacuum from dynamic_assignment.src.demo_write_configs.py


```python
    for n in range(5):
        t_dict = {}
        t_dict["t1"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t2"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t3"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t4"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print(t_dict)
```
{'t1': 'FD7XG', 't2': 'TYJKS', 't3': 'LLHRX', 't4': 'ULF6B'}

```python
        WriteConfigs(
            file_name=r"configs.py",
            source_dict=t_dict,
            primary_keys=["t1", "t2", "t3", "t4"]
        WriteConfigs(
        import configs
        importlib.reload(configs)
        from configs import t1_xf, t2_xf, t3_xf, t4_xf
        print(f"here {t1_xf},{t2_xf},{t3_xf},{t4_xf}")
```
here FD7XG,TYJKS,LLHRX,ULF6B

```python
    for n in range(5):
        t_dict = {}
        t_dict["t1"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t2"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t3"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t4"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print(t_dict)
```
{'t1': 'YQR21', 't2': 'XTGG3', 't3': 'FE03F', 't4': 'ZOVG4'}

```python
        WriteConfigs(
            file_name=r"configs.py",
            source_dict=t_dict,
            primary_keys=["t1", "t2", "t3", "t4"]
        WriteConfigs(
        import configs
        importlib.reload(configs)
        from configs import t1_xf, t2_xf, t3_xf, t4_xf
        print(f"here {t1_xf},{t2_xf},{t3_xf},{t4_xf}")
```
here YQR21,XTGG3,FE03F,ZOVG4

```python
    for n in range(5):
        t_dict = {}
        t_dict["t1"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t2"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t3"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t4"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print(t_dict)
```
{'t1': 'C3V24', 't2': '2SAZJ', 't3': 'DNQH7', 't4': '2FLR7'}

```python
        WriteConfigs(
            file_name=r"configs.py",
            source_dict=t_dict,
            primary_keys=["t1", "t2", "t3", "t4"]
        WriteConfigs(
        import configs
        importlib.reload(configs)
        from configs import t1_xf, t2_xf, t3_xf, t4_xf
        print(f"here {t1_xf},{t2_xf},{t3_xf},{t4_xf}")
```
here C3V24,2SAZJ,DNQH7,2FLR7

```python
    for n in range(5):
        t_dict = {}
        t_dict["t1"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t2"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t3"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t4"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print(t_dict)
```
{'t1': '9SGN2', 't2': 'BSVZG', 't3': 'HNOUY', 't4': 'HDOX9'}

```python
        WriteConfigs(
            file_name=r"configs.py",
            source_dict=t_dict,
            primary_keys=["t1", "t2", "t3", "t4"]
        WriteConfigs(
        import configs
        importlib.reload(configs)
        from configs import t1_xf, t2_xf, t3_xf, t4_xf
        print(f"here {t1_xf},{t2_xf},{t3_xf},{t4_xf}")
```
here 9SGN2,BSVZG,HNOUY,HDOX9

```python
    for n in range(5):
        t_dict = {}
        t_dict["t1"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t2"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t3"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t4"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print(t_dict)
```
{'t1': 'UQGUD', 't2': 'WS3PN', 't3': 'FW88X', 't4': 'Z4O4F'}

```python
        WriteConfigs(
            file_name=r"configs.py",
            source_dict=t_dict,
            primary_keys=["t1", "t2", "t3", "t4"]
        WriteConfigs(
        import configs
        importlib.reload(configs)
        from configs import t1_xf, t2_xf, t3_xf, t4_xf
        print(f"here {t1_xf},{t2_xf},{t3_xf},{t4_xf}")
```
here UQGUD,WS3PN,FW88X,Z4O4F
'''\    for n in range(5):\'''\