#BASE_URL=http://127.0.0.1:8000/sensor/
BASE_URL=http://alien-walker-157903.appspot.com/sensor/
GET_ARGS="?sensor_id=1234"
POST_ARGS="occ_status=1&occ_since=2017-02-20%2013:34:00&occ_license=4AME671"
COOKIES=cookies.txt
CURL_BIN="curl -s -c $COOKIES -b $COOKIES -e $BASE_URL"

echo -n "GETing csrftoken ..."
$CURL_BIN $BASE_URL$GET_ARGS > /dev/null
DJANGO_TOKEN="csrfmiddlewaretoken=$(grep csrftoken $COOKIES | sed 's/^.*csrftoken\s*//')"

echo -n " POSTing ...\n"
$CURL_BIN \
    -D - -d "$DJANGO_TOKEN&$POST_ARGS" \
    -X POST $BASE_URL$GET_ARGS

echo "Finished File Transfer!"
