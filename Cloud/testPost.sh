BASE_URL=http://127.0.0.1:8000/sensor/
POST_ARGS="?a=1&b=how%20spaces&c=32"
YOUR_USER='sdpspot'
YOUR_PASS='sdpsp0t2017'
COOKIES=cookies.txt
CURL_BIN="curl -s -c $COOKIES -b $COOKIES -e $BASE_URL"

echo -n "Django Auth: get csrftoken ..."
$CURL_BIN $BASE_URL > /dev/null
DJANGO_TOKEN="csrfmiddlewaretoken=$(grep csrftoken $COOKIES | sed 's/^.*csrftoken\s*//')"

echo -n " perform post ..."
$CURL_BIN \
    -d "$DJANGO_TOKEN&username=$YOUR_USER&password=$YOUR_PASS" \
    -X POST $BASE_URL$POST_ARGS

