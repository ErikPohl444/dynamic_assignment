import random
import string
from write_configs import WriteConfigs
import importlib
import logging


if __name__ == "__main__":
    for n in range(5):
        logging.info("Set up the dict mapping variable names to values")
        t_dict = {}
        t_dict["t1"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t2"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t3"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        t_dict["t4"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print(t_dict)
        logging.info("call the configs shared state file generator")
        WriteConfigs(
            file_name=r"configs.py",
            source_dict=t_dict,
            primary_keys=["t1", "t2", "t3", "t4"]
        )
        logging.info("import the newly created configs and the variables you created")
        import configs
        importlib.reload(configs)
        from configs import t1_xf, t2_xf, t3_xf, t4_xf

        print(f"here {t1_xf},{t2_xf},{t3_xf},{t4_xf}")


