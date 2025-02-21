"""Load resources.

Classes:

    GameResources
"""

import logging
import pygame


class GameResources:
    """Resource loader."""

    __instance = None
    """Resources instance."""
    __is_loaded = False
    """Resource list is loaded."""
    resources = {}
    """Resources dictionary."""
    logger = logging.getLogger('resource')

    def __init__(self):
        self.logger.debug("Create resources list")
        GameResources.__instance = self
        self.load()

    @classmethod
    def instance(cls):
        """Get resouces instance.

        Returns:
            GameResources: Resources instance.
        """
        if cls.__instance is None:
            cls()

        return cls.__instance

    @classmethod
    def get(cls, resource_id):
        """Get resource by id.

        Args:
            resource_id (string): Id of resource.

        Returns:
            any: Resource.
        """
        return cls.instance().resources.get(resource_id)

    @classmethod
    def __load_resource(cls, resource_id, data):
        cls.resources[resource_id] = data
        cls.logger.debug(f"Resource \"{resource_id}\" is loaded")

    @classmethod
    def __load_resources(cls, *resources):
        for resource_id, data in resources:
            cls.__load_resource(resource_id, data)

    @classmethod
    def load_images(cls):
        return []

    @classmethod
    def load_spritesheets(cls):
        return []

    @classmethod
    def load_fonts(cls):
        return []

    @classmethod
    def load(cls):
        """Load resources list."""
        if cls.__is_loaded:
            return

        cls.logger.debug("Loading resources")
        cls.resources = {}

        # Images
        cls.logger.debug("Loading images")
        cls.__load_resources(*cls.load_images())

        # Spritesheets
        cls.logger.debug("Loading spritesheets")
        cls.__load_resources(*cls.load_spritesheets())

        # Fonts
        cls.logger.debug("Loading fonts")
        cls.__load_resources(*cls.load_fonts())

        cls.logger.debug("Resources are loaded")

        cls.__is_loaded = True
