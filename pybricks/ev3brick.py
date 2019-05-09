"""LEGO® MINDSTORMS® EV3 Brick."""

from parameters import Color
from _common import Speaker, Display, Battery


def buttons():
    """Check which buttons on the EV3 Brick are currently pressed.

    :returns: List of pressed buttons.
    :rtype: List of :class:`Button <parameters.Button>`

    Examples::

        # Do something if the left button is pressed
        if Button.LEFT in brick.buttons():
            print("The left button is pressed.")

    ::

        # Wait until any of the buttons are pressed
        while not any(brick.buttons()):
            wait(10)

        # Wait until all buttons are released
        while any(brick.buttons()):
            wait(10)

    """
    pass


def light(color):
    """Set the color of the brick light.

    Arguments:
        color (Color): Color of the light. Choose ``Color.BLACK`` or ``None``
                       to turn the light off.

    Example::

        # Make the light red
        brick.light(Color.RED)

        # Turn the light off
        brick.light(None)
    """
    pass


sound = Speaker()
display = Display()
battery = Battery()