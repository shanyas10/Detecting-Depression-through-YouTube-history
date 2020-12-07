from empath import Empath
import pandas as pd
import numpy as np

lexicon = Empath()

# Define custom categories for various symptoms on the scale

def define_category():

    categories = { 
        'cesd_1'  : ["appetite"],
        'cesd_2'  : ["blues", "sad"],
        'cesd_3'  : ["distraction", "adhd"],
        'cesd_4'  : ["depressed"],
        'cesd_5_11'  : ["insomnia", "sleep", "restless","overslept", "nightmare"],
        'cesd_6'  : ["sad"],
        'cesd_8'  : ["unhappy"],
        'cesd_9'  : ["self-hate","self_blame"],
        'cesd_10' : ["disinterest", "dull"],
        'cesd_12' : ["slowly","move", "struggle"],
        'cesd_13' : ["fidgety"],
        'cesd_14' : ["suicidal", "own_death"],
        'cesd_15' : ["self_hurt", "self_harm"],
        'cesd_16' : ["tired"],
        'cesd_18' : ["weight_loss"],
 
    }

    return categories

categories = define_category()

# Create custom categories

def create_category(name, categories):
    empath_categories = lexicon.create_category(name,categories)

def analyze(category, string):
	analysis = lexicon.analyze(string, categories = [category])

	return analysis[category]

def cesd_calculate(text):
    
    score = 0
    time = 1
    for category, value in categories.items():
    	score += analyze(category, text)
        
    return score


def score():

	data = pd.read_csv('Comments.csv')
	data = data.dropna()
	texts = data['text']

	scores = 0
	
	for category, value in categories.items():
	        create_category(category, value)

	i =0
	comments_analyzed = 0
	for text in texts:
	    if len(text)>100:
	    	comments_analyzed +=1
	    	score = cesd_calculate(text)
	    	scores+=score	
	if comments_analyzed>0:
		return scores/comments_analyzed
	else:
		return 0

