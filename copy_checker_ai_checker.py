import os

from thefuzz import fuzz
from difflib import SequenceMatcher

verbs = ["Do", "The", "That", "Does", "Is", "Am", "Are", "Has", "Have", "Been", "Has", "Have", "Did", "Was", "Were",
         "Had", "Shall", "Will", "Can", "Could", "May", "Might", "Must", "Should", "Would", "Be", "Of", "A", "An"]





class copy_checker_ai_checker():
    def __init__(self, text1):
        self.text1 = text1

    def send_check(self):
        path = r"C:\Users\HP\Documents\Programming\Python\plagiarism project\data"
        list_dr = os.listdir(path)
        list_dr.remove("system_id_gmail.csv")
        for data in list_dr:
            with open(f"data/{data}") as file:
                text = "".join(file.read().strip("\n"))
            result = self.copy_checker(text)
            if result > 50:
                return False
        return True

    def change_text(self, text):
        list_text = text.split()
        list1 = [word for word in list_text if word.title() not in verbs]
        return " ".join(list1)

    def copy_checker(self, answer):
        d = SequenceMatcher(None, self.text1, answer)
        similarity_ratio = d.ratio()
        similarity_percentage = int(similarity_ratio * 100)
        if similarity_percentage > 40:
            self.text1, answer = self.change_text(self.text1), self.change_text(answer)
            return fuzz.token_set_ratio(self.text1, answer)
        else:
            return similarity_percentage
