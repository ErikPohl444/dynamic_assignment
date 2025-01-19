import os


class WriteConfigs:

    def __init__(
            self,
            primary_keys=[],
            source_dict={},
            file_name="configs.py"
    ):
        self.file_name = file_name
        self.primary_keys = primary_keys
        self.source_dict = source_dict
        self.missing_keys = []
        for pk in self.primary_keys:
            if pk not in self.source_dict.keys():
                self.missing_keys.append(pk)
        if self.missing_keys:
            raise KeyError(f"Missing keys {','.join(self.missing_keys)}")
        else:
            with open(file_name, "wt") as cheat_handle:
                for pk in self.primary_keys:
                    val = f"{pk}_xf = \"{self.source_dict[pk]}\"\n"
                    cheat_handle.write(val)
        # find correct pycache
        path = os.getcwd() + r"\__pycache__"
        os.remove(path + r'\configs.cpython-312.pyc')
