import os
import threading

import Methub


class GirlSRestore(threading.Thread):

    def __init__(self, able_list: list, rgb_list: dict, alpha_list: dict, save_path: str, is_work: bool, form,
                 setting: dict, full: dict):
        super(GirlSRestore, self).__init__()

        self.able_list = able_list
        self.rgb_list = rgb_list
        self.alpha_list = alpha_list
        self.save_path = save_path
        self.is_work = is_work

        self.form = form

        self.setting = setting
        self.full = full

    def run(self):
        length = len(self.rgb_list)
        if not self.is_work:
            pass
        else:
            i = 0
            if self.setting["check_before_start"]:
                for val in self.able_list:
                    Methub.tools.search(self.rgb_list, self.alpha_list, list(self.alpha_list.keys()), val)
                    i += 1
                    val_percent = str(round(100 * (i / len(self.able_list)), 2))
                    val = Methub.Functions.re_int(100 * (i / len(self.rgb_list)))
                    self.form.m_staticText_all.SetLabel("扫描进度：%s %%" % val_percent)
                    self.form.m_gauge_all.SetValue(val)
                i = 0

            for val in self.able_list:
                if self.setting["export_type"] == 1:
                    if val.split("_")[0].lower() != "pic":
                        length -= 1
                        continue
                if self.setting["div_type"] == 1:
                    if val.split("_")[0].lower() == "pic":
                        name = val.split("_")[1]
                        save_path = f"{self.save_path}\\人形\\{name}"
                        os.makedirs(save_path, exist_ok=True)

                    else:
                        save_path = f"{self.save_path}\\其他"
                        os.makedirs(save_path, exist_ok=True)

                elif self.setting["div_type"] == 1:
                    if val.split("_")[0].lower() == "pic":
                        if val.split("_")[-1].lower() == "d":
                            save_path = f"{self.save_path}\\人形\\大破"
                            os.makedirs(save_path, exist_ok=True)
                        else:
                            save_path = f"{self.save_path}\\人形\\普通"
                            os.makedirs(save_path, exist_ok=True)
                    else:
                        save_path = f"{self.save_path}\\其他"
                        os.makedirs(save_path, exist_ok=True)

                else:
                    save_path = self.save_path

                    Methub.Functions.girl_font_line_restore(self.rgb_list[val], self.alpha_list[val], save_path)
                i += 1

                val_percent = str(round(100 * (i / length), 2))
                self.form.m_staticText_now.SetLabel("当前：%s" % val)
                val = Methub.Functions.re_int(100 * (i / length))
                self.form.m_staticText_all.SetLabel("总进度：%s %%" % val_percent)
                self.form.m_gauge_all.SetValue(val)

            self.form.m_staticText_all.SetLabel("总进度：%s %%" % '100')
            self.form.start = False

            if self.full["open_dir"]:
                os.system(r"start %s" % self.save_path)

    def set_value(self, rgb_list, alpha_list, save_path, able_list, setting, full):
        self.rgb_list = rgb_list
        self.alpha_list = alpha_list
        self.save_path = save_path
        self.able_list = able_list

        self.setting = setting
        self.full = full

    def set_work(self, is_work: bool):
        self.is_work = is_work
