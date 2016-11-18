## Why?
# Postman has this bug where POST entries cannot have the newlines added to it.
# https://github.com/postmanlabs/postman-app-support/issues/448
sunny_day='=== RUN   TestBST_integer
    --- PASS: TestBST_integer (0.00s)
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
    --- PASS: TestTrie_Insertion (1.86s)
        Trie_test.go:143: 904061
    PASS
    BenchmarkExp_map-2           	50000000	        27.4 ns/op
    BenchmarkExp_ptr-2           	2000000000	         0.65 ns/op
    BenchmarkExp_arr-2           	2000000000	         0.65 ns/op
    BenchmarkMaxHeap_ins_50000-2 	 5000000	       287 ns/op
    BenchmarkMaxHeap_ins_90000-2 	 3000000	       412 ns/op
    BenchmarkMaxHeap_ins_100000-2	 2000000	       521 ns/op
    BenchmarkMaxHeap_ins_200000-2	       1	1176492043 ns/op
    BenchmarkMaxHeap_ins_300000-2	       1	1858822997 ns/op
    BenchmarkMaxHeap_ins_400000-2	       1	2388464427 ns/op
    BenchmarkMaxHeap_ins_500000-2	       1	3239821271 ns/op
    BenchmarkMinHeap_ins_50000-2 	 5000000	       279 ns/op
    BenchmarkMinHeap_ins_90000-2 	 3000000	       375 ns/op
    BenchmarkMinHeap_ins_100000-2	 3000000	       394 ns/op
    BenchmarkMinHeap_ins_200000-2	       1	1034617725 ns/op
    BenchmarkMinHeap_ins_300000-2	       1	1623952866 ns/op
    BenchmarkMinHeap_ins_400000-2	       1	2059533534 ns/op
    BenchmarkMinHeap_ins_500000-2	       1	2796894245 ns/op
    BenchmarkMaxHeap_pop5000-2   	  100000	     15009 ns/op
    BenchmarkMaxHeap_pop20000-2  	   20000	     65800 ns/op
    BenchmarkMaxHeap_pop50000-2  	    5000	    222388 ns/op
    BenchmarkMaxHeap_pop90000-2  	    2000	    603784 ns/op
    BenchmarkMaxHeap_pop100000-2 	    1000	   1031251 ns/op
    BenchmarkMaxHeap_pop200000-2 	       1	1477133854 ns/op
    BenchmarkMaxHeap_pop300000-2 	       1	2303676884 ns/op
    BenchmarkMaxHeap_pop400000-2 	       1	3039391517 ns/op
    BenchmarkMaxHeap_pop500000-2 	       1	4007572221 ns/op
    Benchmark_trieInsertion-2    	       1	1906820476 ns/op
    Benchmark_triePassSearch-2   	       1	1829905968 ns/op
    Benchmark_strPassSearch-2    	    1000	   1694059 ns/op
    Benchmark_trieFailSearch-2   	       1	1817361659 ns/op
    Benchmark_strFailSearch-2    	     500	   3688744 ns/op
    ok  	github.com/gnithin/gotree/tree/tests	124.664s
'
rainy_day='    === RUN   TestBST_integer
    --- PASS: TestBST_integer (0.00s)
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
    --- PASS: TestTrie_Insertion (1.86s)
        Trie_test.go:143: 904061
    PASS
    BenchmarkExp_map-2           	50000000	        27.4 ns/op
    BenchmarkExp_ptr-2           	2000000000	         0.65 ns/op
    BenchmarkExp_arr-2           	2000000000	         0.65 ns/op
    BenchmarkMaxHeap_ins_50000-2 	 5000000	       287 ns/op
    BenchmarkMaxHeap_ins_90000-2 	 3000000	       412 ns/op
    BenchmarkMaxHeap_ins_100000-2	 2000000	       521 ns/op
    BenchmarkMaxHeap_ins_200000-2	       1	1176492043 ns/op
    BenchmarkMaxHeap_ins_300000-2	       1	1858822997 ns/op
    BenchmarkMaxHeap_ins_400000-2	       1	2388464427 ns/op
    BenchmarkMaxHeap_ins_500000-2	       1	3239821271 ns/op
    BenchmarkMinHeap_ins_50000-2 	 5000000	       279 ns/op
    BenchmarkMinHeap_ins_90000-2 	 3000000	       375 ns/op
    BenchmarkMinHeap_ins_100000-2	 3000000	       394 ns/op
    BenchmarkMinHeap_ins_200000-2	       1	1034617725 ns/op
    BenchmarkMinHeap_ins_300000-2	       1	1623952866 ns/op
    BenchmarkMinHeap_ins_400000-2	       1	2059533534 ns/op
    BenchmarkMinHeap_ins_500000-2	       1	2796894245 ns/op
    BenchmarkMaxHeap_pop5000-2   	  100000	     15009 ns/op
    BenchmarkMaxHeap_pop20000-2  	   20000	     65800 ns/op
    BenchmarkMaxHeap_pop50000-2  	    5000	    222388 ns/op
    BenchmarkMaxHeap_pop90000-2  	    2000	    603784 ns/op
    BenchmarkMaxHeap_pop100000-2 	    1000	   1031251 ns/op
    BenchmarkMaxHeap_pop200000-2 	       1	1477133854 ns/op
    BenchmarkMaxHeap_pop300000-2 	       1	2303676884 ns/op
    BenchmarkMaxHeap_pop400000-2 	       1	3039391517 ns/op
    BenchmarkMaxHeap_pop500000-2 	       1	4007572221 ns/op
    Benchmark_trieInsertion-2    	       1	1906820476 ns/op
    Benchmark_triePassSearch-2   	       1	1829905968 ns/op
    Benchmark_strPassSearch-2    	    1000	   1694059 ns/op
    Benchmark_trieFailSearch-2   	       1	1817361659 ns/op
    Benchmark_strFailSearch-2    	     500	   3688744 ns/op
    ok  	github.com/gnithin/gotree/tree/tests	124.664s
FAIL	github.com/gnithin/gotree/tree/tests	1.678s'

curl --data "allOutput=$sunny_day" http://localhost:8080/post
