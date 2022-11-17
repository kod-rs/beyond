URLS
======

urls module contains all the paths that the backend exposes as an API towards
the frontend. For ease of access, every URL can be accessed as *url/url1* or
*url/url1/*, meaning that the trailing slash may or may not be included.
End user can access the following URLs (trailing slash may be included):

- BASE_URL/login
- BASE_URL/buildings
- BASE_URL/flexibility_demand
- BASE_URL/algorithm
- BASE_URL/flexibility_offer_confirmation
- BASE_URL/flexibility_offer

BASE_URL is URL on which the Flexopt application will be running at.

For detailed information about specific APIs refer to views. Short descriptions
are given here.

- /login: When a user tries to log in, a POST request containing username and
  password are sent. Response will contain user token if successful, and an
  error message otherwise (amongst other data being exchanged).

- /buildings: Once a user logs in, all the buildings that the user has access
  to need to be shown. Therefore, the first POST request to this URL will get a
  response containing all the buildings with their corresponding attributes
  such as building id, building name, and coordinates so that the building can
  be shown on a map. An aggregator can then choose some of the buildings
  through functionalities offered by the frontend. Chosen buildings represent
  the building set on which the flexibility will be calculated. A second POST
  request containing building ids of the aforementioned set will be sent to
  this URL. Response will contain consumption information for the selected
  buildings, and an error message otherwise.

- /flexibility_demand: An aggregator can request to see all the flexibility
  demands currently on the market. The POST response to this request will
  contain time intervals and requested flexibilities. If an error occurs, an
  appropriate message will be sent as a response instead.

- /algorithm: Once an aggregator selects buildings and a flexibility request,
  flexibility algorithm can be applied to that data. A POST request containing
  building consumption information and the time interval on which the
  flexibility wil be calculated is sent. The POST response to this request will
  contain the calculated total flexibility and flexibility per building. If an
  error occurs, an appropriate message will be sent as a response instead.

- /flexibility_offer_confirmation:  An aggregator may try different
  combinations of buildings and time intervals to get the most desired
  flexibility result according to aggregator's criteria. Once the aggregator
  is satisfied with the result, he may choose to save the result. That
  indicates that the aggregator plans to carry out the calculated flexibility.
  That result, called flexibility offer is then saved in the server's database.
  Once saved, the result can be accessed by the Beyond platform. To save the
  flexibility offer, the aggregator will forward all the data received by
  calculating the flexibility using /algorithm. The POST response to this
  request will contain a message indicating whether the saving process was a
  success or a failure.

- /flexibility_offer: **Beyond platform** can access saved flexibility offers
  through this URL. Flexibility offers that the platform can access are tied
  with either an aggregator or a building. By sending a POST request containing
  the desired time period and either a building id or a user id, the POST
  response will contain the information about the offered flexibility for
  that time period and that id (be it either a user of a building). If there
  is no flexibility found for that data of if an error occurs, the POST
  response will contain an appropriate error message.


.. automodule:: urls