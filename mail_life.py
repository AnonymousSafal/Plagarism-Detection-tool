import pandas


class mail_life_checker():
    def __init__(self, system_id):
        self.system_id = system_id
        self.record = pandas.read_csv(
            "data/system_id_gmail.csv")
        self.row_index = self.record.index[self.record["system_id"] == system_id]
        self.individual = self.record.loc[self.row_index]
        self.life = self.individual["life"].item()
        self.gmail = self.individual["gmail"]

    def decrease_life(self):
        self.life -= 1
        self.record.loc[self.record["system_id"]== self.system_id,"life"] = self.life
        self.record.to_csv("data/system_id_gmail.csv",index = False)


if __name__ == "__main__":
    new = mail_life_checker(2023001106)
    new.decrease_life()