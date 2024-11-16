import requests
from typing import Optional
from typing import Sequence

user = "Voltair"
problem = set()
cntp = 0;
CFAPI = "https://codeforces.com/api/"


def LogIn(name):
    user = name;

def Greetings()
    print("Hi ", user, "\n")
    print(

def space(cnt):
    return " " * cnt

def getSolved():
    r = requests.get("https://codeforces.com/api/user.status?handle=" + user + "&from=1")
    f = r.json();
    for sub in f["result"]:
        cntp += 1
        if sub["verdict"] == "OK":
            s = str(sub["contestId"]) + str(sub["problem"]["index"])
            problem.add(s)
    print(len(problem))

def getSubmission(cnt):
    s = str(cnt)
    print("Last " + s + " submission(s):\n")
    r = requests.get("https://codeforces.com/api/user.status?handle=" + user + "&from=1&count=" + s)
    f = r.json();
    print(f)
    headers = ["Problem", "Name", "Rating", "Verdict"]

def main(agrv: Optional[Sequence[str]] = None) -> int:
    getSubmission(1)
    getSolved()

if __name__ == "__main__":
    exit(main())
