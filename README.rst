For Site A::

    python bootstrap
    bin/buildout

    source bin/rabbitmq-env
    bin/rabbitmq-server

    bin/instance fg

For Site B, C, etc..::

    python bootstrap
    bin/buildout instance:http-address=8081

    bin/instance fg

Create Plone-site for all instances.

Open http://localhost:8080/Plone/@@send-announcement (or similar address
with your site id) for Site A and send announcement.

All sites will show the announcement (for the next requests).

Open the announcement from again and, this time, send an empty announcement.

All sites will hide the announcement (for the next requests).
