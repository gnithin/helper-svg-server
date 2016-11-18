from lib.bottle import Bottle, request
import logging
from dal import DAL
from utils import Utils
from pprint import pprint

bottle = Bottle()


@bottle.route('/')
def index():
    return "Hello world!"


@bottle.route('/post', method="POST")
def post():
    all_content_key = "allOutput"
    timestamp_key = "timestamp"
    all_content = request.forms.get(all_content_key)
    logging.info(all_content)
    timestamp = request.forms.get(timestamp_key)
    if not timestamp:
        timestamp = ""

    add_data = {}
    if all_content:
        add_data = {
            "content" : all_content,
            "timestamp": timestamp
        }

    # The return message is just for viewing in circleci
    return Utils.resp_json(
        *(
            [1, "Added test data!"] if DAL.insert_test_data(**add_data)
            else [-1, "Failed adding test data!"]
        )
    )


@bottle.route('/stats')
def stats():
    test_data = DAL.get_latest_test_data()
    if not test_data:
        return Utils.resp_json(-1, "No data available")

    return Utils.resp_json(1, "success", contents=test_data)

if __name__ == "__main__":
    # Just testing out the parser bit
    sunny_str = '''
    === RUN   TestBST_integer
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
    '''

    rainy_str = '''
    === RUN   TestBST_integer
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
    FAIL	github.com/gnithin/gotree/tree/tests	1.678s
    '''
    pprint(Utils.parse_content(sunny_str, ""))
    pprint(Utils.parse_content(rainy_str, ""))
