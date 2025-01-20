import random
import string
from write_configs import WriteConfigs
import importlib


if __name__ == "__main__":
    for n in range(5):
        t_dict = {}
        t_dict["t1"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t2"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t3"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t4"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print(t_dict)
        WriteConfigs(
            file_name=r"configs.py",
            source_dict=t_dict,
            primary_keys=["t1", "t2", "t3", "t4"]
        )
        import configs
        importlib.reload(configs)
        from configs import t1_xf, t2_xf, t3_xf, t4_xf

        print(f"here {t1_xf},{t2_xf},{t3_xf},{t4_xf}")


