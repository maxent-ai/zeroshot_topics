zeroshot_topics
===============

.. contents:: **Table of Contents**
    :backlinks: none

Installation
------------

zeroshot_topics is distributed on `PyPI <https://pypi.org>`_ as a universal
wheel and is available on Linux/macOS and Windows and supports
Python 3.7+ and PyPy.

.. code-block:: bash

    $ pip install zeroshot_topics

Usage
------

.. code-block:: python 

    from zeroshot_topics import ZeroShotTopicFinder
    zsmodel = ZeroShotTopicFinder()
    text = """can you tell me anything else okay great tell me everything you know about George_Washington. 
    he was the first president he was well he I'm trying to well he fought in the Civil_War he was a general 
    in the Civil_War and chopped down his father's cherry tree when he was a little boy he that's it."""
    zsmodel.find_topic(text)
    


License
-------

zeroshot_topics is distributed under the terms of

- `MIT License <https://choosealicense.com/licenses/mit>`_
- `Apache License, Version 2.0 <https://choosealicense.com/licenses/apache-2.0>`_
