
import pytest
from main import *
import requests

class Test_api:

    #checks if the status code is successful when searching for the word 'ignore'
    def test_status_the_word_ignore(self):
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en/ignore'
        response = requests.get(url)

        assert 200 <= response.status_code < 400

    # checks if the status code is successful when searching for the word 'yauza' (N)
    def test_status_the_word_yauza_N(self):
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en/yauza'
        response = requests.get(url)

        assert response.status_code==404

#check that success word in the body
    def test_1_success(self):
        response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/success')
        dict1 = response.json()
        actual = dict1[0]['word']
        expected = 'success'
        assert actual == expected

    def test_2_human(self):
        response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/human')
        dict1 = response.json()
        actual = dict1[0]['word']
        expected = 'human'
        assert actual == expected
