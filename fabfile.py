from fabric.api import local

def test():
    local("./little.py")
def add():
    local("git add .")
def commit():
    local("git commit -m 'justchanging'")
def push():
    local("git push origin master")

def deploye():
   test()
   add()
   commit()
   push()
