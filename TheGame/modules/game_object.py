import pyglet
from modules import utils


class GameObject(pyglet.sprite.Sprite):
    """
    A class to define a generic object in the simulation.
    This class itself is derived from the pyglet.sprite.Sprite class
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the class object.
        :param args: additional positional arguments
        :param kwargs: additional keyword arguments
        """
        super(GameObject, self).__init__(*args, **kwargs)

        # Declaring all the common member variables of the class
        self.batch = kwargs.get("batch", None)  # batch to which this object belongs
        self.group = kwargs.get("group", None)  # group to which this object belongs

        self.type = None  # object type - card etc
        self.child_objects = []  # List of objects that can be spawned by this object
        self.sim_state = None  # State of the object - useful in a state machine
        self.dead = False  # whether this object has to be removed from screen or not
        self.collision_radius = 0  # circle collider radius
        self.collider_type = None  # "circle" or "polygon"
        self.event_handlers = []  # Tell the game handler about any event handlers

    def update_object(self, dt):
        """
        Virtual update_object function. This is not named update because the Sprite object has a
        function called update
        """
        pass