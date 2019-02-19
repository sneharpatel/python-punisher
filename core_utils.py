import os
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def get_driver() -> WebDriver:
    if "env" in os.environ:
        if os.environ["env"] == "chrome":
            return webdriver.Chrome()
        else:
            raise Exception("Not supported browser")
    else:
        return webdriver.Firefox()


def has_long_word(s: str) -> bool:
    array = s.split(' ')
    for word in array:
        if len(word) > 10:
            return True
    return False


# tests has_long_word method
def main():
    s = "This is a python programming language"
    o_p = has_long_word(s)
    print(o_p)
    s = "This is a python code"
    o_p = has_long_word(s)
    print(o_p)


if __name__ == "__main__":
    main()
