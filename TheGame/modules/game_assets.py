import pyglet


class GameAssets(object):
    def __init__(self, *args, **kwargs):
        """
        Initializes the class object.
        :param args: Additional positional arguments
        :param kwargs: Additional keyword arguments
        """
        super(GameAssets, self).__init__(*args, **kwargs)

        self.image_assets = dict()  # dictionary of image assets
        self.sound_assets = dict()  # dictionary of sound assets

        self.load_assets()

    @staticmethod
    def set_anchor_at_centre(image):
        """
        Sets the anchor of an image to its centre
        :param image: Image whose anchor has to be set
        """
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2


    def create_image_asset(self, keyword, file, centered=True):
        """
        Creates an image asset from the specified file and adds it to the
        dictionary of image assets using the specified keyword
        :param keyword: Keyword with which to name the asset
        :param file: File from which to create the asset
        :param centered: Boolean indicating if the anchor has to be centered.
                        Default is True. If False, anchor is at bottom left.
        """
        image_asset = pyglet.resource.image(file)
        if centered:
            self.set_anchor_at_centre(image_asset)
        self.image_assets.update({keyword: image_asset})


    def create_sound_asset(self, keyword, file, shouldStream=False):
        """
        Creates an audio asset from the specified file and adds it to the
        dictionary of sound assets using the specified keyword
        :param keyword: Keyword with which to name the asset
        :param file: File from which to create the asset
        :param shouldStream: True if the source should be streamed from disk
                          False if it should be entirely decoded into memory immediately.
        """
        sound_asset = pyglet.resource.media(file, streaming=shouldStream)
        self.sound_assets.update({keyword: sound_asset})


    def load_assets(self):
        pyglet.resource.path = ["resources"]
        pyglet.resource.reindex()

        ## load images
        self.create_image_asset("img_card_blank", "images/img_card_blank.png", True)
        
        
        ## load audio assets
        self.create_sound_asset("snd_default_bkg", "sounds/taureon-background-loop-straight-04-2699.mp3", True)
        