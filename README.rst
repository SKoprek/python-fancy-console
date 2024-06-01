Dev Fancy Console
=================

Stylized Python console, a project made for fun.

Overview
--------

Dev Fancy Console is a Python library for generating stylized console strings. It provides various features for customizing the appearance of text in the console.

Installation
------------

You can install Dev Fancy Console using pip:

.. code:: bash

    pip install dev-fancy-console

Usage
-----

Here are some code examples demonstrating how to use Dev Fancy Console:

Code example for Fancy Message
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    from dev_fancy_console import FancyMessage, FancyColors, FancyBackgroundColors, FancyStyles, FancyUtilities

    message = FancyMessage(
        message="Hello, world!",
        color=FancyColors.RED,
        background=FancyBackgroundColors.BLUE_BG,
        styles=[FancyStyles.BOLD],
        utility=FancyUtilities.UNDERLINE
    )
    print(message)

Code example for Fancy Message Segmented (Default values)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    from dev_fancy_console import FancyMessage, FancyMessageSegmented

    segmented_message = FancyMessageSegmented([FancyMessage()])
    print(segmented_message)

Included Colors, Background Colors, and Styles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Dev Fancy Console library includes predefined colors, background colors, and styles that you can use for customizing your console output.

Example Simple Message
^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    example_1()

Example Simple Segmented Message
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    example_4()

License
-------

This project is licensed under the MIT License. See the LICENSE file for details.
