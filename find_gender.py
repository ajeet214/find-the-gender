import requests

class gender:
    def search(self, query):
        a = requests.get("https://api.genderize.io/?name="+query)
        return a.json()

if __name__ == "__main__":
    obj = gender()
    print(obj.search("maxwell"))
