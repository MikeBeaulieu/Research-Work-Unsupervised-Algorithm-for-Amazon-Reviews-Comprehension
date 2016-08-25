# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 22:03:15 2016


"""

import collections, itertools
import nltk.classify.util, nltk.metrics
from nltk.metrics import *
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.probability import FreqDist, ConditionalFreqDist

#Creating Corpus using WordListCorpusReader
from nltk.corpus.reader import CategorizedPlaintextCorpusReader
imdb_reviews = CategorizedPlaintextCorpusReader('C:\\Users\\SuryaVikasArun\\Desktop\\INDPStudy\\negpos',
                                                  r'.*\.txt', cat_pattern=r'(\w+)/*')

len(imdb_reviews.fileids())

def word_feats(words):
    return dict([(word, True) for word in words])
   
def best_bigram_word_feats(words, score_fn=BigramAssocMeasures.chi_sq, n=200):
    bigram_finder = BigramCollocationFinder.from_words(words)
    bigrams = bigram_finder.nbest(score_fn, n)
    d = dict([(bigram, True) for bigram in bigrams])
    d.update(word_feats(words))
    return d
    
featx=best_bigram_word_feats

negids = imdb_reviews.fileids('neg')
posids = imdb_reviews.fileids('pos')
 
negfeats = [(featx(imdb_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(featx(imdb_reviews.words(fileids=[f])), 'pos') for f in posids]
 
negcutoff = len(negfeats)*3/4
poscutoff = len(posfeats)*3/4
 
trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
classifier =NaiveBayesClassifier.train(trainfeats)

refsets = collections.defaultdict(set)
testsets = collections.defaultdict(set)
 
for i, (feats, label) in enumerate(testfeats):
    refsets[label].add(i)
    observed = classifier.classify(feats)
    testsets[observed].add(i)
 
print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
classifier.show_most_informative_features()
with open("C:\\Users\\SuryaVikasArun\\Desktop\\INDPStudy\\Python_1.txt") as f:
    sentences = f.read().splitlines();
    
#sentences={"Worst Camera","Great Camera","Best Camera","This little camera even with its quarks, like slow write SD card times, is amazing.",
#"I think the real problem is Sigma's lack of experience with compacts."}
for sentence in sentences:
    sent_words=sentence.split() 
    print sentence
    print classifier.classify(best_bigram_word_feats(sent_words))    