import json
import urllib2
import hashlib

upload_url = "" # Provided by b2_get_upload_url
upload_authorization_token = "" # Provided by b2_get_upload_url
file_data = "Now, I am become Death, the destroyer of worlds."
file_name = "oppenheimer_says.txt"
content_type = "text/plain"
sha1_of_file_data = hashlib.sha1(file_data).hexdigest()

headers = {
    'Authorization' : upload_authorization_token,
    'X-Bz-File-Name' :  file_name,
    'Content-Type' : content_type,
    'X-Bz-Content-Sha1' : sha1_of_file_data
}
request = urllib2.Request(upload_url, file_data, headers)

response = urllib2.urlopen(request)
response_data = json.loads(response.read())
response.close()