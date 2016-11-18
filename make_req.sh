## Why?
# Postman has this bug where POST entries cannot have the newlines added to it.
# https://github.com/postmanlabs/postman-app-support/issues/448

curl --data 'allOutput=
=== RUN   TestBST_integer (/base/data/home/apps/s~king-slayer/20161117t153646.397117299156342176/api.py:19)
--- FAIL: TestBST_integer (0.00s)
	assertions.go:225: 
                        
	Error Trace:	BST_test.go:25
		
	Error:		Should be false
		
=== RUN   TestBST_string
--- PASS: TestBST_string (0.00s)
=== RUN   TestBST_customObj
--- PASS: TestBST_customObj (0.00s)
=== RUN   TestHeap_loadTesting
--- PASS: TestHeap_loadTesting (0.00s)
=== RUN   TestHeap_integer
--- PASS: TestHeap_integer (0.00s)
=== RUN   TestHuffman_basic
--- PASS: TestHuffman_basic (0.00s)
=== RUN   TestHuffman_lyrics
--- PASS: TestHuffman_lyrics (0.00s)
=== RUN   TestTrie_development
--- PASS: TestTrie_development (0.00s)
=== RUN   TestTrie_multiple
--- PASS: TestTrie_multiple (0.00s)
=== RUN   TestTrie_withOptionsMap
--- PASS: TestTrie_withOptionsMap (0.00s)
=== RUN   TestTrie_stopWords
--- PASS: TestTrie_stopWords (0.00s)
=== RUN   TestTrie_Insertion
--- PASS: TestTrie_Insertion (1.64s)
FAIL
exit status 1
FAIL	github.com/gnithin/gotree/tree/tests	1.678s' http://localhost:8080/post
