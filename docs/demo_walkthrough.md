# Usage Walkthrough Markdown created by usage-vacuum from dynamic_assignment.src.demo_write_configs.py


```python
    for n in range(5):
        logging.info("Set up the dict mapping variable names to values")
        t_dict = {}
        t_dict["t1"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t2"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t3"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t4"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print(t_dict)
```
{'t1': 'RG8NB', 't2': '6K1F9', 't3': 'EH141', 't4': 'ENFQP'}

```python
        logging.info("call the configs shared state file generator")
        WriteConfigs(
            file_name=r"configs.py",
            source_dict=t_dict,
            primary_keys=["t1", "t2", "t3", "t4"]
        WriteConfigs(
        logging.info("import the newly created configs and the variables you created")
        import configs
        importlib.reload(configs)
        from configs import t1_xf, t2_xf, t3_xf, t4_xf
        print(f"here {t1_xf},{t2_xf},{t3_xf},{t4_xf}")
```
here RG8NB,6K1F9,EH141,ENFQP

```python
    for n in range(5):
        logging.info("Set up the dict mapping variable names to values")
        t_dict = {}
        t_dict["t1"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t2"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t3"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t4"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print(t_dict)
```
{'t1': 'FU61U', 't2': 'RO3UA', 't3': 'MXJCA', 't4': 'ETGJV'}

```python
        logging.info("call the configs shared state file generator")
        WriteConfigs(
            file_name=r"configs.py",
            source_dict=t_dict,
            primary_keys=["t1", "t2", "t3", "t4"]
        WriteConfigs(
        logging.info("import the newly created configs and the variables you created")
        import configs
        importlib.reload(configs)
        from configs import t1_xf, t2_xf, t3_xf, t4_xf
        print(f"here {t1_xf},{t2_xf},{t3_xf},{t4_xf}")
```
here FU61U,RO3UA,MXJCA,ETGJV

```python
    for n in range(5):
        logging.info("Set up the dict mapping variable names to values")
        t_dict = {}
        t_dict["t1"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t2"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t3"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t4"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print(t_dict)
```
{'t1': 'ISKVS', 't2': '4CSYR', 't3': '52T6Z', 't4': 'KB8HE'}

```python
        logging.info("call the configs shared state file generator")
        WriteConfigs(
            file_name=r"configs.py",
            source_dict=t_dict,
            primary_keys=["t1", "t2", "t3", "t4"]
        WriteConfigs(
        logging.info("import the newly created configs and the variables you created")
        import configs
        importlib.reload(configs)
        from configs import t1_xf, t2_xf, t3_xf, t4_xf
        print(f"here {t1_xf},{t2_xf},{t3_xf},{t4_xf}")
```
here ISKVS,4CSYR,52T6Z,KB8HE

```python
    for n in range(5):
        logging.info("Set up the dict mapping variable names to values")
        t_dict = {}
        t_dict["t1"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t2"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t3"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t4"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print(t_dict)
```
{'t1': 'GZJSD', 't2': 'AKLOC', 't3': 'AWHJK', 't4': '2XXN5'}

```python
        logging.info("call the configs shared state file generator")
        WriteConfigs(
            file_name=r"configs.py",
            source_dict=t_dict,
            primary_keys=["t1", "t2", "t3", "t4"]
        WriteConfigs(
        logging.info("import the newly created configs and the variables you created")
        import configs
        importlib.reload(configs)
        from configs import t1_xf, t2_xf, t3_xf, t4_xf
        print(f"here {t1_xf},{t2_xf},{t3_xf},{t4_xf}")
```
here GZJSD,AKLOC,AWHJK,2XXN5

```python
    for n in range(5):
        logging.info("Set up the dict mapping variable names to values")
        t_dict = {}
        t_dict["t1"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t2"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t3"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t4"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print(t_dict)
```
{'t1': 'GPDQN', 't2': 'HUJMF', 't3': 'VALKV', 't4': 'ACQGR'}

```python
        logging.info("call the configs shared state file generator")
        WriteConfigs(
            file_name=r"configs.py",
            source_dict=t_dict,
            primary_keys=["t1", "t2", "t3", "t4"]
        WriteConfigs(
        logging.info("import the newly created configs and the variables you created")
        import configs
        importlib.reload(configs)
        from configs import t1_xf, t2_xf, t3_xf, t4_xf
        print(f"here {t1_xf},{t2_xf},{t3_xf},{t4_xf}")
```
here GPDQN,HUJMF,VALKV,ACQGR
'''\    for n in range(5):\'''\