#!/bin/bash
API_USER=<your c3 username>
API_KEY=<your c3 api key>

# the output should be the same as testcase_01_batch.log
./run_review.py -r 3.19.0-70.78~14.04.1 -u $API_USER -k $API_KEY --batch_limit 0 --oem
# the output should be the same as testcase_02_single.log
./run_review.py -s 112867 113076 -c 201508-18805 -u $API_USER -k $API_KEY --batch_limit 0
