#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import json

movie=raw_input("Dwste to onoma tis tainias pou thelete.Ean o titlos emperiexei kena eseis anti gia keno patiste to sumbolo '+' : " )

url = "http://www.omdbapi.com/?t=" + movie +"&y=&plot=short&r=json"
json_obj = urllib2.urlopen(url)
data = json.load(json_obj)
print "Ta brabeia tis tainias: ", data['Awards']
print"I kritiki tou Imdb: ", data['imdbRating']
