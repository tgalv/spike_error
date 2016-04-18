# Health Check

curl http://0.0.0.0:5000

# 500

curl http://0.0.0.0:5000/div_zero

# 404

curl http://0.0.0.0:5000/foo

# 415 Unsupported Media Type

## Happy Path

#curl -X POST -d '{"name" : "Eggs", "price" : 34.99}' http://0.0.0.0:5000/json_post

curl -H "Content-Type: application/json" POST -d '{"name" : "Eggs", "price" : 34.99}' http://0.0.0.0:5000/json_post

## Failure Mode

curl -H "Content-Type: text/xml" -d @foo.xml -X POST http://0.0.0.0:5000/json_post

# 406 Accept Header Unacceptable (Content Negotiation)

curl -H "Content-Type: text/xml" -H accept:text/xml  -d @foo.xml -X POST http://0.0.0.0:5000/json_post

# 400 Schema Invalid

curl -X POST -d '{"name" : 11, "price" : "foo"}' http://0.0.0.0:5000/json_post