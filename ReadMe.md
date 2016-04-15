# Health Check

curl http://0.0.0.0:5000

# 500

curl http://0.0.0.0:5000/div_zero

# 404

curl http://0.0.0.0:5000/foo

# Content Negotiation

curl -H "Content-Type: application/json" -X POST -d '{"city":"plymouth"}' http://0.0.0.0:5000/json_post

curl -H "Content-Type: text/xml" -H accept:text/xml  -d @foo.xml -X POST http://0.0.0.0:5000/json_post
