#!/bin/bash
#
# To user this script, please export the following env variables first:
#	API_USER
#	API_KEY
#

review_command='../py/run_review.py'

##############  Reviewd. PASS. Cleared False Alarms.################
# XPS 13 looks good. All false alarm cleared.
#$review_command -c 201508-18805 -s 112867 113535 -u $API_USER -k $API_KEY --batch_limit 0
#$review_command -c 201601-20439 -s 112945 113518 -u $API_USER -k $API_KEY --batch_limit 0
#$review_command -c 201601-20438 -s 112925 113519 -u $API_USER -k $API_KEY --batch_limit 0
#$review_command -c 201601-20489 -s 112821 113538 -u $API_USER -k $API_KEY --batch_limit 0
#$review_command -c 201603-20825 -s 113048 113517 -u $API_USER -k $API_KEY --batch_limit 0
#$review_command -c 201506-18539 -s 113077 113526 -u $API_USER -k $API_KEY --batch_limit 0
#$review_command -c 201601-20436 -s 112766 113641 -u $API_USER -k $API_KEY --batch_limit 0
#$review_command -c 201506-18549 -s 112197 113527 -u $API_USER -k $API_KEY --batch_limit 0
#$review_command -c 201511-19983 -s 113442 113528 -u $API_USER -k $API_KEY --batch_limit 0

######## Not fully tested because it was returned to CE-QA ##########
# currently results shows ok

#############  In Progress ########################################
# source list is weird.
# could not reproduce.
#$review_command -c 201603-20845 -s 113110 113696 -u $API_USER -k $API_KEY --batch_limit 0

$review_command -c 201603-20845 -s 113110 113696 -u $API_USER -k $API_KEY --batch_limit 0
############# Re-running ##########################################

