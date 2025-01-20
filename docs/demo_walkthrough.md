# Usage Walkthrough Markdown created by usage-vacuum from dynamic_assignment.src.demo_write_configs.py


```python
    for n in range(5):
```
> [!NOTE]
>         Set up the dict mapping variable names to values</br>
```python
        t_dict = {}
        t_dict["t1"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t2"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t3"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t4"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print(t_dict)
```
{'t1': 'QHYAZ', 't2': 'SVCYU', 't3': 'C8JWA', 't4': '6GWOM'}
> [!NOTE]
>         call the configs shared state file generator</br>
```python
        WriteConfigs(
            file_name=r"configs.py",
            source_dict=t_dict,
            primary_keys=["t1", "t2", "t3", "t4"]
        WriteConfigs(
```
> [!NOTE]
>         import the newly created configs and the variables you created</br>
```python
        import configs
        importlib.reload(configs)
        from configs import t1_xf, t2_xf, t3_xf, t4_xf
        print(f"here {t1_xf},{t2_xf},{t3_xf},{t4_xf}")
```
here QHYAZ,SVCYU,C8JWA,6GWOM

```python
    for n in range(5):
```
> [!NOTE]
>         Set up the dict mapping variable names to values</br>
```python
        t_dict = {}
        t_dict["t1"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t2"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t3"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t4"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print(t_dict)
```
{'t1': '0ZAL4', 't2': 'R9Q9B', 't3': 'E0ZJZ', 't4': 'JFW6Y'}
> [!NOTE]
>         call the configs shared state file generator</br>
```python
        WriteConfigs(
            file_name=r"configs.py",
            source_dict=t_dict,
            primary_keys=["t1", "t2", "t3", "t4"]
        WriteConfigs(
```
> [!NOTE]
>         import the newly created configs and the variables you created</br>
```python
        import configs
        importlib.reload(configs)
        from configs import t1_xf, t2_xf, t3_xf, t4_xf
        print(f"here {t1_xf},{t2_xf},{t3_xf},{t4_xf}")
```
here 0ZAL4,R9Q9B,E0ZJZ,JFW6Y

```python
    for n in range(5):
```
> [!NOTE]
>         Set up the dict mapping variable names to values</br>
```python
        t_dict = {}
        t_dict["t1"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t2"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t3"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t4"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print(t_dict)
```
{'t1': 'EWW6V', 't2': 'NW0OG', 't3': 'C0MPX', 't4': '2YKZI'}
> [!NOTE]
>         call the configs shared state file generator</br>
```python
        WriteConfigs(
            file_name=r"configs.py",
            source_dict=t_dict,
            primary_keys=["t1", "t2", "t3", "t4"]
        WriteConfigs(
```
> [!NOTE]
>         import the newly created configs and the variables you created</br>
```python
        import configs
        importlib.reload(configs)
        from configs import t1_xf, t2_xf, t3_xf, t4_xf
        print(f"here {t1_xf},{t2_xf},{t3_xf},{t4_xf}")
```
here EWW6V,NW0OG,C0MPX,2YKZI

```python
    for n in range(5):
```
> [!NOTE]
>         Set up the dict mapping variable names to values</br>
```python
        t_dict = {}
        t_dict["t1"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t2"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t3"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t4"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print(t_dict)
```
{'t1': 'VRID5', 't2': '1VBMW', 't3': 'F76M7', 't4': '8DADZ'}
> [!NOTE]
>         call the configs shared state file generator</br>
```python
        WriteConfigs(
            file_name=r"configs.py",
            source_dict=t_dict,
            primary_keys=["t1", "t2", "t3", "t4"]
        WriteConfigs(
```
> [!NOTE]
>         import the newly created configs and the variables you created</br>
```python
        import configs
        importlib.reload(configs)
        from configs import t1_xf, t2_xf, t3_xf, t4_xf
        print(f"here {t1_xf},{t2_xf},{t3_xf},{t4_xf}")
```
here VRID5,1VBMW,F76M7,8DADZ

```python
    for n in range(5):
```
> [!NOTE]
>         Set up the dict mapping variable names to values</br>
```python
        t_dict = {}
        t_dict["t1"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t2"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t3"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t4"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print(t_dict)
```
{'t1': 'TLN4C', 't2': 'A235M', 't3': 'QYSG0', 't4': 'O54LP'}
> [!NOTE]
>         call the configs shared state file generator</br>
```python
        WriteConfigs(
            file_name=r"configs.py",
            source_dict=t_dict,
            primary_keys=["t1", "t2", "t3", "t4"]
        WriteConfigs(
```
> [!NOTE]
>         import the newly created configs and the variables you created</br>
```python
        import configs
        importlib.reload(configs)
        from configs import t1_xf, t2_xf, t3_xf, t4_xf
        print(f"here {t1_xf},{t2_xf},{t3_xf},{t4_xf}")
```
here TLN4C,A235M,QYSG0,O54LP
'''\    for n in range(5):\'''\