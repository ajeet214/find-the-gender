# find-the-gender
determination of  the gender of a first name
Single Usage: 
An example of genderizing a single name could look like this.

requests.get("https://api.genderize.io/?name=patrick")

This would render a JSON response like the following. The count represents the number of data entries examined in order to calculate the response.
response:  {"name":"patrick","gender":"male","probability":1,"count":2877}

Multiple Usage:

To genderize multiple names at a time, send along an array as the name parameter.

The API is limited to a maximum of 10 names per request

requests.get("https://api.genderize.io/?name[0]=patrick&name[1]=allen&name[2]=sophiya")

response: 
[{"name":"patrick","gender":"male","probability":1,"count":2877},{"name":"allen","gender":"male","probability":0.99,"count":561},{"name":"sophiya","gender":"female","probability":1,"count":1}]

Localization

To achieve more qualified guesses, it is also possible to use localization filters to retreive a guess based only on data for a certain country or language. It's recommended to always use a filter if you have the needed data, since naming can rely heavily on demographics.

The endpoint accepts two optional localization parameters.

1. country_id string Adds a filter with the following country ID - optional
2. language_id string Adds a filter with the following language ID - optional
Both parameters are availible both when genderizing a single or multiple names.

An example could look like this.

requests.get("https://api.genderize.io/?name=kim&country_id=dk")
