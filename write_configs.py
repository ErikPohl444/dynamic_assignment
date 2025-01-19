import os
import sys


class WriteConfigs:

    def __init__(
            self,
            primary_keys=None,
            source_dict=None,
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
        # remove pycache
        path = os.path.join(sys.path[0], "__pycache__")
        pycache_file_name = [x for x in os.listdir(path) if file_name.split('.')[0] in x][0]
        file_path = os.path.join(path, pycache_file_name)
        try:
            os.remove(file_path)
        except FileNotFoundError:
            pass
