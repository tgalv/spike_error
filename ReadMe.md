# Error Spike

This is the Spike Code for the [Investigate Generic Error Handler] (https://www.pivotaltracker.com/story/show/117047569) Story. 

Initial Investigations by Simon are on an old [branch] (https://github.com/LandRegistry/dm-deed-api/tree/CHORE4-api-exceptions).

# Purpose

To model the kinds of exceptions that might occur; as well as those identified by Simon it includes some demonstrations of Content Negotiation.

# Scope

The code is deliberately raw given the context of a Spike. I did not want to second guess a Land Registry Error Handling Framework. Rather seed some ideas as to what might need to be incorporated in the code in Refactorings as we move forward.

The example is an amalgamation of the responses of Client Facing services (showing rendering of web pages e.g. [Borrower Front End] (https://github.com/LandRegistry/dm-borrower-frontend)) and the responses hit by other Microservices such as the Conveyancers interaction with the [Deed API] (https://github.com/LandRegistry/dm-deed-api/).

# Tests

Unittests give a working example of the various Error Modes.

# Demo

The `examples.py` gives a demo against a running server using [requests] (http://docs.python-requests.org/en/master/).

The following Curl commands also demonstrate the different cases. 

## 200

curl -I http://0.0.0.0:5000

## 500

curl -I http://0.0.0.0:5000/div_zero

# 404

curl -I http://0.0.0.0:5000/foo

# 415 Unsupported Media Type

curl -H "Content-Type: text/xml" -d @foo.xml -X POST http://0.0.0.0:5000/json_post

# 406 Accept Header Unacceptable (Content Negotiation)

curl -H "Content-Type: text/xml" -H accept:text/xml  -d @foo.xml -X POST http://0.0.0.0:5000/json_post

# 400 Schema Invalid

curl -X POST -d '{"name":11,"price":"foo"}' http://0.0.0.0:5000/json_post