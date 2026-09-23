from main import *
import sys
import trace

# 2 pts
def test_word_count_map():
    assert sorted(word_count_map('i am sam i am')) == \
           sorted([('i', 1), ('am', 1), ('sam', 1), ('i', 1), ('am', 1)])

# 2 pts
def test_word_count_reduce():
    assert word_count_reduce(['i', [1,1,1]]) == ('i', 3)

# 2 pts
def test_word_count_reduce_uses_reduce():
	# test that reduce is called from word_count_reduce
	tracer = trace.Trace(ignoredirs=[sys.prefix, sys.exec_prefix], countfuncs=1)
	tracer.runfunc(word_count_reduce, (['i', [1,1,1]]))
	r = tracer.results()
	assert len([i for i in r.calledfuncs if i[2]=='reduce']) > 0

# 1 pts
def test_word_count():
    assert sorted(run_map_reduce(word_count_map, word_count_reduce, ['i am sam i am', 'sam is ham'])) == \
           sorted([('am', 2), ('ham', 1), ('i', 2), ('is', 1), ('sam', 2)])

# 2 pts
def test_sentiment_map():
    assert sentiment_map('it was a terrible waste of time') == [('negative', 1), ('negative', 1)]
    assert sorted(sentiment_map('it was a sockdolager waste of time')) == [('negative', 1), ('positive', 1)]

# 2 pts
def test_sentiment():
    docs = [
        'it was not great but not terrible',
        'thou art a boil a plague-sore or embossed carbuncle in my corrupted blood',
        'it was a sockdolager of a good time'
    ]
    result = run_map_reduce(sentiment_map, word_count_reduce, docs)
    assert result == [('negative', 3), ('positive', 3)]