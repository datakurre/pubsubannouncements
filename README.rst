Let’s do a simple publish-subscribe -scenario.

Let there be Plone Site A with some custom HTML form for sending announcement
messages::

    python bootstrap
    bin/buildout

    source bin/rabbitmq-env
    bin/rabbitmq-server

    bin/instance fg

And let there be other Plone sites, like B and C, to immediately act upon those
messages. For example, by making them visible for the current users::

    python bootstrap
    bin/buildout instance:http-address=8081

    bin/instance fg

Create Plone-site for all instances.

Open http://localhost:8080/Plone/@@send-announcement (or similar address
with your site id) for Site A and send announcement.

All sites will show the announcement (for the next requests).

Open the announcement from again and, this time, send an empty announcement.

All sites will hide the announcement (for the next requests).

.. image:: https://secure.travis-ci.org/datakurre/pubsubannouncements.png
     :target: http://travis-ci.org/datakurre/pubsubannouncements
