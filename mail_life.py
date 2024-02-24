file_path = r"C:\Users\HP\Documents\Programming\Python\plagiarism project\data\system_id_gmail.csv"
import pandas


class mail_life_checker():
    def __init__(self, system_id):
        self.record = r"C:\Users\HP\Documents\Programming\Python\plagiarism project\data\system_id_gmail.csv"
        self.system_id = system_id
        self.record = pandas.read_csv(
            r"C:\Users\HP\Documents\Programming\Python\plagiarism project\data\system_id_gmail.csv")
        self.row_index = self.record.index[self.record["system_id"] == system_id]
        self.individual = self.record.loc[self.row_index]
        self.life = self.individual["life"].to_dict()
        self.gmail = self.individual["gmail"]

    def decrease_life(self):
        self.life -= 1
        self.record[self.row_index, "life"] = self.life
        self.record.to_csv(f"{self.record}", index=False)



if __name__ == "__main__":
    mail_life_checker(2023001106)
