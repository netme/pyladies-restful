.. title:: RESTful API

:skip-help: true
:data-transition-duration: 500
:css: styles.css

----

:id: title-slide


RESTful API
===========


Mikhail Chernykh (@netme)

.. image:: https://rhodecode.com/wp-content/uploads/2015/04/logo-no-label-400px-277x300.png
    :height: 60px


----

API
===

**Application Programming Interface (API)** is a set of routines, protocols, and tools for building software applications. An API expresses a software component in terms of its operations, inputs, outputs, and underlying types. An API defines functionalities that are independent of their respective implementations, which allows definitions and implementations to vary without compromising each other. A good API makes it easier to develop a program by providing all the building blocks. A programmer then puts the blocks together.


http://en.wikipedia.org/wiki/Application_programming_interface

----

REST
====

**Representational State Transfer (REST)** is a software architecture style consisting of guidelines and best practices for creating scalable web services.

http://en.wikipedia.org/wiki/Representational_state_transfer

----

RESTful API
===========

Web service APIs that adhere to the REST architectural constraints are called **RESTful APIs**. HTTP based RESTful APIs are defined with these aspects:

* base URI, such as http://example.com/resources/
* an Internet media type for the data. This is often JSON.
* standard HTTP methods (e.g., GET, PUT, POST, or DELETE)
* hypertext links to reference state
* hypertext links to reference related resources

http://en.wikipedia.org/wiki/Representational_state_transfer

----

Advantages :)
=============

* Uses the power of the HTTP protocol
* API is cleaner and easier to understand
* Maps perfectly to CRUD actions
* Gives a lot of flexibility to the developer

----

Disadvantages :(
================

* Requires to follow some rules to keep the API clean
* Not all actions easily map to CRUD
* Not all the HTTP clients are supporting the required HTTP methods (e.g. PATCH)

----

Disadvantages :(
================

.. code:: http

    PUT /books/123/ HTTP/1.1
    Host: example.com
    Authentication: MySuperSecureAPIKey

    {
        'method': 'PATCH',
        ...
    }

----

BookStore API Features:
=======================

* List all the books
* Show details for selected book
* Add the new book to the list
* Change the existing item
* Change the item price
* Remove the item from the list
* Show order list
* Show order details
* Create a new order
* Cancel order

----

BookStore API Endpoints
=======================

* `/books/`
* `/orders/`

----

HTTP Methods
============

* `GET` (Read)
* `POST` (Create)
* `PUT` (Update)
* `PATCH` (Partial Update)
* `DELETE` (Delete)

----

GET Request
===========

.. code:: http

    GET /books/123/ HTTP/1.1
    Host: example.com
    Authentication: MySuperSecureAPIKey

----


GET Response
============

.. code:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "url": "/books/123/",
        "name": "Django Book",
        "price": "29.90"
    }

----

POST Request
============

.. code:: http

    POST /books/ HTTP/1.1
    Host: example.com
    Authentication: MySuperSecureAPIKey

    {
        "name": "Python Cookbook",
        "price": "39.90"
    }

----

POST Response
=============

.. code:: http

    HTTP/1.1 201 Created
    Content-Type: application/json

    {
        "id": 124,
        "url": "/books/124/"
    }

----

PUT Request
===========

.. code:: http

    PUT /books/124/ HTTP/1.1
    Host: example.com
    Authentication: MySuperSecureAPIKey

    {
        "name": "Python 3 Cookbook",
        "price": "35.90"
    }

----

PUT Response
============

.. code:: http

    HTTP/1.1 204 No Content


----

PATCH Request
=============

.. code:: http

    PATCH /books/124/ HTTP/1.1
    Host: example.com
    Authentication: MySuperSecureAPIKey

    {
        "price": "33.90"
    }

----

PATCH Response
==============

.. code:: http

    HTTP/1.1 204 No Content

----

DELETE Request
==============

.. code:: http

    DELETE /books/124/ HTTP/1.1
    Host: example.com
    Authentication: MySuperSecureAPIKey

----

DELETE Response
===============

.. code:: http

    HTTP/1.1 204 No Content

----

HTTP URL Parameters
===================

Usage: Send some parameters to the API, e.g. filters.

.. code:: http

    GET /books/?price_more_than=35.00 HTTP/1.1


----

HTTP Headers
============

Usage: Send some hidden parameters to the API, e.g. some flags which are  changing behaviour.

.. code:: http

    DELETE /books/124/ HTTP/1.1
    Host: example.com
    Authentication: MySuperSecureAPIKey
    X-Show-Archived-Books: true
    X-Show-Archived-Books-Since: 2014-06-01


----

HTTP Body Payload
=================

Usage: Send some data to the API.

.. code:: http

    POST /books/ HTTP/1.1
    Host: example.com
    Authentication: MySuperSecureAPIKey

    {
        "name": "Python Cookbook",
        "price": "39.90"
    }


----

:id: status-codes-slide


HTTP Status codes
=================

========================= ==================
Status Code               When to use
========================= ==================
200 OK                    Successful GET request
201 Created               Successful POST request
202 Accepted              When data is accepted for computation
204 No Content            Successful PUT, PATCH and DELETE
400 Bad Request           The provided data has errors
401 Unauthorized          User is unauthorized
403 Forbidden             User has not enough permissions
405 Method Not Allowed    When a provided HTTP method is not supported
409 Conflict              The given data has conflicts with existing data
500 Application Error     Oh noooooo :-(
========================= ==================


----

REST Clients
============

* POSTman (Chrome)
* Advanced REST Client (Chrome)
* curl (command line)


----

Let's Practice
==============

GitHub: netme/pyladies-restful


----

Links
=====

* http://www.restapitutorial.com/
* http://github.com/netme/pyladies-restful
