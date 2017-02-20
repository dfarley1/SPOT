BASE_URL=http://127.0.0.1:8000/sensor/
GET_ARGS="?sensor_id=1234"
POST_ARGS="sensor_id=1234&occ_status=1&occ_since=2017-02-20%2013:34:00&occ_license=4AME671"
YOUR_USER='sdpspot'
YOUR_PASS='sdpsp0t2017'
COOKIES=cookies.txt
CURL_BIN="curl -s -c $COOKIES -b $COOKIES -e $BASE_URL"

echo -n "Django Auth: get csrftoken ..."
$CURL_BIN $BASE_URL > /dev/null
DJANGO_TOKEN="csrfmiddlewaretoken=$(grep csrftoken $COOKIES | sed 's/^.*csrftoken\s*//')"

echo -n " perform post ..."
$CURL_BIN \
    -D - -d "$DJANGO_TOKEN&username=$YOUR_USER&password=$YOUR_PASS&$POST_ARGS" \
    -X POST $BASE_URL$GET_ARGS

